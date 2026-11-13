"""Descriptive checks named in PREREG.md: rates by attribute type and by source order.

For the baseline conditions C1 and C12 and the forgery conditions C13 and C15, per model and
split: the false-follow rate for each attribute type, and for items where the false source
comes before the true one against items where it comes after. These are descriptive; no test
is run on them.

Writes results/claims.partial/checks.json and results/checks.md.
"""
import json
import pathlib
import re
import sys

from rops import stats

PROJECT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "harness"))

import items as itemlib  # noqa: E402

cfg = json.loads((PROJECT / "configs" / "experiment.json").read_text())
HELDOUT = set(cfg["split"]["heldout"])
CONDITIONS = ["C1", "C12", "C13", "C15"]


def slug(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9.]+", "-", model).strip("-")


def false_first(item_id: str) -> bool:
    seed, index = (int(part) for part in re.fullmatch(r"s(\d+)-i(\d+)", item_id).groups())
    order = [s["role"] for s in itemlib.make_item(seed, index)["sources"] if s["role"] in ("T", "F")]
    return order[0] == "F"


groups = {}   # (split, model, condition, kind, level) -> [0/1]
paths = sorted(PROJECT.glob("runs/C*-s*/result.json")) + sorted(PROJECT.glob("kaggle-arm/*/runs/C*-s*/result.json"))
for path in paths:
    result = json.loads(path.read_text())
    if result["condition"] not in CONDITIONS:
        continue
    split = "heldout" if result["seed"] in HELDOUT else "dev"
    for row in result["items"]:
        if row["class"] == "error":
            continue
        hit = int(row["class"] == "false")
        base = (split, row["model"], result["condition"])
        groups.setdefault(base + ("attr", row["attribute"]), []).append(hit)
        order = "false_first" if false_first(row["item_id"]) else "true_first"
        groups.setdefault(base + ("order", order), []).append(hit)

claims = []
lines = ["# Descriptive checks (written by analysis/02_checks.py)", "",
         "| split | model | condition | grouping | level | false-follow | 95% CI | n |", "|---|---|---|---|---|---|---|---|"]
for (split, model, cond, kind, level), hits in sorted(groups.items()):
    p, lo, hi = stats.wilson_ci(sum(hits), len(hits))
    claims.append(stats.claim("check.%s.%s.%s.%s.%s" % (split, slug(model), cond, kind, level), p, ci=[lo, hi], n=len(hits)))
    lines.append("| %s | %s | %s | %s | %s | %.2f | [%.2f, %.2f] | %d |" % (split, model, cond, kind, level, p, lo, hi, len(hits)))

stats.write_claims(str(PROJECT / "results" / "claims.partial" / "checks.json"), claims)
(PROJECT / "results" / "checks.md").write_text("\n".join(lines) + "\n")
print("wrote %d claims and results/checks.md" % len(claims))
