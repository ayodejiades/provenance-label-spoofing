"""False-follow rates per condition and model, and the paired contrasts in PREREG.md.

Reads runs/C*-s*/result.json and the Kaggle arm's kaggle-arm/*/runs/C*-s*/result.json
(pilot runs are ignored). Held-out seeds give the headline
numbers; development seeds are reported separately. Every rate has a Wilson interval, every
contrast is paired by item, with a bootstrap interval and an exact sign test, Holm-corrected
per model over the H1 to H4 contrasts.

Writes results/claims.partial/rates.json and results/tables.md.
"""
import json
import math
import pathlib
import re

from rops import stats

PROJECT = pathlib.Path(__file__).resolve().parents[1]
cfg = json.loads((PROJECT / "configs" / "experiment.json").read_text())
HELDOUT = set(cfg["split"]["heldout"])

# (id, A, B): the contrast is rate(A) - rate(B) on the same items
CONTRASTS = [
    ("pc", "C4", "C1"), ("decoy", "C3", "C1"), ("label_frame", "C12", "C1"),
    ("h1_honest", "C2", "C1"), ("h2_metadata_forgery", "C5", "C1"),
    ("h3_tag_no_labels", "C6", "C1"), ("h3_tag_vs_honest", "C7", "C2"),
    ("h3_tag_partial", "C13", "C12"), ("h3_prose_vs_honest", "C9", "C2"),
    ("h3_prose_partial", "C15", "C12"),
    ("h4_fix_tag_vs_honest", "C8", "C7"), ("h4_fix_prose_vs_honest", "C10", "C9"),
    ("h4_fix_tag_partial", "C14", "C13"), ("h4_fix_prose_partial", "C16", "C15"),
    ("h4_fix_metadata", "C11", "C5"),
    ("residual_tag_vs_honest", "C8", "C2"), ("residual_prose_vs_honest", "C10", "C2"),
    ("residual_tag_partial", "C14", "C12"), ("residual_prose_partial", "C16", "C12"),
    ("residual_metadata", "C11", "C12"),
]
TESTED = [c[0] for c in CONTRASTS if c[0].startswith(("h1", "h2", "h3", "h4"))]


def slug(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9.]+", "-", model).strip("-")


def sign_test(diffs: list) -> float:
    """Exact two-sided sign test on the non-zero paired differences."""
    plus = sum(1 for d in diffs if d > 0)
    minus = sum(1 for d in diffs if d < 0)
    n = plus + minus
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, k) for k in range(0, min(plus, minus) + 1)) / 2 ** n
    return min(1.0, 2 * tail)


rows = {}      # (split, model, condition) -> {item_id: class}
survive = {}   # (split, condition) -> [bool]
for path in sorted(PROJECT.glob("runs/C*-s*/result.json")) + sorted(PROJECT.glob("kaggle-arm/*/runs/C*-s*/result.json")):
    result = json.loads(path.read_text())
    split = "heldout" if result["seed"] in HELDOUT else "dev"
    for row in result["items"]:
        if row["class"] == "error":
            continue
        rows.setdefault((split, row["model"], result["condition"]), {})[row["item_id"]] = row["class"]
        if row.get("claim_survived_fix") is not None:
            survive.setdefault((split, result["condition"]), []).append(bool(row["claim_survived_fix"]))

claims = []
table = ["# Results tables (written by analysis/01_rates.py)", ""]
models = sorted({key[1] for key in rows})
conditions = [c["id"] for c in cfg["conditions"]]
for split in ("heldout", "dev"):
    table += ["## False-follow rate, %s seeds" % split, "",
              "| condition | " + " | ".join(models) + " |", "|---|" + "---|" * len(models)]
    for cond in conditions:
        cells = []
        for model in models:
            classes = rows.get((split, model, cond))
            if not classes:
                cells.append("")
                continue
            n = len(classes)
            for name in ("false", "true", "neither", "both"):
                k = sum(1 for c in classes.values() if c == name)
                p, lo, hi = stats.wilson_ci(k, n)
                claims.append(stats.claim("%s.%s.%s.%s" % (name, split, slug(model), cond), p, ci=[lo, hi], n=n))
                if name == "false":
                    cells.append("%.2f [%.2f, %.2f] n=%d" % (p, lo, hi, n))
        table.append("| %s | %s |" % (cond, " | ".join(cells)))
    table.append("")
    table += ["## Paired contrasts (A minus B), %s seeds" % split, "",
              "| contrast | A | B | model | difference | 95% CI | p (sign) | p (Holm) | pairs |", "|---|---|---|---|---|---|---|---|---|"]
    for model in models:
        found = []
        for cid, a, b in CONTRASTS:
            ra, rb = rows.get((split, model, a)), rows.get((split, model, b))
            if not ra or not rb:
                continue
            shared = sorted(set(ra) & set(rb))
            diffs = [(ra[i] == "false") - (rb[i] == "false") for i in shared]
            mean, lo, hi = stats.mean_ci(diffs)
            found.append((cid, a, b, mean, lo, hi, sign_test(diffs), len(shared)))
        tested = [f for f in found if f[0] in TESTED]
        adjusted = dict(zip([f[0] for f in tested], stats.holm([f[6] for f in tested])))
        for cid, a, b, mean, lo, hi, p, n in found:
            claims.append(stats.claim("diff.%s.%s.%s" % (split, slug(model), cid), mean, ci=[lo, hi], n=n))
            claims.append(stats.claim("p.%s.%s.%s" % (split, slug(model), cid), adjusted.get(cid, p)))
            table.append("| %s | %s | %s | %s | %+.2f | [%+.2f, %+.2f] | %.4f | %s | %d |" % (
                cid, a, b, model, mean, lo, hi, p, ("%.4f" % adjusted[cid]) if cid in adjusted else "", n))
    table.append("")

for (split, cond), flags in sorted(survive.items()):
    claims.append(stats.claim("survived_fix.%s.%s" % (split, cond), sum(flags) / len(flags), n=len(flags)))
    table.append("Forged claims left in the text after the fix, %s %s: %d of %d" % (split, cond, sum(flags), len(flags)))

stats.write_claims(str(PROJECT / "results" / "claims.partial" / "rates.json"), claims)
(PROJECT / "results" / "tables.md").write_text("\n".join(table) + "\n")
print("wrote %d claims and results/tables.md" % len(claims))
