# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [2026.2.0] - 2026-09-08

### Changed

- The repository is now a generated archive of the real newsletter at
  varna.substack.com. `scripts/sync_substack.py` writes all 13 posts to
  `archive/` from the public Substack API, with an index and a
  recurring-sections index.
- `scripts/build_companions.py` compiles eight companion pages from the
  archive: research praxis, disambiguation corner, methods corner, datasets,
  researchers, papers and reports, books and long reads, tools and resources.
- Four tested scripts in `tools/`: `deletion_rate.py`, `poverty_lines.py`,
  `odds_likelihood.py`, `audits.py`. 23 tests in `tests/`, run in CI.
- House-style landing page and layout (`assets/css/stack.css`,
  `_layouts/default.html`), no Jekyll theme.
- Monthly `sync-substack.yml` workflow opens a pull request with new posts.
- `companions/errata.md` records the two known errors in the newsletter's
  own text.

### Removed

- `issues/`, `featured/`, `extras/` and `index.md`. The two "issues" did not
  correspond to any edition of the newsletter; the featured page and book
  companion were unrelated to it. Links to `researchrundown.substack.com`,
  which is not the newsletter's address.

## [2026.1.0] - 2026-08-28

### Added

- Initial repository: two issue summaries, one featured tool page, one book
  companion, documentation and content lints.
