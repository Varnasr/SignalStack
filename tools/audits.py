"""Two checklists from the newsletter, as files you fill in and a check that reads them.

    python tools/audits.py recommendation --template > recs.json
    python tools/audits.py recommendation recs.json

    python tools/audits.py participation --template > design.json
    python tools/audits.py participation design.json

Recommendation audit (Research praxis, April 2025). "A finding is not an
inference. An inference is not a recommendation." For each recommendation in
an evaluation report, four questions:

1. Which finding supports this?
2. What causal or institutional assumption connects the finding to the
   recommendation?
3. What evidence supports that assumption?
4. What would make the recommendation wrong?

The check reads a JSON list of recommendations and reports which of the four
each one leaves blank. An unanswered fourth question is the usual finding.

Participation audit (methods note, June 2025). "Participation is a design
property, not a label." Eight questions about where authority sits:

1. Who chose the research question?
2. Who decided what counted as evidence?
3. Who controlled the budget?
4. Who interpreted the findings?
5. Who could disagree with the researchers?
6. Who owns the data?
7. Who decides where and how the work is published?
8. What happens after the project ends?

Each is answered with `held_by`: "researchers", "shared" or "participants",
plus a note. From the answers the check names the arrangement in the terms
the June 2025 praxis note uses: consultation (researchers hold every
decision), collaboration (some are shared or held by participants) or
community control (participants hold most, including the question and the
interpretation). None of the three is the correct model; the check exists so
the label on the proposal matches the design.

Exit status is 1 when anything is missing, so the check can gate a report.
"""

from __future__ import annotations

import argparse
import json
import sys

RECOMMENDATION_QUESTIONS = {
    "finding": "Which finding supports this?",
    "assumption": "What causal or institutional assumption connects the finding to the recommendation?",
    "evidence_for_assumption": "What evidence supports that assumption?",
    "what_would_make_it_wrong": "What would make the recommendation wrong?",
}

PARTICIPATION_QUESTIONS = {
    "research_question": "Who chose the research question?",
    "what_counts_as_evidence": "Who decided what counted as evidence?",
    "budget": "Who controlled the budget?",
    "interpretation": "Who interpreted the findings?",
    "dissent": "Who could disagree with the researchers?",
    "data_ownership": "Who owns the data?",
    "publication": "Who decides where and how the work is published?",
    "after_the_project": "What happens after the project ends?",
}

HOLDERS = ("researchers", "shared", "participants")


def recommendation_template() -> list[dict]:
    return [{"recommendation": "", **{k: "" for k in RECOMMENDATION_QUESTIONS}}]


def participation_template() -> dict:
    return {"project": "",
            "questions": {k: {"held_by": "", "note": ""} for k in PARTICIPATION_QUESTIONS}}


def _blank(v) -> bool:
    return v is None or (isinstance(v, str) and not v.strip())


def check_recommendations(recs: list[dict]) -> list[dict]:
    """For each recommendation, the questions left unanswered."""
    if not isinstance(recs, list):
        raise ValueError("expected a JSON list of recommendations")
    out = []
    for i, r in enumerate(recs, 1):
        missing = [k for k in RECOMMENDATION_QUESTIONS if _blank(r.get(k))]
        out.append({"n": i, "recommendation": (r.get("recommendation") or "").strip() or f"(untitled #{i})",
                    "missing": missing, "complete": not missing})
    return out


def classify_participation(answers: dict) -> str:
    held = {k: (answers.get(k) or {}).get("held_by") for k in PARTICIPATION_QUESTIONS}
    by_participants = [k for k, v in held.items() if v == "participants"]
    shared = [k for k, v in held.items() if v == "shared"]
    if not by_participants and not shared:
        return "consultation"
    core = {"research_question", "interpretation"}
    if len(by_participants) >= len(PARTICIPATION_QUESTIONS) / 2 and core <= set(by_participants):
        return "community control"
    return "collaboration"


def check_participation(design: dict) -> dict:
    if not isinstance(design, dict) or not isinstance(design.get("questions"), dict):
        raise ValueError("expected an object with a 'questions' map")
    q = design["questions"]
    missing, invalid = [], []
    for k in PARTICIPATION_QUESTIONS:
        a = q.get(k) or {}
        if _blank(a.get("held_by")):
            missing.append(k)
        elif a.get("held_by") not in HOLDERS:
            invalid.append(k)
    arrangement = None if (missing or invalid) else classify_participation(q)
    return {"project": design.get("project") or "(unnamed project)",
            "missing": missing, "invalid": invalid, "arrangement": arrangement,
            "complete": not missing and not invalid}


def report_recommendations(rows: list[dict]) -> str:
    lines = []
    for r in rows:
        if r["complete"]:
            lines.append(f"{r['n']}. {r['recommendation']}: all four questions answered.")
        else:
            lines.append(f"{r['n']}. {r['recommendation']}: unanswered:")
            for k in r["missing"]:
                lines.append(f"     - {RECOMMENDATION_QUESTIONS[k]}")
    n_bad = sum(not r["complete"] for r in rows)
    lines.append(f"{len(rows)} recommendation(s), {n_bad} with gaps.")
    return "\n".join(lines)


def report_participation(res: dict) -> str:
    lines = [f"{res['project']}"]
    for k in res["missing"]:
        lines.append(f"  unanswered: {PARTICIPATION_QUESTIONS[k]}")
    for k in res["invalid"]:
        lines.append(f"  held_by must be one of {HOLDERS}: {PARTICIPATION_QUESTIONS[k]}")
    if res["arrangement"]:
        lines.append(f"  arrangement: {res['arrangement']}")
        lines.append("  None of the three is the correct model. Say which one this is, in the proposal, "
                     "and where the design falls short of the label.")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("kind", choices=["recommendation", "participation"])
    ap.add_argument("file", nargs="?", help="JSON file to check")
    ap.add_argument("--template", action="store_true", help="print a blank file to fill in")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    a = ap.parse_args(argv)
    if a.template:
        tpl = recommendation_template() if a.kind == "recommendation" else participation_template()
        print(json.dumps(tpl, indent=2))
        return 0
    if not a.file:
        ap.error("give a JSON file to check, or --template")
    with open(a.file, encoding="utf-8") as fh:
        data = json.load(fh)
    if a.kind == "recommendation":
        rows = check_recommendations(data)
        print(json.dumps(rows, indent=2) if a.json else report_recommendations(rows))
        return 0 if all(r["complete"] for r in rows) else 1
    res = check_participation(data)
    print(json.dumps(res, indent=2) if a.json else report_participation(res))
    return 0 if res["complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
