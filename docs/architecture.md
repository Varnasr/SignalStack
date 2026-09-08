# Architecture

## The pipeline

```text
varna.substack.com  --(sync_substack.py)-->  archive/*.md
                                                 |
                              (build_companions.py)
                                                 v
                                          companions/*.md
```

`scripts/sync_substack.py` pages `/api/v1/archive?sort=new` to list posts,
fetches each post's `body_html` from `/api/v1/posts/<slug>`, converts it
with a small `HTMLParser` subclass, and writes the file with front matter.
It then rewrites `archive/README.md` and `archive/SECTIONS.md`. `--check`
compares the listing with the files on disk and exits 1 if the archive is
behind, without writing.

`scripts/build_companions.py` splits every archived post on its `##`, `###`
and `####` headings, matches section headings against a small keyword table,
and derives each entry's title from the heading suffix, a sub-heading, or a
bold first line, in that order. `--check` rebuilds to memory and exits 1 if
the eight generated files would change.

## Why generated

The previous contents of this repository were written by hand and described
as the newsletter's issues. They matched no edition. A generated archive can
be wrong in one way only, a converter bug, and that is fixed once in the
script rather than post by post.

## Workflows

| Workflow | Trigger | What it does |
| --- | --- | --- |
| `tests.yml` | push, PR | `pytest tests/` and `build_companions.py --check` |
| `lint-content.yml` | push, PR | markdownlint, cspell, lychee on hand-written Markdown; generated files excluded |
| `sync-substack.yml` | monthly, manual | sync, rebuild, open a PR if anything changed |
| `deploy-pages.yml` | push to main | Jekyll build and deploy |

The sync never pushes to main. A pull request runs the tests and lints first
and a person merges it.

## Site

GitHub Pages, Jekyll, `jekyll-readme-index`, no theme. `_config.yml` applies
`_layouts/default.html` to every Markdown page, so a click-through from the
landing page keeps the house style. `assets/css/stack.css` is the same file
as in InsightStack, FieldStack and EquityStack.

## Git hooks

`npm install` sets `core.hooksPath` to `.githooks/`. `commit-msg` enforces
the prefix convention in `CONTRIBUTING.md`; `pre-commit` blocks credential
files and merge-conflict markers.
