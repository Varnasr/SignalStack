# SignalStack

Companion archive for the Research Rundown newsletter at
[varna.substack.com](https://varna.substack.com). Part of the
[OpenStacks](https://openstacks.dev) family, beside the three stacks rather
than one of them. Status: Stable, per the family
[maintenance policy](https://github.com/Varnasr/OpenStacks-for-Change/blob/main/MAINTENANCE.md).

## What it is, and what it was

Before 2026-09-08 this repository held two "issues" (June 2024, April 2025)
whose contents had nothing in common with the editions of those dates on
Substack, a "featured" page on Excel AI tools, and a book companion for a
book the newsletter never mentioned. The README linked
`researchrundown.substack.com`, which holds one "Coming soon" post. None of
it was the newsletter. All of it was deleted.

What replaced it is generated from the real thing. Three layers, in order of
how much a session should worry about them:

- **`archive/`** is written by `scripts/sync_substack.py` from the public
  Substack API (`/api/v1/archive` to list, `/api/v1/posts/<slug>` for
  `body_html`). Do not edit files there; a re-sync overwrites them. The text
  is the newsletter's, verbatim, including the corrupted words in the August
  2025 edition ("createifferently", "DVisualisationtion"), which are in the
  Substack source. If a rendering looks wrong, fix the converter
  (`_ToMarkdown`) and re-sync.
- **`companions/`** is written by `scripts/build_companions.py` from
  `archive/`. Eight generated pages plus two hand-written ones, `README.md`
  and `errata.md`. `--check` fails CI if the generated eight are stale.
- **`tools/`** is hand-written and tested. Each script does what one methods
  note in the newsletter describes and names the edition in its docstring.

## Heading conventions in the archive, so the builder is not "fixed" back

The newsletter's structure changed across years and `build_companions.py`
reconciles it. The 2024-25 editions use `## Research praxis` with a `###`
sub-heading carrying the note's title; the August 2025 and March 2026
editions put emoji and bold in the `##` heading and lead with a bold line;
the 2026 editions put the title after a colon (`## Research Praxis: How to
Read a Deletion Rate`) and separate entries with `---`. Researchers are `###`
sub-headings in 2024-25 and bold `Name — Affiliation` leads from 2026. The
rules are in `entries()` and `people()`, with the order of preference
written down. Add a case there rather than editing generated output.

Two converter bugs worth remembering. Void tags (`<img>`, `<br>`) were once
pushed onto the tag stack and never popped, so a stale `li` joined every
later paragraph of a post onto one line; `VOID` exists for that. A `<p>`
inside `<blockquote>` emitted a bare quote marker on its own line; it now starts a fresh quoted line.

## Tools: what each refuses to do

- `deletion_rate.py` has no default attrition rate. The user supplies the
  crude death rate and out-migration rate with a source; the crude death rate
  is a floor for an adult-only roll, and the output says so.
- `poverty_lines.py` converts lines to one unit for reading a table. It is
  not a headcount and says so; the World Bank's own conversion uses a
  survey-year CPI and the rural/urban split. Figures in `DATA` each have a
  named source in the docstring; `--fetch` refreshes PPP and CPI from the
  World Bank API and prints a diff rather than writing.
- `odds_likelihood.py` has no hypothesis test. Likelihood is shown on a grid
  and a test asserts it does not integrate to one.
- `audits.py` classifies a participation design as consultation,
  collaboration or community control and prints that none of the three is
  the correct model. That sentence is the newsletter's point; keep it.

## The Rs 1,622 finding

The May 2026 edition gives the Tendulkar rural line as "roughly Rs 1,622 per
person per month ... at 2011-12 prices". The 2011-12 figure is Rs 816
(Planning Commission, 22 July 2013). Rs 816 inflated to 2023 prices by the
World Bank CPI series is Rs 1,625. So the number is right and the year label
is wrong. It is recorded in `companions/errata.md` and asserted by a test;
do not "correct" the archive, which is verbatim, and do not propagate the
label.

## Testing

`.github/workflows/tests.yml` runs `python -m pytest tests/` (23 tests) and
`build_companions.py --check` on pull requests and pushes to main.
`lint-content.yml` runs markdownlint, cspell and lychee over hand-written
Markdown; `archive/` and the generated companions are excluded from all three
because their text is not ours to lint. `sync-substack.yml` runs monthly and
opens a PR; it never pushes to main.

## Design references

The house style exists as a file: `assets/css/stack.css`, the same file as in
InsightStack, FieldStack and EquityStack. Change it in one place and copy it
to the others. 2px borders, no shadows, no border-radius, Bricolage Grotesque
uppercase for display, Work Sans for prose, JetBrains Mono for labels, colour
bands rather than floating cards, saffron `#f2a541` as the single accent. No
emoji anywhere in hand-written files; the archive keeps the newsletter's.

For anything the house style does not answer, draw from
[kombai.com/gallery/web](https://kombai.com/gallery/web).

GitHub Pages builds with `jekyll-readme-index` and no theme; `_config.yml`
applies `_layouts/default.html` to every Markdown page. A folder becomes a
page only if it holds a `README.md`. `archive/` and `companions/` both do.
After changing the landing page, load it at 390x844 and compare
`documentElement.scrollWidth` against `clientWidth`.
