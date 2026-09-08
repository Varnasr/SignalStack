# Tools

Four scripts, each from one methods note in the newsletter. Standard
library only, Python 3.10 or later. `python -m pytest tests/` runs the
23 tests.

| Script | From | What it does |
| --- | --- | --- |
| `deletion_rate.py` | Research praxis, July 2026 | Reads an electoral-roll deletion figure: share of the roll, expected churn, draft or final, wrongful removals. |
| `poverty_lines.py` | Research praxis, May 2026 | Puts World Bank and Indian committee poverty lines in rupees per person per month at one price year. |
| `odds_likelihood.py` | Methods corner, June 2024 | Odds and probability; odds ratio against relative risk; a binomial likelihood on a grid. |
| `audits.py` | Research praxis, April 2025; methods note, June 2025 | Two checklists as JSON: the four questions for a recommendation, the eight questions for a participatory design. |

## deletion_rate.py

```bash
python tools/deletion_rate.py --removed 4700000 --roll 78900000 --stage draft
python tools/deletion_rate.py --removed 4700000 --roll 78900000 \
    --years 22 --death-rate 6.4 --out-migration-rate 4 --stage draft
```

Prints the four checks. Share of the roll. Expected attrition,
`roll x (1 - (1 - r)^years)`, and the excess or shortfall against it. Whether
the figure is a draft, and the restored share if you pass `--final-removed`.
The number of wrongful removals if you pass an audited `--wrongful-share`.

There is no built-in attrition rate. Pass the crude death rate (Sample
Registration System) and an out-migration rate (Census D-series or the PLFS
migration module) per thousand per year.

## poverty_lines.py

```bash
python tools/poverty_lines.py --year 2023
python tools/poverty_lines.py --check 1622 --line tendulkar_rural
python tools/poverty_lines.py --fetch
```

Ten lines in rupees per person per month: the World Bank lines at 2017 and
2021 PPPs, and the Tendulkar and Rangarajan lines, rural and urban. Dollar
lines are converted with the PPP factor for private consumption in the base
year, the CPI ratio to the target year, and 30.4375 days a month. Rupee lines
are inflated by the CPI ratio.

`--check` finds the price year at which a line comes closest to a figure you
have been given. `--fetch` pulls current PPP and CPI values from the World
Bank API and prints what changed. The sources for every figure are in the
docstring. This is for reading a table; it is not a poverty headcount.

## odds_likelihood.py

```bash
python tools/odds_likelihood.py odds 0.25
python tools/odds_likelihood.py table 75 25 50 50
python tools/odds_likelihood.py lik 7 20 --points 11
```

`odds` and `prob` convert between the two. `table` takes a 2x2 table
(exposed with the outcome, exposed without, unexposed with, unexposed
without) and prints relative risk, odds ratio and their ratio. `lik` prints
the binomial log-likelihood across values of p. No hypothesis test.

## audits.py

```bash
python tools/audits.py recommendation --template > recs.json
python tools/audits.py recommendation recs.json
python tools/audits.py participation --template > design.json
python tools/audits.py participation design.json
```

Fill in the JSON, run the check. It exits 1 until every question is
answered.

The recommendation audit asks four questions of each recommendation: which
finding supports it, what assumption connects the two, what evidence
supports the assumption, what would make it wrong. The participation audit
asks eight questions about who holds authority, each answered `researchers`,
`shared` or `participants`, and names the arrangement: consultation,
collaboration or community control. Worked examples are in `examples/`.
