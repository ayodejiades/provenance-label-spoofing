# Provenance Study: does a reliability label help the model or the attacker?

Team discreet entry for the Apart Research AI x Epistemics sprint (13 to 15 November 2026),
Track 2, example project 2.8.

The question, conditions and decision rule are in `PREREG.md`. The experiment asks whether
reliability labels on retrieved sources improve a model's accuracy, whether a forged
"verified" label makes it follow a false source, and whether checking labels in the harness
(`harness/trustgate.py`) removes the effect.

## Reproduce

Run `make reproduce` to rebuild the numbers. It needs Ollama with `qwen2.5:7b` and
`llama3.1:8b`, and the ResearchOps toolkit (`ROPS_HOME`).

The Kaggle arm (gemma3:12b, mistral-nemo:12b, phi4:14b) runs the same harness on a T4 GPU,
one notebook per model:

    python3 harness/make_kaggle_arm.py
    rops-kaggle pack kaggle-arm/<name> --user <kaggle-username>
    rops-kaggle push kaggle-arm/<name>
    rops-kaggle pull kaggle-arm/<name>

`analysis/01_rates.py` reads the local runs and `kaggle-arm/*/runs/` together.

An exploratory arm, not preregistered, runs nine conditions on held-out seeds 4 and 5 with two
free hosted models reached through the OpenCode command-line agent
(`opencode/deepseek-v4.1-flash-free`, `opencode/glm-5.3-flash-free`):

    python3 harness/make_hosted_arm.py
    rops-run grid explore-arm/<name> --provider opencode

These models answer inside OpenCode's own agent prompt, so they are not tested bare. Their
numbers are kept apart from the preregistered claims. Deviations from the preregistration are
in `DEVIATIONS.md` (D1 and D2, both about the positive control).

## What existed before the sprint

- The ResearchOps toolkit (`rops-*` commands) that runs the grid, the ledger and the checks.
  It contains no experiment code for this project.
- Nothing else. The project folder was scaffolded on 11 November 2026 with empty templates.
  The question card, harness, config, analysis script, preregistration draft and a pilot
  (seed 100, 20 items, logged with phase `pilot` in `runs/calls.jsonl`) were made on the
  morning of 13 November 2026, the first day of the sprint, before the kickoff session.

## Who did what

The harness, config and analysis code were written by Claude (Anthropic), a coding agent,
under Ayodeji Adesegun's direction. The question card and preregistration were drafted by
Claude for Ayodeji to review and freeze. Scoring is exact match in code; there is no judge
model and there are no hand labels.
