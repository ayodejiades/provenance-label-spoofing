"""Stage the exploratory hosted-model arm: one project per model under explore-arm/.

NOT preregistered (PREREG.md, "Not in this preregistration"). Free hosted models reached
through the OpenCode command-line agent, which wraps every prompt in its own agent prompt, so
these models are tested inside an agent harness, not bare. A subset of conditions on held-out
seeds 4 and 5 (the same items the other arms see). The control is the D2 form.

    python3 harness/make_hosted_arm.py
    rops-run grid explore-arm/<name> --provider opencode
"""
import json
import pathlib
import re
import shutil

PROJECT = pathlib.Path(__file__).resolve().parents[1]
cfg = json.loads((PROJECT / "configs" / "experiment.json").read_text())
MODELS = ["opencode/deepseek-v4.1-flash-free", "opencode/glm-5.3-flash-free"]
CONDITIONS = ["C4", "C1", "C2", "C5", "C12", "C13", "C14", "C15", "C16"]
SEEDS = [4, 5]

for model in MODELS:
    name = "hosted-" + re.sub(r"[^a-z0-9]+", "-", model.split("/", 1)[1].lower()).strip("-")
    stage = PROJECT / "explore-arm" / name
    if (stage / "harness").exists():
        shutil.rmtree(stage / "harness")
    shutil.copytree(PROJECT / "harness", stage / "harness", ignore=shutil.ignore_patterns("__pycache__"))
    (stage / ".rops").mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROJECT / ".rops" / "limits.json", stage / ".rops" / "limits.json")
    staged = dict(cfg)
    staged.pop("kaggle_arm", None)
    staged["provider"] = "opencode"
    staged["models"] = [{"name": model, "provider": "opencode"}]
    staged["seeds"] = SEEDS
    staged["split"] = {"development": [], "heldout": SEEDS}
    staged["calls_per_run"] = cfg["items_per_run"]
    staged["positive_control"] = {"condition": "C4", "baseline": "C1", "metric": "true_follow",
                                  "threshold": 0.3, "direction": ">="}
    staged["conditions"] = [c for cid in CONDITIONS for c in cfg["conditions"] if c["id"] == cid]
    staged["exploratory"] = "not preregistered; hosted model inside the OpenCode agent harness"
    (stage / "configs").mkdir(exist_ok=True)
    (stage / "configs" / "experiment.json").write_text(json.dumps(staged, indent=2) + "\n")
    for folder in ("runs", "results"):
        (stage / folder).mkdir(exist_ok=True)
    print("staged %s (%s)" % (stage.relative_to(PROJECT), model))
