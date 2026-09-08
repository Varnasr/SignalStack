# Architecture

```text
varna.substack.com  --(sync_substack.py)-->  archive/*.md  --(build_companions.py)-->  companions/*.md
```

`scripts/sync_substack.py` lists posts from `/api/v1/archive`, fetches each
post's HTML from `/api/v1/posts/<slug>`, converts it to Markdown and writes
the file with front matter, then rewrites `archive/README.md` and
`archive/SECTIONS.md`. `--check` exits 1 if Substack has posts the archive
does not.

`scripts/build_companions.py` splits each post on its headings, matches
section headings against a keyword table, and writes the eight companion
pages. `--check` exits 1 if they would change.

## Workflows

| Workflow | Trigger | Runs |
| --- | --- | --- |
| `tests.yml` | push, PR | `pytest tests/`, `build_companions.py --check` |
| `lint-content.yml` | push, PR | markdownlint, cspell, lychee on hand-written Markdown |
| `sync-substack.yml` | monthly, manual | sync, rebuild, open a PR if anything changed |
| `deploy-pages.yml` | push to main | Jekyll build and deploy |

## Site

GitHub Pages, Jekyll, `jekyll-readme-index`, no theme. `_config.yml` applies
`_layouts/default.html` to every Markdown page. `assets/css/stack.css` is
shared with InsightStack, FieldStack and EquityStack.

## Git hooks

`npm install` sets `core.hooksPath` to `.githooks/`. `commit-msg` checks the
prefix convention in `CONTRIBUTING.md`; `pre-commit` blocks credential files
and merge-conflict markers.
