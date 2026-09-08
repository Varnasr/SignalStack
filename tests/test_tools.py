"""Plain-assert tests for tools/ and scripts/. Run: python -m pytest tests/

Every expectation is a closed-form identity or a figure from a cited source,
never a previous run's output.
"""

import json
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools import audits, deletion_rate, odds_likelihood, poverty_lines  # noqa: E402


# ---------------------------------------------------------------- deletion_rate

def test_bihar_share_matches_the_newsletter():
    # July 2026: "Forty-seven lakh against Bihar's 7.89 crore roll is 5.95 per cent."
    assert abs(deletion_rate.share(47e5, 7.89e7) * 100 - 5.957) < 0.01


def test_attrition_compounds_rather_than_multiplies():
    roll = 1_000_000
    one = deletion_rate.expected_attrition(roll, 0.01, 1)
    twenty = deletion_rate.expected_attrition(roll, 0.01, 20)
    assert abs(one - 10_000) < 1e-6
    assert twenty < 200_000                      # not 20 x 10,000
    assert abs(twenty - roll * (1 - 0.99 ** 20)) < 1e-6


def test_draft_is_a_ceiling_and_restoration_is_reported():
    r = deletion_rate.read(1000, 100_000, stage="draft", final_removed=700)
    assert r["ceiling"] is True
    assert abs(r["restored_share"] - 0.3) < 1e-12
    assert abs(r["final_share"] - 0.007) < 1e-12


def test_wrongful_share_uses_final_removals_when_given():
    r = deletion_rate.read(1000, 100_000, stage="draft", final_removed=700, wrongful_share=0.1)
    assert abs(r["wrongful_removals"] - 70) < 1e-9


def test_excess_sign_is_right():
    r = deletion_rate.read(60_000, 1_000_000, years=5, death_rate=6.0, out_migration_rate=4.0)
    expected = 1_000_000 * (1 - 0.99 ** 5)
    assert abs(r["baseline"]["expected_removals"] - expected) < 1e-6
    assert r["baseline"]["excess"] > 0
    assert "exceed" in deletion_rate.report(r)


def test_bad_inputs_are_refused():
    for bad in ((-1, 10), (5, 0)):
        try:
            deletion_rate.share(*bad)
        except ValueError:
            continue
        raise AssertionError(bad)


# ---------------------------------------------------------------- odds_likelihood

def test_odds_and_probability_round_trip():
    assert abs(odds_likelihood.odds(0.25) - 1 / 3) < 1e-12
    assert abs(odds_likelihood.prob(3) - 0.75) < 1e-12
    for p in (0.0, 0.1, 0.5, 0.9):
        assert abs(odds_likelihood.prob(odds_likelihood.odds(p)) - p) < 1e-12
    assert math.isinf(odds_likelihood.odds(1.0))


def test_or_equals_rr_only_when_the_outcome_is_rare():
    rare = odds_likelihood.two_by_two(2, 998, 1, 999)
    common = odds_likelihood.two_by_two(75, 25, 50, 50)
    assert abs(rare["or_over_rr"] - 1) < 0.01
    assert abs(common["relative_risk"] - 1.5) < 1e-12
    assert abs(common["odds_ratio"] - 3.0) < 1e-12        # OR 3, RR 1.5: the June 2024 point
    assert common["or_over_rr"] > 1.5


def test_likelihood_is_maximised_at_k_over_n_and_is_not_a_density():
    k, n = 7, 20
    grid = odds_likelihood.likelihood_grid(k, n, 201)
    best_p = max(grid, key=lambda t: t[1])[0]
    assert abs(best_p - odds_likelihood.mle(k, n)) < 0.01
    assert odds_likelihood.binomial_loglik(k, n, 0.0) == -math.inf
    total = sum(math.exp(ll) for _, ll in grid if ll > -math.inf)
    assert abs(total - 1) > 0.5                         # L(p) does not integrate to one over p


def test_loglik_matches_closed_form():
    ll = odds_likelihood.binomial_loglik(3, 5, 0.4)
    expect = math.log(math.comb(5, 3) * 0.4 ** 3 * 0.6 ** 2)
    assert abs(ll - expect) < 1e-12


# ---------------------------------------------------------------- audits

def test_recommendation_template_round_trips_and_is_incomplete():
    tpl = audits.recommendation_template()
    rows = audits.check_recommendations(json.loads(json.dumps(tpl)))
    assert rows[0]["missing"] == list(audits.RECOMMENDATION_QUESTIONS)
    assert not rows[0]["complete"]


def test_example_recommendations_name_the_missing_questions():
    data = json.loads((ROOT / "tools/examples/recommendations.json").read_text())
    rows = audits.check_recommendations(data)
    assert rows[0]["complete"]
    assert rows[1]["missing"] == ["assumption", "evidence_for_assumption", "what_would_make_it_wrong"]


