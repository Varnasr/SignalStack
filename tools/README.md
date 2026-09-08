# Tools

Four scripts that do what the newsletter's methods notes describe. Standard
library only, Python 3.10 or later, each runnable from the command line and
importable. `python -m pytest tests/` runs the 23 tests; the expectations are
closed-form identities and cited figures, never a previous run's output.

| Script | From | The question it answers |
| --- | --- | --- |
| `deletion_rate.py` | Research praxis, July 2026 | Is "47 lakh electors removed" alarming, or ordinary churn? |
| `poverty_lines.py` | Research praxis, May 2026 | Is $2.15 a day more or less than the Tendulkar line, in rupees, this year? |
| `odds_likelihood.py` | Methods corner, June 2024 | Is an odds ratio of 3 "three times as likely"? What is a likelihood, if not a probability? |
| `audits.py` | Research praxis, April 2025; methods note, June 2025 | Does each recommendation rest on evidence? Does "participatory" match where authority sits? |

## deletion_rate.py

```bash
python tools/deletion_rate.py --removed 4700000 --roll 78900000 --stage draft
python tools/deletion_rate.py --removed 4700000 --roll 78900000 \
    --years 22 --death-rate 6.4 --out-migration-rate 4 --stage draft
```

Runs the four checks in order: the share of the roll; the attrition a roll
accumulates on its own, `roll x (1 - (1 - r)^years)`, against which the
removals are an excess or a shortfall; whether the figure is a draft
(a ceiling) or final, with the restored share if you have both; and, given
an audited wrongful share, how many people who belonged on the roll were
removed.

No attrition rate is built in. Take the crude death rate from the Sample
Registration System bulletin for the state and year, and out-migration from
the Census D-series or the PLFS migration module, and pass them. The crude
death rate is a floor for an electoral roll, since every elector is an adult.

## poverty_lines.py

```bash
python tools/poverty_lines.py --year 2023
python tools/poverty_lines.py --check 1622 --line tendulkar_rural
python tools/poverty_lines.py --fetch
```

Puts ten lines in rupees per person per month at one price year: the six
World Bank lines (2017 and 2021 PPP vintages) and the four Indian committee
lines (Tendulkar and Rangarajan, rural and urban, 2011-12). The formula is
the World Bank's own: dollars per day, times the PPP conversion factor for
private consumption in the base year, times the CPI ratio to the target year,
times 30.4375. National lines are inflated by the CPI ratio alone.

`--check` takes a rupee figure and finds the price year at which the named
line comes closest, which is how the newsletter's Rs 1,622 turned out to be
the rural Tendulkar line at 2023 prices, not 2011-12 (see
`companions/errata.md`). `--fetch` pulls fresh PPP and CPI values from the
World Bank API and prints what changed; it does not write.

It is a reading aid, not a headcount. The Bank uses a survey-year CPI and a
rural/urban split, and the 2022-23 HCES changed the recall period, which is
the comparison the newsletter warns against.

## odds_likelihood.py

```bash
python tools/odds_likelihood.py odds 0.25
python tools/odds_likelihood.py table 75 25 50 50
python tools/odds_likelihood.py lik 7 20 --points 11
```

`odds` and `prob` convert. `table` takes a 2x2 (exposed with outcome,
exposed without, unexposed with, unexposed without) and prints relative risk
and odds ratio side by side with their ratio; at a 50 per cent baseline an OR
of 3 is an RR of 1.5, and the output says not to report it as "times as
likely". `lik` prints the binomial log-likelihood over a grid of p; it peaks
at k/n and does not sum to one, which is the point. There is no hypothesis
test here and none is planned.

## audits.py

```bash
python tools/audits.py recommendation --template > recs.json
python tools/audits.py recommendation recs.json
python tools/audits.py participation --template > design.json
python tools/audits.py participation design.json
```

Two checklists as JSON you fill in, and a check that exits 1 until every
question is answered, so it can gate a report.

The recommendation audit asks the April 2025 note's four questions of each
recommendation: which finding, what assumption connects it, what evidence
for the assumption, what would make it wrong. The participation audit asks
the June 2025 note's eight questions about where authority sits (research
question, evidence, budget, interpretation, dissent, data, publication,
afterwards), each answered `researchers`, `shared` or `participants`, and
names the arrangement in the June 2025 praxis note's terms: consultation,
collaboration or community control. None of the three is the correct model;
the check exists so the label on the proposal matches the design.

Worked examples are in `examples/`. The recommendations example has one
complete entry and one that fails on three questions, so you can see both.
