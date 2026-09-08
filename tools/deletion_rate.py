"""Read an electoral-roll deletion figure the way the July 2026 praxis note says to.

    python tools/deletion_rate.py --removed 4700000 --roll 78900000 \
        --years 22 --death-rate 6.4 --out-migration-rate 4 --stage draft

The note ("How to read a deletion rate", Research Rundown, July 2026) gives
four checks to run before reacting to a headline like "47 lakh electors
removed". This script runs them and prints what each one says.

1. Denominator.  Removals as a share of the roll. 47 lakh of 7.89 crore is
   5.96 per cent; the absolute figure is built to alarm, the ratio is what
   you reason with.
2. Baseline.     Rolls decay on their own through death and out-migration.
   Given a per-year attrition rate and the years since the roll was last
   revised, the expected clean-up is  roll x (1 - (1 - r)^years).  The
   question is whether removals exceed that, not whether they are large.
3. Draft or final.  A draft-roll deletion is a ceiling: names can be
   restored during the claims window. If you have both figures the restored
   share is reported; if you only have the draft, the script says so.
4. Error borne by whom.  Every verification trades wrongful removals against
   wrongful retentions. If an audit sample gives the share of removals that
   were wrongful, the script turns it into a count of people; if not, it
   prints the question you still have to answer.

No parameter has a hidden default. The attrition inputs are yours to source:
the crude death rate from the Registrar General's Sample Registration System
bulletin for the state and year, and an out-migration rate from the Census
D-series or the PLFS migration module. The crude death rate is a floor for an
electoral roll, because every elector is an adult and adults die at a higher
rate than the population as a whole.
"""

from __future__ import annotations

import argparse
import json
import sys


def share(removed: float, roll: float) -> float:
    """Removals as a fraction of the roll. Raises if the roll is not positive."""
    if roll <= 0:
        raise ValueError("roll must be positive")
    if removed < 0:
        raise ValueError("removed must not be negative")
    return removed / roll


def expected_attrition(roll: float, per_year_rate: float, years: float) -> float:
    """Names a roll would lose to death and out-migration on its own.

    `per_year_rate` is a fraction (0.0104 for 10.4 per thousand). The formula
    compounds, so a roll left for twenty years does not lose twenty times the
    annual rate: it loses 1 - (1 - r)^20 of itself.
    """
    if not 0 <= per_year_rate < 1:
        raise ValueError("per_year_rate must be a fraction in [0, 1)")
    if years < 0:
        raise ValueError("years must not be negative")
    return roll * (1 - (1 - per_year_rate) ** years)


def restored_share(draft_removed: float, final_removed: float) -> float:
    """Share of draft removals reversed by the time the roll was finalised."""
    if draft_removed <= 0:
        raise ValueError("draft_removed must be positive")
    if final_removed < 0 or final_removed > draft_removed:
        raise ValueError("final_removed must lie between 0 and draft_removed")
    return 1 - final_removed / draft_removed


def read(removed: float, roll: float, *, years: float | None = None,
         death_rate: float | None = None, out_migration_rate: float | None = None,
         stage: str = "unknown", final_removed: float | None = None,
         wrongful_share: float | None = None) -> dict:
    """Run the four checks. Rates are per thousand per year, as published."""
    out: dict = {"removed": removed, "roll": roll, "share": share(removed, roll)}

    if years is not None and death_rate is not None:
        r = (death_rate + (out_migration_rate or 0.0)) / 1000
        exp = expected_attrition(roll, r, years)
        out["baseline"] = {
            "per_year_rate": r, "years": years,
            "expected_removals": exp, "expected_share": exp / roll,
            "excess": removed - exp, "excess_share": (removed - exp) / roll,
        }

    out["stage"] = stage
    if stage == "draft":
        out["ceiling"] = True
        if final_removed is not None:
            out["restored_share"] = restored_share(removed, final_removed)
            out["final_share"] = share(final_removed, roll)

    if wrongful_share is not None:
        if not 0 <= wrongful_share <= 1:
            raise ValueError("wrongful_share must be a fraction in [0, 1]")
        base = final_removed if final_removed is not None else removed
        out["wrongful_removals"] = base * wrongful_share
    return out


