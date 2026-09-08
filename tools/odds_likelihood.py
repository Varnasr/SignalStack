"""Odds, probability, odds ratios, relative risk and likelihood, kept apart.

    python tools/odds_likelihood.py odds 0.25          # probability -> odds
    python tools/odds_likelihood.py prob 3             # odds -> probability
    python tools/odds_likelihood.py table 30 70 10 90  # 2x2: a b c d
    python tools/odds_likelihood.py lik 7 20           # binomial likelihood of p

The June 2024 methods corner: "Odds compare the probability of an event
occurring with the probability of it not occurring. Likelihood is a function
used in statistical estimation. They sound similar. They do different jobs."

Three confusions this module is built to make visible.

Odds are not probabilities. p = 0.25 is odds of 1 to 3, and odds of 3 is
p = 0.75. Reporting an odds ratio of 2 as "twice as likely" is wrong unless
the outcome is rare.

An odds ratio is not a relative risk. From a 2x2 table (exposed/unexposed by
outcome/no outcome) both are computed and the gap between them is shown.
They agree when the outcome is rare and diverge as it becomes common; with a
50 per cent baseline an OR of 3 is an RR of 1.5.

Likelihood is a function of the parameter, not a probability of the data.
`binomial_loglik` returns log L(p | k, n) on a grid; it is maximised at k/n
and does not integrate to one over p. Nothing here is a hypothesis test.
"""

from __future__ import annotations

import argparse
import math
import sys


def odds(p: float) -> float:
    """p / (1 - p). Infinite at p = 1."""
    if not 0 <= p <= 1:
        raise ValueError("probability must lie in [0, 1]")
    return math.inf if p == 1 else p / (1 - p)


def prob(o: float) -> float:
    """Odds back to probability: o / (1 + o)."""
    if o < 0:
        raise ValueError("odds must not be negative")
    return 1.0 if math.isinf(o) else o / (1 + o)


def two_by_two(a: int, b: int, c: int, d: int) -> dict:
    """a = exposed with outcome, b = exposed without, c = unexposed with,
    d = unexposed without. Returns risks, odds, RR, OR and their ratio."""
    for x in (a, b, c, d):
        if x < 0:
            raise ValueError("cell counts must not be negative")
    if a + b == 0 or c + d == 0:
        raise ValueError("each exposure row needs at least one observation")
    risk_e, risk_u = a / (a + b), c / (c + d)
    rr = math.inf if risk_u == 0 else risk_e / risk_u
    if b == 0 or c == 0:
        or_ = math.inf if a * d > 0 else math.nan
    else:
        or_ = (a * d) / (b * c)
    return {
        "risk_exposed": risk_e, "risk_unexposed": risk_u,
        "odds_exposed": odds(risk_e), "odds_unexposed": odds(risk_u),
        "relative_risk": rr, "odds_ratio": or_,
        "or_over_rr": (or_ / rr) if rr not in (0, math.inf) and not math.isinf(or_) else math.nan,
        "baseline_risk": risk_u,
    }


def binomial_loglik(k: int, n: int, p: float) -> float:
    """log L(p | k successes in n). -inf where the data are impossible."""
    if not 0 <= k <= n:
        raise ValueError("need 0 <= k <= n")
    if not 0 <= p <= 1:
        raise ValueError("p must lie in [0, 1]")
    if (p == 0 and k > 0) or (p == 1 and k < n):
        return -math.inf
    ll = math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
    if k > 0:
        ll += k * math.log(p)
    if n - k > 0:
        ll += (n - k) * math.log(1 - p)
    return ll


def likelihood_grid(k: int, n: int, points: int = 101) -> list[tuple[float, float]]:
    """(p, log-likelihood) on an even grid over [0, 1]."""
    return [(i / (points - 1), binomial_loglik(k, n, i / (points - 1))) for i in range(points)]


def mle(k: int, n: int) -> float:
    """The maximum-likelihood estimate of p is k / n in closed form."""
    if n <= 0:
        raise ValueError("n must be positive")
    return k / n


def report_table(t: dict) -> str:
    lines = [
        f"risk, exposed      {t['risk_exposed']:.4f}   odds {t['odds_exposed']:.4f}",
        f"risk, unexposed    {t['risk_unexposed']:.4f}   odds {t['odds_unexposed']:.4f}",
        f"relative risk      {t['relative_risk']:.4f}",
        f"odds ratio         {t['odds_ratio']:.4f}",
    ]
    if not math.isnan(t["or_over_rr"]):
        lines.append(f"OR / RR            {t['or_over_rr']:.4f}   "
                     f"(baseline risk {t['baseline_risk'] * 100:.1f} per cent; "
                     + ("close enough to read the OR as a risk ratio"
                        if abs(t["or_over_rr"] - 1) < 0.1 else
                        "the OR overstates the risk ratio; do not report it as 'times as likely'") + ")")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("odds", help="probability to odds"); s.add_argument("p", type=float)
    s = sub.add_parser("prob", help="odds to probability"); s.add_argument("o", type=float)
    s = sub.add_parser("table", help="2x2 table: a b c d")
    for name in "abcd":
        s.add_argument(name, type=int)
    s = sub.add_parser("lik", help="binomial log-likelihood of p given k of n")
    s.add_argument("k", type=int); s.add_argument("n", type=int)
    s.add_argument("--points", type=int, default=11)
    a = ap.parse_args(argv)
    if a.cmd == "odds":
        print(f"p = {a.p:g}  ->  odds = {odds(a.p):g}  ({a.p:g} to {1 - a.p:g})")
    elif a.cmd == "prob":
        print(f"odds = {a.o:g}  ->  p = {prob(a.o):.4f}")
    elif a.cmd == "table":
        print(report_table(two_by_two(a.a, a.b, a.c, a.d)))
    elif a.cmd == "lik":
        print(f"MLE p = {mle(a.k, a.n):.4f}  (k/n, closed form)")
        for p, ll in likelihood_grid(a.k, a.n, a.points):
            print(f"p = {p:.2f}   log L = {ll:9.3f}")
        print("log L is a function of p given the data; it is not a probability of p "
              "and does not sum to one across this grid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
