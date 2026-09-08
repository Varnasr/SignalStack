# SignalStack

The [Research Rundown](https://varna.substack.com) newsletter, archived in
full and made usable. Every post as Markdown, the recurring sections compiled
into standing reference pages, and the methods notes turned into scripts you
can run. Part of the [OpenStacks](https://openstacks.dev) family, beside the
three stacks rather than one of them. Status: Stable, per the family
[maintenance policy](https://github.com/Varnasr/OpenStacks-for-Change/blob/main/MAINTENANCE.md).

Site: [varnasr.github.io/SignalStack](https://varnasr.github.io/SignalStack/).

## What is here

| Folder | What it holds | How it is made |
| --- | --- | --- |
| [`archive/`](archive/) | All 13 posts from varna.substack.com (June 2024 to September 2026, about 26,000 words), newest first, each with front matter and a link to the original. `SECTIONS.md` indexes the recurring sections by edition. | `scripts/sync_substack.py`, from the public Substack API. Text is verbatim, typos included. |
| [`companions/`](companions/) | Eight pages, one per recurring section: research praxis (7 notes), disambiguation corner (10 entries), methods corner (4), datasets (1), researchers worth following (15 people), papers and reports (35), books and long reads (13), tools and resources (11). Every entry links to the edition it came from. | `scripts/build_companions.py`, from `archive/`. `--check` fails if they drift. |
| [`tools/`](tools/) | Four standard-library Python scripts that do what the newsletter's methods notes describe: `deletion_rate.py`, `poverty_lines.py`, `odds_likelihood.py`, `audits.py`. | Hand-written, 23 tests in `tests/`. |
| [`companions/errata.md`](companions/errata.md) | The two places the newsletter's own text is known to be wrong, found while building the tools. | Hand-written. |

## Reading it

Start with the [companions](companions/). A reader who wants the poverty-line
note does not care that it ran in May 2026; they want the note, and
[`praxis.md`](companions/praxis.md) has it beside the six others. The
[glossary](companions/glossary.md) is the fastest way in for anyone who has
had SIR, NPR and NRC, or BPL, SECC and MPI, run together in a meeting.

The [archive](archive/) is for reading an edition as it was sent.
[`SECTIONS.md`](archive/SECTIONS.md) is the map: which edition carries which
section.

## Running the tools

Nothing to install beyond Python 3.10 or later; pytest for the tests.

```bash
python tools/deletion_rate.py --removed 4700000 --roll 78900000 --stage draft
python tools/poverty_lines.py --year 2023
python tools/poverty_lines.py --check 1622 --line tendulkar_rural
python tools/odds_likelihood.py table 75 25 50 50
python tools/audits.py recommendation tools/examples/recommendations.json

python -m pytest tests/          # 23 tests
```

Each script's docstring names the edition and the note it comes from, and
states the formula it applies. [`tools/README.md`](tools/README.md) says
what each one is for and what it deliberately does not do.

## Keeping it current

```bash
python scripts/sync_substack.py             # pull new posts; --check exits 1 if behind
python scripts/build_companions.py          # rebuild companions/; --check exits 1 if stale
```

`.github/workflows/sync-substack.yml` runs both on the second of each month
and opens a pull request when anything changed. Nothing reaches `main`
without the tests and the content lints passing.

## The family

| Repository | What it is for | Language |
| --- | --- | --- |
| [InsightStack](https://github.com/Varnasr/InsightStack) | MEL tools, calculators, research documentation, loaders for real survey microdata | Stata, Python, R, SPSS |
| [FieldStack](https://github.com/Varnasr/FieldStack) | Field operations: high-frequency checks, enumerator monitoring, back-checks, sampling and weighted estimation | R |
| [EquityStack](https://github.com/Varnasr/EquityStack) | Distributional analysis and design-based survey estimation from a development-economics view | Python |

[openstacks.dev](https://openstacks.dev) is the index for all of it.
SignalStack is the companion archive for the
[Research Rundown](https://varna.substack.com) newsletter, alongside the
stacks rather than one of them.
[PolicyStack](https://github.com/Varnasr/PolicyStack) is superseded by
[PolicyDhara](https://github.com/Varnasr/PolicyDhara). RootStack, BridgeStack
and ViewStack are archived.

## Citation

See [`CITATION.cff`](CITATION.cff). The newsletter itself is cited as
Sri Raman, Varna, *The Research Rundown*, varna.substack.com, with the
edition date; this repository is the archive, not the publication.

## License

MIT. See [LICENSE](LICENSE). The newsletter text in `archive/` is the
author's, republished here by the author.
