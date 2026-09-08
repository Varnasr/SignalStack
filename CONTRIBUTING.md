# Contributing

Most of this repository is generated, so most contributions are to the
scripts rather than the content.

## What to change where

| You want to | Change |
| --- | --- |
| Fix how a post renders in `archive/` | `scripts/sync_substack.py` (`_ToMarkdown`), then re-run it. Never edit `archive/` by hand; the next sync overwrites it. |
| Fix how a companion page is compiled | `scripts/build_companions.py` (`entries()`, `people()`), then re-run it. Never edit the eight generated pages. |
| Record an error in the newsletter's text | `companions/errata.md`. The archive stays verbatim. |
| Add or fix a tool | `tools/`, with a test in `tests/test_tools.py` pinned to a closed-form answer or a cited figure. |
| Fix the site | `index.html`, `_layouts/default.html`, `assets/css/stack.css`. The CSS is shared with the other stacks; change it in one place and copy it. |

The newsletter itself is not edited here. It is published on Substack by its
author and archived by script.

## Before opening a pull request

```bash
python -m pytest tests/
python scripts/build_companions.py --check
```

Markdown you write by hand is linted with markdownlint and cspell in CI, and
its links checked with lychee. Generated files are excluded from all three.

## Commit messages

Start with one of `Add:`, `Fix:`, `Update:`, `Docs:`, `Refactor:`, `Test:`,
`CI:`, `Chore:`. The `commit-msg` hook in `.githooks/` enforces it;
`npm install` installs the hook.
