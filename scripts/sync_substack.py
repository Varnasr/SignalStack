"""Pull every post of the Research Rundown from Substack into this repository.

    python scripts/sync_substack.py            # fetch, write, rebuild indexes
    python scripts/sync_substack.py --check    # exit 1 if the archive is behind

The newsletter is published at varna.substack.com. This reads Substack's
public archive API, converts each post's HTML to Markdown, and writes one file
per post under `archive/`, then rebuilds the indexes. Everything in `archive/`
is generated: edit the newsletter on Substack, not here, and re-run.

Why this exists. The repository used to hold two hand-written "issues" that
did not match the editions they were named after, and linked to a Substack
address that has one post on it. An archive that is a copy of the source
cannot drift from it; an archive that is somebody's summary of the source
already has.

Standard library only, so it runs anywhere Python does.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

PUBLICATION = "https://varna.substack.com"
ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "archive"
UA = {"User-Agent": "SignalStack sync (github.com/Varnasr/SignalStack)"}


def fetch_json(url: str):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def list_posts() -> list[dict]:
    out, offset = [], 0
    while True:
        page = fetch_json(f"{PUBLICATION}/api/v1/archive?sort=new&offset={offset}&limit=50")
        if not page:
            break
        out.extend(page)
        offset += len(page)
        if len(page) < 50:
            break
    return out


def classify(title: str) -> str:
    t = title.lower()
    if "daily" in t:
        return "daily"
    if "brief" in t:
        return "brief"
    if "research rundown" in t:
        return "edition"
    return "other"


class _ToMarkdown(HTMLParser):
    """Substack post HTML to Markdown. Covers what Substack actually emits:
    headings, paragraphs, lists, blockquotes, links, emphasis, images,
    horizontal rules, and its button/embed wrappers, which become links."""

    BLOCK = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
             "blockquote", "hr", "div", "figure", "figcaption", "pre"}
    # Elements with no end tag. They must never go on the tag stack: an
    # <img> or <br> left there once meant a list item's "li" was never popped,
    # so every later paragraph in the post was joined onto one line.
    VOID = {"br", "img", "hr", "input", "meta", "link", "source", "wbr", "col", "embed"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.stack: list[str] = []
        self.list_stack: list[tuple[str, int]] = []
        self.href: str | None = None
        self.skip = 0

    def _emit(self, s: str):
        self.out.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if tag in ("script", "style", "svg", "button"):
            self.skip += 1
            return
        if self.skip:
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._emit("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            # A paragraph inside a list item is the item's text; a blank line
            # there breaks the list into a bare marker and a paragraph. A
            # paragraph inside a blockquote starts a new quoted line.
            if "li" in self.stack:
                self._emit(" ")
            elif "blockquote" in self.stack:
                self._emit("" if self.out and self.out[-1] == "\n\n> " else "\n>\n> ")
            else:
                self._emit("\n\n")
        elif tag == "br":
            self._emit("  \n")
        elif tag == "hr":
            self._emit("\n\n---\n\n")
        elif tag in ("ul", "ol"):
            self.list_stack.append((tag, 0))
            self._emit("\n")
        elif tag == "li":
            kind, n = self.list_stack[-1] if self.list_stack else ("ul", 0)
            if self.list_stack:
                self.list_stack[-1] = (kind, n + 1)
            indent = "  " * (len(self.list_stack) - 1)
            marker = f"{n + 1}." if kind == "ol" else "-"
            self._emit(f"\n{indent}{marker} ")
        elif tag == "blockquote":
            self._emit("\n\n> ")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "code":
            self._emit("`")
        elif tag == "a":
            self.href = a.get("href")
            self._emit("[")
        elif tag == "img":
            src = a.get("src", "")
            alt = a.get("alt", "") or "image"
            if src:
                self._emit(f"![{alt}]({src})")
        elif tag == "figcaption":
            self._emit("\n*")
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg", "button"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in self.stack:
            # pop to the matching open tag, discarding anything left unclosed
            while self.stack and self.stack[-1] != tag:
                self.stack.pop()
            self.stack.pop()
        if tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "code":
            self._emit("`")
        elif tag == "a":
            self._emit(f"]({self.href})" if self.href else "]")
            self.href = None
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            self._emit("\n")
        elif tag == "figcaption":
            self._emit("*\n")
        elif tag == "blockquote":
            self._emit("\n")

    def handle_data(self, data):
        if self.skip:
            return
        self._emit(re.sub(r"\s+", " ", data))

    def result(self) -> str:
        s = "".join(self.out)
        s = re.sub(r"[ \t]+\n", "\n", s)
        s = re.sub(r"\n{3,}", "\n\n", s)
        return s.strip() + "\n"


def to_markdown(body_html: str) -> str:
    p = _ToMarkdown()
    p.feed(body_html)
    return p.result()


def slug_filename(post: dict) -> str:
    return f"{post['post_date'][:10]}-{post['slug']}.md"


def write_post(post: dict, full: dict) -> Path:
    kind = classify(post["title"])
    body = to_markdown(full.get("body_html") or "")
    fm = "\n".join([
        "---",
        f"title: {json.dumps(post['title'], ensure_ascii=False)}",
        f"date: {post['post_date'][:10]}",
        f"type: {kind}",
        f"url: {post['canonical_url']}",
        f"subtitle: {json.dumps(post.get('subtitle') or '', ensure_ascii=False)}",
        "source: varna.substack.com, fetched by scripts/sync_substack.py",
        "---",
    ])
    text = (f"{fm}\n\n# {post['title']}\n\n"
            f"*{post['post_date'][:10]}. Published at [{post['canonical_url']}]({post['canonical_url']}). "
            "This file is a generated copy; the Substack post is the original.*\n\n"
            + body)
    ARCHIVE.mkdir(exist_ok=True)
    path = ARCHIVE / slug_filename(post)
    path.write_text(text, encoding="utf-8")
    return path


def headings(md: str) -> list[str]:
    return [m.group(2).strip() for m in re.finditer(r"^(#{2,4}) (.+)$", md, re.M)]


def build_indexes(posts: list[dict]) -> None:
    posts = sorted(posts, key=lambda p: p["post_date"], reverse=True)
    lines = ["# Archive", "",
             f"{len(posts)} posts from [varna.substack.com]({PUBLICATION}), newest first. "
             "Generated by `scripts/sync_substack.py`; do not edit by hand.", "",
             "| Date | Type | Title |", "|---|---|---|"]
    for p in posts:
        title = p["title"].strip().replace("|", "\\|")      # a pipe in a title breaks the table
        lines.append(f"| {p['post_date'][:10]} | {classify(p['title'])} | [{title}]({slug_filename(p)}) |")
    (ARCHIVE / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Sections index: the recurring section headings across editions, so a
    # reader can follow "Research praxis" or "Researchers worth following"
    # through every issue without opening each one.
    by_section: dict[str, list[tuple[str, str, str]]] = {}
    for p in posts:
        md = (ARCHIVE / slug_filename(p)).read_text(encoding="utf-8")
        for h in headings(md):
            key = re.sub(r"[^a-z ]", "", h.lower()).strip()
            for canon in RECURRING:
                if key.startswith(canon):
                    by_section.setdefault(canon, []).append((p["post_date"][:10], p["title"], slug_filename(p)))
                    break
    lines = ["# Recurring sections", "",
             "Where each recurring section of the newsletter appears, by edition. "
             "Generated; do not edit by hand.", ""]
    for canon in RECURRING:
        hits = by_section.get(canon, [])
        if not hits:
            continue
        lines.append(f"## {canon.capitalize()}")
        lines.append("")
        for d, t, f in hits:
            lines.append(f"- {d}: [{t.strip()}]({f})")
        lines.append("")
    (ARCHIVE / "SECTIONS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


RECURRING = [
    "in this issue", "research praxis", "researchers worth following",
    "podcasts for the commute", "a small methods corner", "research history",
    "one book", "books", "one dataset to open", "disambiguation corner",
    "a visual detour", "documentary", "a south asia resource",
]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if the archive is behind Substack")
    args = ap.parse_args(argv)

    posts = list_posts()
    if args.check:
        missing = [p for p in posts if not (ARCHIVE / slug_filename(p)).exists()]
        print(f"{len(posts)} posts on Substack, {len(missing)} not archived")
        for p in missing:
            print("  ", p["post_date"][:10], p["title"])
        return 1 if missing else 0

    written = []
    for p in posts:
        full = fetch_json(f"{PUBLICATION}/api/v1/posts/{p['slug']}")
        written.append(write_post(p, full))
    build_indexes(posts)
    print(f"archived {len(written)} posts to {ARCHIVE.relative_to(ROOT)}/ (checked {date.today()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
