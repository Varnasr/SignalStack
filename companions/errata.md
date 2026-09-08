# Errata

Places where the newsletter's own text is known to be wrong, found while
building the archive and the tools. The archive is verbatim and is not
corrected; this page is where the correction lives.

## May 2026, Research praxis: the Tendulkar line's price year

The edition says India's Tendulkar poverty line "sits at roughly Rs 1,622
per person per month in rural areas at 2011-12 prices".

At 2011-12 prices the Tendulkar rural line is Rs 816 per person per month
(Planning Commission press note, 22 July 2013; urban Rs 1,000). Rs 816
inflated to 2023 prices by the World Bank's CPI series for India (FP.CPI.TOTL,
108.91 in 2011 to 216.86 in 2023) is Rs 1,625. So the figure is the rural
line at 2023 prices with the wrong year attached. The number is right; the
label is wrong.

`python tools/poverty_lines.py --check 1622 --line tendulkar_rural` shows
the calculation, and `tests/test_tools.py` asserts it.

## August 2025 edition: corrupted words in the published text

The edition as published on Substack contains several words damaged in
editing: "createifferently" (Research Praxis), "DVisualisationtion" and
"Rath-focused" (Tools and Tech), and "GLables aor ... ganisingransformed
hoorganisenise" (Research Resources and Tools). They are in the source HTML,
not introduced by the sync, and the archive reproduces them. Read past them.
