"""Put poverty lines on one footing: rupees per person per month at a stated price year.

    python tools/poverty_lines.py                     # the table, at the latest CPI year
    python tools/poverty_lines.py --year 2023         # at 2023 prices
    python tools/poverty_lines.py --check 1622 --line tendulkar_rural
    python tools/poverty_lines.py --fetch             # refresh PPP and CPI from the World Bank API

The May 2026 praxis note ("What a poverty line actually is") makes the
point that the line is a choice, that the international dollar lines and
India's committee lines are expressed in different units, and that the
reference period and price year are where comparisons go wrong. This script
converts every line to the same unit so the choice is visible.

Units. A World Bank line is international dollars per person per day at a
PPP base year (2017 for $2.15, 2021 for $3.00). To express it in rupees for
a given year: multiply by the PPP conversion factor for private consumption
in the base year (LCU per international $), then by the CPI ratio between
the base year and the target year, then by days per month (365.25 / 12).
India's committee lines are rupees per person per month at 2011-12 prices;
those are inflated by the CPI ratio alone.

    monthly INR (year t) = line_per_day x PPP(base) x CPI(t) / CPI(base) x 30.4375

This is the arithmetic the World Bank's own conversion performs. It is not
the whole story: the Bank uses a survey-year CPI and, for India, a rural /
urban split and the 2022-23 HCES with its changed recall period, which is the
MMRP break the newsletter warns about. The numbers here are for reading a
table, not for reproducing a headcount.

Sources, each read into DATA and not restated anywhere else:
- International lines: World Bank, "Global poverty lines updated" (2017 PPP
  lines of $2.15 / $3.65 / $6.85, September 2022) and the June 2025 update to
  2021 PPPs ($3.00 / $4.20 / $8.30).
- Tendulkar 2011-12: Planning Commission press note of 22 July 2013, Rs 816
  rural and Rs 1,000 urban per capita per month.
- Rangarajan 2011-12: Report of the Expert Group to Review the Methodology
  for Measurement of Poverty, June 2014, Rs 972 rural and Rs 1,407 urban.
- PPP factor and CPI: World Bank indicators PA.NUS.PRVT.PP and FP.CPI.TOTL
  (2010 = 100) for India, fetched 2026-09-08 from a series last updated
  2026-07-13. `--fetch` refreshes both and prints what changed.

One consequence worth knowing. The May 2026 edition gives the Tendulkar rural
line as "roughly Rs 1,622 per person per month ... at 2011-12 prices". At
2011-12 prices it is Rs 816. Rs 816 inflated to 2023 prices by this CPI
series is Rs 1,625, so the newsletter's number is the line at 2023 prices
with the wrong year attached. `--check 1622 --line tendulkar_rural` finds
that price year.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request

DAYS_PER_MONTH = 365.25 / 12

DATA = {
    "international": {
        # name: (dollars per day, PPP base year)
        "wb_2017_extreme": (2.15, 2017),
        "wb_2017_lmic": (3.65, 2017),
        "wb_2017_umic": (6.85, 2017),
        "wb_2021_extreme": (3.00, 2021),
        "wb_2021_lmic": (4.20, 2021),
        "wb_2021_umic": (8.30, 2021),
    },
    "national": {
        # name: (rupees per person per month, price year)
        "tendulkar_rural": (816, 2011),
        "tendulkar_urban": (1000, 2011),
        "rangarajan_rural": (972, 2011),
        "rangarajan_urban": (1407, 2011),
    },
    # World Bank PA.NUS.PRVT.PP, India, LCU per international $
    "ppp": {2011: 15.2829, 2012: 15.5332, 2013: 17.1338, 2014: 18.0977, 2015: 18.8498,
            2016: 19.4344, 2017: 20.1501, 2018: 19.8211, 2019: 19.5281, 2020: 19.7747,
            2021: 19.469, 2022: 19.2339, 2023: 19.5171, 2024: 19.8969, 2025: 19.8389},
    # World Bank FP.CPI.TOTL, India, 2010 = 100
    "cpi": {2011: 108.9118, 2012: 119.2355, 2013: 131.1804, 2014: 139.9244, 2015: 146.7905,
            2016: 154.054, 2017: 159.1812, 2018: 165.4511, 2019: 171.6216, 2020: 182.9888,
            2021: 192.3787, 2022: 205.2662, 2023: 216.862, 2024: 227.6033, 2025: 233.0631},
    "fetched": "2026-09-08", "series_updated": "2026-07-13",
}

LABELS = {
    "wb_2017_extreme": "World Bank $2.15 (2017 PPP)", "wb_2017_lmic": "World Bank $3.65 (2017 PPP)",
    "wb_2017_umic": "World Bank $6.85 (2017 PPP)", "wb_2021_extreme": "World Bank $3.00 (2021 PPP)",
    "wb_2021_lmic": "World Bank $4.20 (2021 PPP)", "wb_2021_umic": "World Bank $8.30 (2021 PPP)",
    "tendulkar_rural": "Tendulkar rural, 2011-12", "tendulkar_urban": "Tendulkar urban, 2011-12",
    "rangarajan_rural": "Rangarajan rural, 2011-12", "rangarajan_urban": "Rangarajan urban, 2011-12",
}


def inflate(amount: float, year_from: int, year_to: int, cpi: dict | None = None) -> float:
    """Move a rupee amount between price years by the CPI ratio."""
    cpi = cpi or DATA["cpi"]
    if year_from not in cpi or year_to not in cpi:
        raise KeyError(f"CPI covers {min(cpi)}-{max(cpi)}")
    return amount * cpi[year_to] / cpi[year_from]


def daily_ppp_to_monthly_inr(line: float, base_year: int, year: int, *,
                             ppp: dict | None = None, cpi: dict | None = None) -> float:
    """International dollars per day at `base_year` PPPs to rupees per month at `year` prices."""
    ppp = ppp or DATA["ppp"]
    if base_year not in ppp:
        raise KeyError(f"no PPP factor for {base_year}")
    return inflate(line * ppp[base_year] * DAYS_PER_MONTH, base_year, year, cpi)


def monthly_inr(name: str, year: int) -> float:
    """Any named line, in rupees per person per month at `year` prices."""
    if name in DATA["international"]:
        line, base = DATA["international"][name]
        return daily_ppp_to_monthly_inr(line, base, year)
    if name in DATA["national"]:
        amt, base = DATA["national"][name]
        return inflate(amt, base, year)
    raise KeyError(name)


def daily_inr(name: str, year: int) -> float:
    return monthly_inr(name, year) / DAYS_PER_MONTH


def table(year: int) -> list[tuple[str, float, float]]:
    rows = [(LABELS[n], monthly_inr(n, year), daily_inr(n, year))
            for n in list(DATA["international"]) + list(DATA["national"])]
    return sorted(rows, key=lambda r: r[1])


def find_price_year(claimed: float, name: str) -> tuple[int, float]:
    """The CPI year at which `name` comes closest to `claimed` rupees per month."""
    best = min(DATA["cpi"], key=lambda y: abs(monthly_inr(name, y) - claimed))
    return best, monthly_inr(name, best)


def fetch(country: str = "IND") -> dict:
    """Refresh PPP and CPI from the World Bank API. Returns {'ppp': {...}, 'cpi': {...}}."""
    out = {}
    for key, ind in (("ppp", "PA.NUS.PRVT.PP"), ("cpi", "FP.CPI.TOTL")):
        url = (f"https://api.worldbank.org/v2/country/{country}/indicator/{ind}"
               f"?format=json&per_page=100&date=2011:2035")
        with urllib.request.urlopen(url, timeout=30) as r:
            meta, rows = json.load(r)
        out[key] = {int(x["date"]): round(x["value"], 4) for x in rows if x["value"] is not None}
        out[f"{key}_updated"] = meta.get("lastupdated")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--year", type=int, default=max(DATA["cpi"]), help="price year for the table")
    ap.add_argument("--check", type=float, help="a rupees-per-month figure to place against a line")
    ap.add_argument("--line", default="tendulkar_rural", choices=sorted(LABELS),
                    help="which line --check refers to")
    ap.add_argument("--fetch", action="store_true", help="refresh PPP and CPI from the World Bank API")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    if a.fetch:
        new = fetch()
        changed = {k: {y: (DATA[k].get(y), v) for y, v in new[k].items() if DATA[k].get(y) != v}
                   for k in ("ppp", "cpi")}
        print(json.dumps({"changed": changed, "ppp_updated": new["ppp_updated"],
                          "cpi_updated": new["cpi_updated"]}, indent=2))
        print("Paste the new values into DATA and update the 'fetched' date.")
        return 0

    if a.check is not None:
        year, value = find_price_year(a.check, a.line)
        base = DATA["national"].get(a.line, DATA["international"].get(a.line))[1]
        print(f"{LABELS[a.line]} is Rs {monthly_inr(a.line, base):,.0f} per month at {base} prices.")
        print(f"Rs {a.check:,.0f} is closest to that line at {year} prices (Rs {value:,.0f}).")
        return 0

    rows = table(a.year)
    if a.json:
        print(json.dumps([{"line": n, "inr_per_month": m, "inr_per_day": d} for n, m, d in rows], indent=2))
        return 0
    print(f"Rupees per person, at {a.year} prices (CPI series updated {DATA['series_updated']})")
    print(f"{'line':34} {'per month':>10} {'per day':>8}")
    for n, m, d in rows:
        print(f"{n:34} {m:10,.0f} {d:8,.0f}")
    print("International lines: dollars/day x PPP(base year) x CPI ratio x 30.4375. "
          "National lines: 2011-12 rupees x CPI ratio. Reading only; not a headcount.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