def lakh_crore(n: float) -> str:
    if n >= 1e7:
        return f"{n / 1e7:.2f} crore"
    if n >= 1e5:
        return f"{n / 1e5:.1f} lakh"
    return f"{n:,.0f}"


def report(res: dict) -> str:
    lines = []
    lines.append(f"1. Denominator: {lakh_crore(res['removed'])} removed from a roll of "
                 f"{lakh_crore(res['roll'])} is {res['share'] * 100:.2f} per cent.")
    b = res.get("baseline")
    if b:
        lines.append(f"2. Baseline: at {b['per_year_rate'] * 1000:.1f} per thousand a year for "
                     f"{b['years']:g} years, the roll would have lost about "
                     f"{lakh_crore(b['expected_removals'])} ({b['expected_share'] * 100:.1f} per cent) on its own.")
        if b["excess"] > 0:
            lines.append(f"   Removals exceed that by {lakh_crore(b['excess'])} "
                         f"({b['excess_share'] * 100:.1f} points). That excess is the number to explain.")
        else:
            lines.append(f"   Removals fall short of that by {lakh_crore(-b['excess'])}; "
                         "the revision has not even caught up with ordinary churn.")
        lines.append("   The crude death rate is a floor for an electoral roll: every elector is an "
                     "adult, and adults die at a higher rate than the population as a whole.")
    else:
        lines.append("2. Baseline: not computed. Pass --years and --death-rate (and --out-migration-rate) "
                     "to compare removals against the churn a roll accumulates on its own.")
    if res["stage"] == "draft":
        if "restored_share" in res:
            lines.append(f"3. Draft or final: {res['restored_share'] * 100:.1f} per cent of draft removals "
                         f"were restored; the final rate is {res['final_share'] * 100:.2f} per cent.")
        else:
            lines.append("3. Draft or final: this is a DRAFT figure, so it is a ceiling, not a verdict. "
                         "Names can be restored during the claims window. Do not quote it as final.")
    elif res["stage"] == "final":
        lines.append("3. Draft or final: final roll. Compare against the draft to see how much the "
                     "claims window corrected.")
    else:
        lines.append("3. Draft or final: stage not given. Find out; a draft number is routinely "
                     "quoted as if it were the outcome.")
    if "wrongful_removals" in res:
        lines.append(f"4. Error borne by whom: at the audited wrongful share, about "
                     f"{lakh_crore(res['wrongful_removals'])} people who belonged on the roll were removed. "
                     "Each of them must now prove their claim to the state.")
    else:
        lines.append("4. Error borne by whom: unknown. Every verification trades wrongful removals against "
                     "wrongful retentions; ask who has to prove what, and what an audit sample shows.")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--removed", type=float, required=True, help="names removed")
    ap.add_argument("--roll", type=float, required=True, help="size of the roll before removals")
    ap.add_argument("--years", type=float, help="years since the roll was last intensively revised")
    ap.add_argument("--death-rate", type=float, help="crude death rate, per thousand per year (SRS)")
    ap.add_argument("--out-migration-rate", type=float, default=0.0,
                    help="out-migration, per thousand per year (Census D-series / PLFS)")
    ap.add_argument("--stage", choices=["draft", "final", "unknown"], default="unknown")
    ap.add_argument("--final-removed", type=float, help="removals on the final roll, if --stage draft")
    ap.add_argument("--wrongful-share", type=float,
                    help="share of removals found wrongful in an audit sample, as a fraction")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    a = ap.parse_args(argv)
    res = read(a.removed, a.roll, years=a.years, death_rate=a.death_rate,
               out_migration_rate=a.out_migration_rate, stage=a.stage,
               final_removed=a.final_removed, wrongful_share=a.wrongful_share)
    print(json.dumps(res, indent=2) if a.json else report(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
