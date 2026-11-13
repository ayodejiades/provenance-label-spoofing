"""One run = one condition x one seed (called by rops-run grid).

Builds the seed's items, asks every model in the config each item under this condition, scores
the replies by exact match and writes $ROPS_RUN_DIR/result.json.

`false_follow` is the share of scored replies that name the planted false value only, pooled
over models; `by_model` has the same rates per model, and `items` has every reply.

Pilot overrides (never used by the grid): EPI_MODELS="a,b" and EPI_ITEMS=10.
"""
import json
import os
import pathlib
import sys

PROJECT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "harness"))

import items as itemlib  # noqa: E402
import render  # noqa: E402
import score  # noqa: E402
from rops import llm  # noqa: E402

cfg = json.loads((PROJECT / "configs" / "experiment.json").read_text())
cond = json.loads(os.environ["ROPS_CONDITION_JSON"])
seed = int(os.environ["ROPS_SEED"])
out = pathlib.Path(os.environ["ROPS_RUN_DIR"]).resolve()
default_provider = os.environ.get("ROPS_PROVIDER") or cfg.get("provider", "ollama")

models = cfg["models"]
if os.environ.get("EPI_MODELS"):
    models = [name.strip() for name in os.environ["EPI_MODELS"].split(",") if name.strip()]
models = [m if isinstance(m, dict) else {"name": m} for m in models]
count = int(os.environ.get("EPI_ITEMS") or cfg["items_per_run"])
heldout = seed in set(cfg.get("split", {}).get("heldout", []))
max_tokens = int(cond.get("max_tokens", cfg.get("max_tokens", 64)))

CLASSES = ["true", "false", "both", "neither"]


def rates(rows: list) -> dict:
    scored = [r for r in rows if r["class"] in CLASSES]
    n = len(scored)
    summary = {"n": n, "errors": len(rows) - n}
    for name in CLASSES:
        hits = sum(1 for r in scored if r["class"] == name)
        summary[name + "_n"] = hits
        summary[("%s_follow" % name) if name in ("true", "false") else name] = (hits / n) if n else None
    return summary


rows = []
prompts = [(item,) + render.build(item, cond, heldout) for item in itemlib.make_items(seed, count)]
for model in models:            # one model at a time, so a small machine loads each model once
    for item, messages, info in prompts:
        row = {"item_id": item["item_id"], "attribute": item["attribute"], "model": model["name"],
               "false_position": item["false_position"], "forged_claim": info["forged_claim"],
               "claim_survived_fix": info["claim_survived_fix"]}
        try:
            reply = llm.chat(messages, model["name"], provider=model.get("provider", default_provider),
                             temperature=float(cfg.get("temperature", 0.0)), max_tokens=max_tokens)
            row["reply"] = reply["text"]
            row["finish_reason"] = reply["finish_reason"]
            row["class"] = score.classify(reply["text"], item["true"], item["false"])
        except Exception as exc:  # one failed call must not lose the run
            row["reply"] = None
            row["class"] = "error"
            row["error"] = str(exc)[:300]
        rows.append(row)

result = {"condition": cond["id"], "seed": seed, "heldout": heldout, "items_per_run": count,
          "models": [m["name"] for m in models]}
result.update(rates(rows))
result["by_model"] = {m["name"]: rates([r for r in rows if r["model"] == m["name"]]) for m in models}
survived = [r["claim_survived_fix"] for r in rows if r["claim_survived_fix"] is not None]
result["claim_survived_fix_rate"] = (sum(survived) / len(survived)) if survived else None
result["items"] = rows
(out / "result.json").write_text(json.dumps(result, indent=2) + "\n")
