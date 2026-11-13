"""Audit of the exact-match scorer on every main-phase reply.

Counts replies, replies with no `ANSWER:` line (scored on the whole reply), replies cut off
by the token limit, and near-misses: replies scored "neither" (outside the closed-book
condition) that contain a planted value once punctuation, spacing and case are removed. A
near-miss would mean the scorer missed an answer because of formatting.

Writes results/claims.partial/audit.json and results/audit.md.
"""
import json
import pathlib
import re
import sys

from rops import stats

PROJECT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "harness"))

import items as itemlib  # noqa: E402


def squash(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())


paths = (sorted(PROJECT.glob("runs/C*-s*/result.json")) + sorted(PROJECT.glob("kaggle-arm/*/runs/C*-s*/result.json"))
         + sorted(PROJECT.glob("explore-arm/*/runs/C*-s*/result.json")))
total = no_line = cut = neither_open = errors = 0
near = []
for path in paths:
    result = json.loads(path.read_text())
    for row in result["items"]:
        total += 1
        if row["class"] == "error":
            errors += 1
            continue
        reply = row["reply"] or ""
        no_line += not re.search(r"answer\s*:", reply, flags=re.I)
        cut += row.get("finish_reason") in ("length", "max_tokens")
        if result["condition"] != "C0" and row["class"] == "neither":
            neither_open += 1
            seed, index = (int(p) for p in re.fullmatch(r"s(\d+)-i(\d+)", row["item_id"]).groups())
            item = itemlib.make_item(seed, index)
            if squash(item["true"]) in squash(reply) or squash(item["false"]) in squash(reply):
                near.append("%s %s %s: %s" % (row["model"], result["condition"], row["item_id"], reply[:120]))

claims = [stats.claim("audit.replies", total), stats.claim("audit.errors", errors),
          stats.claim("audit.no_answer_line", no_line), stats.claim("audit.cut_off", cut),
          stats.claim("audit.neither_with_sources", neither_open), stats.claim("audit.near_misses", len(near))]
stats.write_claims(str(PROJECT / "results" / "claims.partial" / "audit.json"), claims)
lines = ["# Scorer audit (written by analysis/03_audit.py)", "",
         "- replies: %d" % total, "- failed calls: %d" % errors,
         "- replies with no ANSWER: line (scored on the whole reply): %d" % no_line,
         "- replies cut off by the token limit: %d" % cut,
         "- replies scored neither, sources shown: %d" % neither_open,
         "- near-misses (a planted value present but not matched): %d" % len(near), ""] + ["- " + n for n in near]
(PROJECT / "results" / "audit.md").write_text("\n".join(lines) + "\n")
print("wrote %d claims and results/audit.md (%d replies, %d near-misses)" % (len(claims), total, len(near)))
