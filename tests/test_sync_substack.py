"""Plain-assert tests for scripts/sync_substack.py. No network: urlopen and
fetch_json are replaced, and time.sleep is patched so retries run at once.

Run: python -m pytest tests/
"""

import io
import json
import sys
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import sync_substack as sync  # noqa: E402


class _Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def _http_error(code):
    return urllib.error.HTTPError("https://x", code, "err", {}, None)


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    monkeypatch.setattr(sync.time, "sleep", lambda s: None)


def _urlopen_sequence(monkeypatch, outcomes):
    calls = iter(outcomes)

    def fake(req, timeout=None):
        outcome = next(calls)
        if isinstance(outcome, Exception):
            raise outcome
        return _Response(json.dumps(outcome).encode())

    monkeypatch.setattr(sync.urllib.request, "urlopen", fake)


# ---------------------------------------------------------------- fetch_json

def test_a_403_then_a_200_returns_the_payload(monkeypatch):
    _urlopen_sequence(monkeypatch, [_http_error(403), [{"slug": "a"}]])
    assert sync.fetch_json("https://x") == [{"slug": "a"}]


def test_a_network_error_then_success_returns_the_payload(monkeypatch):
    _urlopen_sequence(monkeypatch, [urllib.error.URLError("reset"), {"ok": 1}])
    assert sync.fetch_json("https://x") == {"ok": 1}


def test_repeated_failure_exits_with_the_fetch_code_and_names_the_url(monkeypatch, capsys):
    _urlopen_sequence(monkeypatch, [_http_error(403)] * (len(sync.RETRY_WAITS) + 1))
    with pytest.raises(SystemExit) as e:
        sync.fetch_json("https://varna.substack.com/api/v1/archive")
    assert e.value.code == sync.FETCH_FAILED == 2
    err = capsys.readouterr().err
    assert "HTTP 403" in err and "varna.substack.com/api/v1/archive" in err


def test_repeated_network_errors_end_on_one_line_not_a_traceback(monkeypatch, capsys):
    _urlopen_sequence(monkeypatch, [urllib.error.URLError("dns")] * (len(sync.RETRY_WAITS) + 1))
    with pytest.raises(SystemExit) as e:
        sync.fetch_json("https://x")
    assert e.value.code == 2
    assert "Could not reach https://x" in capsys.readouterr().err


def test_a_404_is_not_retried(monkeypatch):
    _urlopen_sequence(monkeypatch, [_http_error(404), {"never": "reached"}])
    with pytest.raises(SystemExit):
        sync.fetch_json("https://x")


# ---------------------------------------------------------------- list_posts

def _pages(monkeypatch, pages):
    """Serve `pages` in order, each as the cursor-shaped answer Substack gives
    since November 2026: {"posts": [...], "nextCursor": "..." or None}. The URLs
    asked for are kept in the returned list."""
    it = iter(pages)
    urls = []

    def fake(url):
        urls.append(url)
        return next(it)

    monkeypatch.setattr(sync, "fetch_json", fake)
    return urls


def _posts(start, n):
    return [{"id": i, "slug": f"p{i}"} for i in range(start, start + n)]


def _page(posts, cursor):
    return {"posts": posts, "nextCursor": cursor}


def test_short_pages_do_not_end_the_listing(monkeypatch):
    # Substack returned 23 and then 19 on 6 October 2026. Only a missing cursor
    # or an empty page ends the listing.
    _pages(monkeypatch, [_page(_posts(0, 23), "a"), _page(_posts(23, 19), "b"), _page([], None)])
    assert len(sync.list_posts()) == 42


def test_overlapping_pages_keep_each_post_once(monkeypatch):
    _pages(monkeypatch, [_page(_posts(0, 23), "a"), _page(_posts(20, 6), "b"), _page([], None)])
    got = sync.list_posts()
    assert [p["id"] for p in got] == list(range(26))


def test_the_listing_follows_the_cursor_and_never_sends_offset(monkeypatch):
    # Substack answers HTTP 400 to `offset` and to a `limit` above 25.
    urls = _pages(monkeypatch, [_page(_posts(0, 25), "abc=="), _page(_posts(25, 24), None)])
    assert len(sync.list_posts()) == 49
    assert len(urls) == 2
    assert all("offset" not in u for u in urls)
    assert "cursor=" not in urls[0] and "limit=25" in urls[0]
    assert "cursor=abc%3D%3D" in urls[1]


def test_the_page_cap_stops_a_listing_that_never_ends(monkeypatch):
    count = iter(range(10**6))

    def endless(url):
        n = next(count)
        return _page([{"id": n, "slug": f"p{n}"}], f"c{n}")

    monkeypatch.setattr(sync, "fetch_json", endless)
    assert len(sync.list_posts()) == sync.PAGE_CAP


# ---------------------------------------------------------------- indexes and dry run

def _archived(tmp, name, title, day):
    (tmp / name).write_text(
        f'---\ntitle: {json.dumps(title)}\ndate: {day}\ntype: edition\nurl: https://x/{name}\n'
        f'subtitle: ""\nsource: test\n---\n\n# {title}\n\n## Research praxis\n', encoding="utf-8")


def _post(slug, day, title):
    return {"slug": slug, "post_date": f"{day}T06:00:00.000Z", "title": title,
            "canonical_url": f"https://varna.substack.com/p/{slug}", "subtitle": ""}


def test_a_partial_listing_keeps_every_archived_post_in_the_index(monkeypatch, tmp_path):
    monkeypatch.setattr(sync, "ARCHIVE", tmp_path)
    _archived(tmp_path, "2026-08-01-old-one.md", "Research Rundown | August", "2026-08-01")
    _archived(tmp_path, "2026-07-01-old-two.md", "Research Rundown | July", "2026-07-01")
    new = _post("new-one", "2026-09-01", "Research Rundown | September")
    sync.write_post(new, {"body_html": "<h2>Research praxis</h2><p>x</p>"})
    sync.build_indexes([new])
    readme = (tmp_path / "README.md").read_text(encoding="utf-8")
    for name in ("2026-09-01-new-one.md", "2026-08-01-old-one.md", "2026-07-01-old-two.md"):
        assert name in readme
    assert readme.index("2026-09-01") < readme.index("2026-08-01") < readme.index("2026-07-01")
    assert "3 posts" in readme


def test_dry_run_writes_nothing(monkeypatch, tmp_path):
    monkeypatch.setattr(sync, "ARCHIVE", tmp_path)
    _archived(tmp_path, "2026-08-01-old-one.md", "Research Rundown | August", "2026-08-01")
    before = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    monkeypatch.setattr(sync, "list_posts", lambda: [_post("new-one", "2026-09-01", "Daily")])
    monkeypatch.setattr(sync, "fetch_json", lambda url: {"body_html": "<p>x</p>"})
    assert sync.main(["--dry-run"]) == 0
    assert {p.name: p.read_bytes() for p in tmp_path.iterdir()} == before
