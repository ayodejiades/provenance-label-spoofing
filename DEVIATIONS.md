# Deviations

## D1: positive control for a model that reports the conflict (13 November 2026, 17:15 Lagos)

Drafted by Claude; decided by Ayodeji after seeing the numbers below.

**What the preregistration says.** The positive control passes when the false-follow rate of
C4 (the prompt names the false source) is at least 0.30 below that of C1 (no labels).

**What happened.** phi4:14b on Kaggle: C1 false-follow 0.175, C4 false-follow 0.003, a
contrast of -0.172, so the control failed and the grid stopped before any other condition.
In C1 phi4 named both values or said the sources conflict in 61.6% of replies, so its
false-follow rate started below 0.30 and a 0.30 drop was not reachable. Its true-follow rate
went from 0.191 in C1 to 0.988 in C4 (320 items each), so the model did use the instruction.

**Why the rule was wrong.** The threshold was set after a pilot on qwen2.5:7b and
llama3.1:8b only, which always name one value. It did not allow for a model whose baseline
answer is to report the conflict.

**The change.** For a model whose C1 false-follow rate is below 0.30, the positive control
passes when the true-follow rate of C4 minus that of C1 is +0.30 or higher. Models whose C1
false-follow rate is 0.30 or higher keep the preregistered rule. The same change applies to
gemma3:12b or mistral-nemo:12b if either stops for the same reason.

**What had been seen when this was decided.** phi4's C1 and C4 only (16 runs, 640 calls). No
other phi4 condition had run. The local arm's control and the other two Kaggle notebooks
had not reported.

**What is done about it.** phi4's grid is run again on Kaggle with the changed control. The
first C1 and C4 runs are kept as they are; the first control result is saved as
`kaggle-arm/epi-phi4-14b/results/positive_control.first.json`. The primary metric, the
hypotheses, the decision rule and every other condition are unchanged. Because phi4 often
names both values, its "both" rate is reported beside its false-follow rate in every condition.