def test_participation_classification():
    q = {k: {"held_by": "researchers"} for k in audits.PARTICIPATION_QUESTIONS}
    assert audits.classify_participation(q) == "consultation"
    q["dissent"] = {"held_by": "shared"}
    assert audits.classify_participation(q) == "collaboration"
    for k in ("research_question", "interpretation", "budget", "data_ownership"):
        q[k] = {"held_by": "participants"}
    assert audits.classify_participation(q) == "community control"
    q["research_question"] = {"held_by": "shared"}        # majority without the question is not control
    assert audits.classify_participation(q) == "collaboration"


def test_participation_example_is_collaboration_and_bad_holder_is_reported():
    data = json.loads((ROOT / "tools/examples/participation.json").read_text())
    res = audits.check_participation(data)
    assert res["complete"] and res["arrangement"] == "collaboration"
    data["questions"]["budget"]["held_by"] = "donor"
    res = audits.check_participation(data)
    assert res["invalid"] == ["budget"] and res["arrangement"] is None


def test_cli_exit_status_gates_a_report():
    r = subprocess.run([sys.executable, "tools/audits.py", "recommendation",
                        "tools/examples/recommendations.json"], cwd=ROOT, capture_output=True)
    assert r.returncode == 1


# ---------------------------------------------------------------- poverty_lines

def test_official_lines_are_the_published_figures():
    nat = poverty_lines.DATA["national"]
    assert nat["tendulkar_rural"] == (816, 2011) and nat["tendulkar_urban"] == (1000, 2011)
    assert nat["rangarajan_rural"] == (972, 2011) and nat["rangarajan_urban"] == (1407, 2011)
    intl = poverty_lines.DATA["international"]
    assert intl["wb_2017_extreme"] == (2.15, 2017) and intl["wb_2021_extreme"] == (3.00, 2021)


def test_inflation_is_a_cpi_ratio_and_identity_at_same_year():
    cpi = poverty_lines.DATA["cpi"]
    assert poverty_lines.inflate(816, 2011, 2011) == 816
    assert abs(poverty_lines.inflate(816, 2011, 2023) - 816 * cpi[2023] / cpi[2011]) < 1e-9


def test_ppp_conversion_is_the_stated_formula():
    ppp, cpi = poverty_lines.DATA["ppp"], poverty_lines.DATA["cpi"]
    got = poverty_lines.daily_ppp_to_monthly_inr(2.15, 2017, 2023)
    want = 2.15 * ppp[2017] * cpi[2023] / cpi[2017] * 365.25 / 12
    assert abs(got - want) < 1e-9
    assert abs(poverty_lines.daily_inr("wb_2017_extreme", 2023) * 365.25 / 12 - got) < 1e-9


def test_the_newsletters_1622_is_the_rural_tendulkar_line_at_2023_prices():
    year, value = poverty_lines.find_price_year(1622, "tendulkar_rural")
    assert year == 2023
    assert abs(value - 1622) < 10
    assert poverty_lines.monthly_inr("tendulkar_rural", 2011) == 816


def test_table_is_sorted_and_covers_every_line():
    rows = poverty_lines.table(2024)
    assert len(rows) == len(poverty_lines.LABELS)
    assert [r[1] for r in rows] == sorted(r[1] for r in rows)


# ---------------------------------------------------------------- scripts

def test_markdown_converter_handles_void_tags_and_blockquotes():
    sys.path.insert(0, str(ROOT / "scripts"))
    from sync_substack import to_markdown
    md = to_markdown('<ul><li><p>one <img src="x.png" alt="a"></p></li><li><p>two</p></li></ul>'
                     '<p>after</p><p>more</p><blockquote><p>q1</p><p>q2</p></blockquote>')
    assert "\n\nafter\n\nmore\n\n" in md            # paragraphs after a list stay separate
    assert "> q1\n>\n> q2" in md


def test_companions_are_in_step_with_the_archive():
    r = subprocess.run([sys.executable, "scripts/build_companions.py", "--check"],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_every_companion_entry_links_back_to_an_edition():
    import re
    for f in (ROOT / "companions").glob("*.md"):
        if f.name in ("README.md", "errata.md"):
            continue
        text = f.read_text(encoding="utf-8")
        heads = len(re.findall(r"(?m)^## ", text))
        links = len(re.findall(r"\]\(\.\./archive/2", text))
        assert heads > 0, f.name
        assert links >= heads, f"{f.name}: {heads} entries, {links} source links"
        for target in re.findall(r"\]\(\.\./archive/([^)#]+)", text):
            assert (ROOT / "archive" / target).exists(), target
