# Red team

Drafted by Claude on 15 November 2026 from the paper in `paper/paper.md` and the files in this repository. The owner should read each answer, correct anything that is wrong, and add their own.

### A1: What decision changes, and for whom, if this result is true?
Status: fixed
Response: An agent-framework developer deciding whether to pass reliability labels to the model decides to pass them only after the harness has verified them (signature check, everything else shown as unverified). The abstract, Introduction and Conclusion state this.

### A2: Where is the positive control, what number did it give, and is it in Results?
Status: fixed
Response: Condition C4 (the prompt names the false source). It opens Section 4.1. Pooled over the two local models the false-follow rate fell from 45 to 8 percent, a drop of 37 points against a threshold of 30; Table 2 gives each of the five models, under the preregistered rule and the changed rule (D1, D2).

### A3: Does any comparison change more than one variable at once?
Status: limited
Response: Yes. The fix bundles three changes (signature check on labels, stripping of label-shaped text, and a sentence in the prompt telling the model that source text is untrusted), so the paper cannot say which part does the work. C5 against C1 also changes the labelling scheme as well as the forged label, which C12 against C1 partly separates. No ablation of the fix was run. The paper says the verification and prompt carry the protection, which is an inference from the prose-forgery result, not a tested claim.

### A4: Could the headline be an artefact of a token cap, truncation, parser, prompt format or judge?
Status: limited
Response: Token cap and truncation are ruled out: replies cut off by the 64-token limit were 56 of 27,200 and truncation was under 1 percent per condition. The parser was audited on every reply and found 3 near-misses. There is no judge. The prompt format is a single wording per condition, so an effect size could change under another format; the paper states this in Section 5.

### A5: Does the abstract state anything that Limitations takes back or narrows?
Status: limited
Response: The abstract's last two sentences ("Developers should pass labels only after verifying them...") are a recommendation drawn from five small open-weight models on synthetic questions, which Section 5 narrows. The abstract does say the questions are made up and the models are open-weight. A tighter closing sentence would say "in these models".

### A6: Do the prereg URL and code URL load, and does the code reproduce the headline numbers?
Status: limited
Response: The repository (github.com/ayodejiades/provenance-label-spoofing) and the prereg-v1 tag page load. The committed runs reproduce every table and figure with `make analyze`. Re-running the model calls needs Ollama for the local arm and a Kaggle GPU for the other three models, so full reproduction is not a one-command job. The links must also be present in the submitted Doc, which is the owner's step.

### A7: What was built or run before the weekend, and is it disclosed?
Status: fixed
Response: Disclosed in the report's "What is new this weekend" section and in README.md: the author's existing general-purpose experiment tooling was used for runs and checks, with no experiment code for this project. The question, items, harness, fix and analysis were written on 13 November 2026, the first day of the sprint, before the kickoff session. The pilot used seed 100, which no reported result uses.

### A8: If an LLM judge scored anything, what is its agreement with hand labels?
Status: rejected
Response: No LLM judge scored anything. Answers are scored by exact match against two planted values in code (harness/score.py), and the scorer was audited on every reply.

### A9: How many seeds or samples per cell, and is variance reported?
Status: limited
Response: Four held-out seeds of 40 items, so 160 items per condition per model, with one reply per item at temperature 0. Wilson intervals and paired bootstrap intervals are reported. Run-to-run variation from sampling is not measured because every run is deterministic at temperature 0; Section 5 says so.

### A10: Does every reported metric have a scale a non-specialist can read?
Status: fixed
Response: The one metric is the share of answers that follow the false source, reported as a percentage, and differences are in percentage points. Table 3 and Figure 1 use the same scale.

### A11: Does Methods describe exactly what ran, with settings identical to configs/?
Status: limited
Response: Temperature, token limit, items, seeds and conditions match configs/experiment.json. The exact prompt wording, the Ollama model quantisations and the Kaggle notebook details are not in the paper; they are in harness/render.py and the configuration files in the repository. Adding a prompt example to an appendix would close this.

### A12: Is any section a second paper that should be cut?
Status: limited
Response: No section is a second paper. The report is over the page limit by about a quarter page in Google's layout, so the candidates to cut are the paragraph on the scorer audit in 4.1, the Patil paragraph in Related Work, and the sentence about the abandoned hosted-model arm in Section 5.

### A13: Which three paragraphs read most like generated text (rops-lint L18/L19 plus the voice audit in the bundle), and did a human rewrite each one in their own words?
Status: limited
Response: rops-lint reports no L18 or L19 findings, but the whole text was drafted by a language model and the owner has so far made light edits. The paragraphs most likely to read as generated are the first paragraph of the Introduction, the Section 4.3 summary paragraph beginning "So the typed claim is not a reliability label", and the Conclusion. They have not yet been rewritten by a human. The LLM Usage Statement says plainly that a model drafted the text.

### N1: Is following a "verified" label evidence of trust, or just instruction following, and does the Conclusion overclaim by saying labels change what models believe?
Status: limited
Response: The prompt explains what "verified" means, so the effect shows models follow a stated signal, which is the practical question for a developer. It does not show a change in belief. The Conclusion's first sentence ("change what language models believe") overreaches and should say "change which source models follow".

### N2: With about half the answers going to the false source when there is no signal, are the label effects just a coin flip resolved by any cue?
Status: limited
Response: The baseline false-follow rate is near 50 percent in three models and 18 percent in phi4:14b, so models have no ground truth to use beyond the sources. That is the intended condition: a framework passes labels exactly when the model cannot tell. The decoy (C3) shows an uninformative cue moves the rate by at most 8 points, and the honest-label and typed-claim results differ by more than that, so the effect is specific to reliability content. A setting where the model can partly judge the sources itself was not tested.

### N3: Do the headline claims depend on models that failed the preregistered positive control?
Status: limited
Response: Two models (llama3.1:8b, phi4:14b) fail the preregistered control rule and pass only the changed rule (D1, D2). Three models pass the original rule, and the main pattern (labels help, a forged metadata label raises false-following, a typed claim works under partial coverage) holds in each of those three as well. The paper does not yet say this in one sentence and should.

### N4: Are the fix results double-counted?
Status: fixed
Response: Conditions C11 and C14 give the model the same prompt after the fix and returned identical replies, so the metadata forgery and the label-shaped claim under partial coverage count as one test. Section 4.4 and Table 4 say so, leaving four distinct settings per model.

### N5: Is the fix tested against an adversary who knows it?
Status: limited
Response: No. The stripper's patterns were written against the development phrasings and tested on held-out phrasings written by two local models that never saw the fix. It removed every label-shaped claim and no prose claim, so stripping is weak, and the paper says so. Nobody tried to write a typed claim to defeat the fix, and the signature check was not attacked by an adversary who holds the signing key. Section 5 and Appendix A state this.
