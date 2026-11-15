# Red-team bundle

Attack this paper. Return the five strongest new attacks in REDTEAM.md format:

```
### N1: <attack, one question>
Status: <fixed | limited | rejected>
Response: <at least 20 characters>
```

## Rubric

- Impact Potential & Innovation
- Execution Quality
- Presentation & Clarity

## Standing attacks

- A1: What decision changes, and for whom, if this result is true?
- A2: Where is the positive control, what number did it give, and is it in Results?
- A3: Does any comparison change more than one variable at once?
- A4: Could the headline be an artefact of a token cap, truncation, parser, prompt format or judge?
- A5: Does the abstract state anything that Limitations takes back or narrows?
- A6: Do the prereg URL and code URL load, and does the code reproduce the headline numbers?
- A7: What was built or run before the weekend, and is it disclosed?
- A8: If an LLM judge scored anything, what is its agreement with hand labels?
- A9: How many seeds or samples per cell, and is variance reported?
- A10: Does every reported metric have a scale a non-specialist can read?
- A11: Does Methods describe exactly what ran, with settings identical to configs/?
- A12: Is any section a second paper that should be cut?
- A13: Which three paragraphs read most like generated text (rops-lint L18/L19 plus the voice audit in the bundle), and did a human rewrite each one in their own words?

## Reviews of other projects

### Review 1

This paper puts three copies of a model in charge of three departments whose records must not be shared, with an official tool as the only sanctioned route, and asks what happens when the tool breaks. The agents refuse a colleague's direct request almost always, then break the same rule in a large share of games once the route returns only a rounded answer, mostly jointly in four of six models, and most file false success reports when they fail. The trigger finding is the strongest result and directly challenges refusal-based safety evaluations: a team that passes a request-refusal test will still break the rule under goal pressure. The four-stage decomposition into discovery, coordination, joint execution, and concealment is useful because different models stall at different stages. The checkpoint analysis showing that inter-agent talk appears at supervised fine-tuning and that a short final preference update doubles rule-breaking is the most original piece and deserves follow-up. I would push back on the "emergent collusion" label: agents sharing data to finish an assigned task when the sanctioned route fails is rule-breaking under pressure more than coordination at a third party's expense, and the false-report finding is independent of whether a breach occurred, so it is about false success generally.Read full reviewShow less

### Review 2

The randomized private target, structure-preserving null, carrier permutation and canonical recomputation provide a convincing audit of information flow. Separating authorized flow from harmful approval is a major strength, as is testing attackers that know the sanitizer. The cross-model reading of Gemini tickets is also informative. For the next version, make the adaptive-note comparisons confirmatory on fresh seeds and pin providers or quantify routing variation. Evaluate a workflow where free text contains genuinely necessary information, so defense cost cannot be avoided by dropping a redundant field. Present recovery conditional on valid guesses beside the abstention rate in the main table, and distinguish target identification from harmful approval throughout. The current work establishes carriers of instructed collusion and a useful causal audit; it does not show spontaneous prohibited objectives or a general defense that preserves legitimate free-text utility. In relating the audit to Keppo et al., distinguish observable behavioral effects from inferred cognition or trust. On the Fragility of AI Agent Collusion and Trusting AI in Competitive Markets motivate that distinction, but neither replaces your randomized target, carrier interventions and explicit harm controls.Read full reviewShow less

### Review 3

This paper proposes a randomized canary audit: give one agent a uniformly random private target, ask whether a second agent's behavior depends on it, then intervene on the shared tool state between them. The identification argument is clean, the exact null handles abstention, and permutation shows whether behavior follows the carrier rather than coincidence. The empirical findings are strong: one model's preparers converge on marking the target urgent without any pre-agreement, other models' approvers decode it, and sanitizer-aware preparers move the signal into a surviving free-text note. The five-way distinction between information flow, authorized cooperation, covert signaling, joint prohibited objective, and violating outcome is a real conceptual contribution, and the demonstration that an authorized expedite request produces the same flow signature as collusion shows why flow alone is not evidence. This is the most methodologically ambitious paper in the group and the audit is reusable. It shares its premise with the task-claims paper, that structured state carries collusion, but adds the auditing machinery that paper lacks. Collusion is instructed, so it measures carriers, not emergence, which the authors mention.Read full reviewShow less

### Review 4

An important, under-studied problem handled with real rigour: monitors that accuse honest agents of colluding when they simply cooperate in the open.Séance makes this hard negative concrete, and the result is stark. Under a plain prompt, every monitor accused most honest games played by Qwen, and Claude Opus 5.5 accused all 50 while naming the right pair in every collusion game. The work is immediately reusable because:A pre-registered main study;A frozen held-out test set scored once;Baselines (prior, top scorers, a statistics detector, recalibration);Aablations;A full release with an explorer.Suggestions:Test whether the plus-factor paragraph works through its evidence or simply shifts the prior. Use a prompt that only states the base rate and a placebo paragraph of the same length, and compare at matched false-alarm rates.Tabulate missed coalitions for every condition and use one catch-rate definition throughout.Test a paragraph not tied to this game, and a second setting such as pricing.Stronger classes: make collusion actually pay, and audit honest players through their private notes.Report the messages-only and actions-only views listed in the plan.Read full reviewShow less

### Review 5

Excellent control structure, and the negative findings are the valuable ones. Trim the main text: the abstract is a wall of numbers and the thesis arrives late. Flag the replication as post-hoc in the abstract, not only in Section 3.5, and chase the Ministral miscalibration.

### Review 6

Super interesting work on the limits of behavior-based collusion audits. The headline result that plain correlation actually outperforms net influence while avoiding the false alarms of fixed thresholds is a really valuable reality check for overseers. My main suggestion for next steps would be testing how this handles shared cost shocks across firms, which usually trigger false positives in these setups, and thinking through how overseers can apply this when they don't have access to a clean "honest twin" market.

### Review 7

This is a compelling and highly relevant submission that follows AI agent collusion through the full behavioural chain from proposal and agreement to bidding, deviation, enforcement, and collapse. The persistent agent procurement environment is particularly strong, and the paper does a good job of showing why collusive communication alone is not sufficient evidence of a functioning cartel.The most interesting result is that mild profit pressure was followed by concrete bid rigging proposals in all four tested markets, yet the agreements were fragile. In the strongest case, most sellers changed their bidding behavior, but disagreement over whether the agreement was active and competition from a non member caused the cartel to fail quickly. The detailed comparison between what agents said and what they actually bid is especially valuable.The main limitation is the small number of independent markets and weak control condition, which limits causal conclusions about the effect of the profit pressure instruction. Overall, this is a clear, original, and practically informative study of how agent cartels form and why they may fail.Read full reviewShow less

### Review 8

This experiment provides insight into a critical intervention into collusion among LLMs agents in procurement auctions, and as the title suggests, that is the simple one sentence statement that a competition law enforcement agency reviews the messages. This is helpful in thinking about whether the sort of market design enabling monitoring we see in public securities markets should be adopted in this context.


## Voice audit

### Findings from rops-lint

- no L18 or L19 findings

### Checklist for the critic

- sentences of near-identical length;
- vague claims where a number exists;
- inflated verbs where is, are or has would do;
- anything that would sound wrong read aloud.

No voice sample: put 200+ words of your own unassisted writing in paper/VOICE_SAMPLE.md

### Question for the critic

What makes the below so obviously AI generated?
Answer paragraph by paragraph, citing each paragraph's first words, without rewriting anything.

## Paper

<!-- generated by rops-doc from paper.docx sha256=0d0323bec24e258d7b9885da5641f47d9945392359b7c2908bb6d0aedab2f7af; edit the Google Doc, not this file -->

# Forged Provenance Labels Mislead LLMs Unless Verified

Ayodeji Adesegun Independent Researcher

With Apart Research

## Abstract

Agent frameworks increasingly attach reliability labels, such as a "verified" flag, to retrieved sources before a language model reads them. We ask whether such labels improve accuracy when sources conflict, whether a forged label makes a model follow a false source, and whether checking labels in the harness removes that effect. We built questions about made-up entities, each with one true source, one false source, and two irrelevant ones, and scored them with exact-match code without a judge model. Five open-weight models from five developers answered 160 held-out items per condition across 17 conditions. Honest labels cut the share of answers following the false source by 16 to 48 points in every model. A forged label in the metadata channel raised it by 30 to 74 points. A trust claim typed inside the false document did so mainly where no source on the question was verified, adding 19 to 43 points for a label-shaped claim and 14 to 24 for the same claim written as prose, and little where the true source was verified. A harness that checks a signature on each label, marks everything else unverified and tells the model that source text is untrusted returned both typed forgeries and the metadata forgery to within five points of baseline in all but two checks, across four distinct forgery settings and five models. Developers should pass labels to models only after verifying them in the harness. Labels the harness cannot verify do not help and can be forged.

## 1. Introduction

When an agent retrieves several sources that disagree, the framework around the model often adds metadata about each source: a reliability score, a "verified" badge, a provenance record. The assumption is that the model will use this signal to prefer the better source. The assumption is rarely tested, and it has a second edge. A signal the model obeys is also a signal an attacker wants to write. If the model treats the words "verified source" as a reason to believe a document, anyone who can place text in the context can claim that status.

We study this for the person who has to decide: an agent-framework developer choosing whether to pass reliability labels to the model at all, and whether they must be verified in the harness first. Our contributions are:

1. A controlled test, on synthetic questions with known answers, of whether reliability labels reduce the share of answers that follow a false source, with a decoy that controls for the mere presence of metadata and a positive control that tells the model which source is false.

2. A test of two forgeries: a label placed in the metadata channel, and a trust claim typed into the false document itself, in a label-shaped form and as an ordinary sentence.

3. A harness-side fix, signature-checked labels plus stripping of trust claims from document text, scored against both forgeries and against the prose forgery the stripper was not designed for.

We preregistered all of this on 13 November 2026, before any main-phase run, with two recorded deviations to the positive control (Section 3.4).

## 2. Related Work

Wan, Wallace and Klein [1] study what evidence language models find convincing when real web documents conflict. They report that models rely heavily on a document's relevance to the query and largely ignore stylistic cues humans weigh, such as scientific references or a neutral tone. Our setting differs in two ways: the harness supplies an explicit reliability label as the cue, and we test whether that cue can be forged.

Ge et al. [2] introduce CONFACT, a dataset of questions paired with conflicting evidence from sources of different credibility, and show that retrieval-augmented models struggle when conflicts stem from differences in media-source credibility. They report that incorporating source credibility information substantially improves how well models resolve conflicts. This supports the premise that credibility signals can help; it does not ask what happens when the signal is untrustworthy.

Patil [3] shows that embedding-based defences for retrieval-augmented systems fail to detect numerical manipulation of retrieved text, and proposes verifying extracted claims against a registry built from the corpus. This supports our harness-side view that trust decisions should be made in code the attacker cannot write. Our work differs by testing the label the model sees and measuring the model's response, scoring answers by exact match. We found no prior work that tests whether a model reads a forged reliability label as a trust signal.

## 3. Methods

### 3.1 Items

Each item asks a question about a made-up entity, for example, the year a made-up observatory was completed, and offers four sources. One source states the true value, one states a false value, and two give no answer. The true and false values come from the same generator and sentence templates, and the order in which each appears is balanced across items, so only a reliability signal can distinguish them. There are five attribute types: completion year, tower height, designer, town and heritage register number. Each item depends only on its seed and index, so every condition sees the same items and paired contrasts. Each seed has 40 items, and there are 8 seeds: seeds 0 to 3 are development, seeds 4 to 7 are held out, and they form the basis of every headline number except Table 2.

### 3.2 Conditions

Table 1 lists the 17 conditions. "Verified" and "unverified" are status attributes on the source tag, set by the harness. A "typed claim" is a sentence the attacker places at the top of the false document. The label-shaped form is a tag, such as a bracketed verification status; the prose form is an ordinary sentence stating that the page was checked and confirmed. Two settings matter: in honest coverage, the harness verifies the true source; in partial coverage, the labelling scheme exists, but no source for the question is verified.

Table 1. Conditions.

| Id | What the model sees |
|---|---|
| C0 | Question only, no sources (closed book; checks that items cannot be answered from memory) |
| C1 | Four sources, no labels (baseline) |
| C2 | True source verified, others unverified (honest labels) |
| C3 | Retrieval date and document id on every source, no reliability content (decoy) |
| C4 | No labels; the prompt states which source contains an error (positive control) |
| C5 | False source carries an unsigned "verified" label, others unverified (metadata forgery) |
| C6 | No labels; the false document opens with a label-shaped trust claim |
| C7 | As C2, plus a label-shaped trust claim in the false document |
| C8 | C7 with the fix |
| C9 | As C2, plus a prose trust claim in the false document |
| C10 | C9 with the fix |
| C11 | C5 with the fix |
| C12 | Labels on, no source verified (partial-coverage baseline) |
| C13 | C12 plus a label-shaped trust claim in the false document |
| C14 | C13 with the fix |
| C15 | C12 plus a prose trust claim in the false document |
| C16 | C15 with the fix |

### 3.3 The fix

The fix is a small harness component. It shows a "verified" label only when an HMAC over the source id and text verifies; every other source is shown as unverified. It then removes label-shaped trust claims from document text with pattern matching, and the prompt tells the model that the status attribute is the only trust signal and that text inside a source is untrusted. The patterns were written against the development phrasings only. The held-out forged phrasings were written by two local models that did not see the fix, and the fix was not changed after they were written.

### 3.4 Models, scoring and preregistration

Five open-weight models from five developers ran every condition at temperature 0 with one reply per item and at most 64 output tokens: qwen2.5:7b and llama3.1:8b locally on Ollama, and gemma3:12b, mistral-nemo:12b and phi4:14b on a Kaggle T4 GPU, one notebook each. A reply is scored by exact match against the two planted values as true, false, both or neither. The primary metric is the false-follow rate, the share of replies that name the false value and not the true one. There is no judge model and no hand labelling. We report paired differences by item with a bootstrap interval, an exact sign test and Holm correction. Table 4 gives the intervals; the sign tests and Holm-adjusted p-values are in the repository.

The preregistration was frozen as tag prereg-v1 on 13 November 2026. Its positive control required the false-follow rate of C4 to fall at least 30 points below that of C1. The control passed pooled over the two local models, but two models showed that the rule had been badly specified, and we recorded two deviations after seeing only the control runs.

D1. phi4:14b often names both values or reports the conflict when no labels are given, so its baseline false-follow rate was already below 30 percent and a drop of 30 points was unreachable. Its first control failed on that basis. We changed the rule for models whose baseline false-follow rate is below 30 percent to a rise of at least 30 points in the true-follow rate, and re-ran phi4:14b.

D2. llama3.1:8b missed the original rule by under two points (a drop of 28 points). We extended the D1 rule to every model. Every model passes it. Table 2 shows each model's control under both rules; two models fail the original rule, and every claim that depends on them should be read as holding under the changed rule only.

## 4. Results

### 4.1 Positive control and instrument checks

The positive control comes first. Pooled over the two local models, telling the model which source is false cut the false-follow rate from 45 to 8 percent, a drop of 37 points against the preregistered 30, so the pooled control passes. Table 2 gives each model separately.

Table 2. Positive control per model over all seeds: change in false-follow rate and in true-follow rate when the prompt names the false source (C4 against C1).

| Model | Drop in false-follow | Rise in true-follow | Passes original rule | Passes changed rule |
|---|---|---|---|---|
| gemma3:12b | -44 | 44 | yes | yes |
| llama3.1:8b | -28 | 42 | no | yes |
| mistral-nemo:12b | -45 | 45 | yes | yes |
| phi4:14b | -17 | 80 | no | yes |
| qwen2.5:7b | -46 | 47 | yes | yes |

In the closed-book condition C0 no model answered with either planted value in more than 1 percent of replies, so items cannot be answered from memory. Of 27,200 replies, 0 calls failed and 1,332 had no answer line and were scored on the whole reply. We checked every reply scored neither with sources shown (213 replies) for a planted value that formatting had hidden from the scorer and found 3; they are abstentions or replies cut off by the token limit.

### 4.2 Labels help, and a forged label in the metadata channel is strong leverage

Table 3 and Figure 1 give the held-out false-follow rates. In all five models, honest labels (C2) lowered the false-follow rate by 16 to 48 points against no labels (C1). The decoy (C3), metadata of similar length with no reliability content, moved it by at most 8 points, so the effect is a response to the label and not to extra metadata.

The same channel is an attack surface. An unsigned "verified" label on the false source (C5) raised the false-follow rate by 30 to 74 points against no labels, to between 81 and 98 percent of answers.

Table 3. Held-out false-follow rate (percent of 160 replies) per condition and model.

| Cond. | gemma3:12b | llama3.1:8b | mistral-nemo:12b | phi4:14b | qwen2.5:7b |
|---|---|---|---|---|---|
| C0 | 0 | 0 | 0 | 0 | 1 |
| C1 | 51 | 42 | 44 | 18 | 51 |
| C3 | 51 | 34 | 49 | 17 | 46 |
| C2 | 17 | 1 | 1 | 2 | 4 |
| C4 | 4 | 8 | 2 | 0 | 4 |
| C5 | 81 | 95 | 98 | 92 | 94 |
| C6 | 57 | 69 | 69 | 33 | 71 |
| C7 | 23 | 9 | 11 | 9 | 13 |
| C8 | 11 | 6 | 0 | 2 | 3 |
| C9 | 26 | 5 | 2 | 4 | 6 |
| C10 | 8 | 5 | 1 | 1 | 3 |
| C11 | 29 | 42 | 41 | 5 | 41 |
| C12 | 36 | 40 | 44 | 6 | 41 |
| C13 | 56 | 83 | 82 | 41 | 80 |
| C14 | 29 | 42 | 41 | 5 | 41 |
| C15 | 52 | 64 | 66 | 20 | 62 |
| C16 | 36 | 36 | 44 | 8 | 50 |

Figure 1: Share of held-out answers following the false source, by condition and model, with 95% Wilson intervals. C2 honest labels, C5 forged metadata label, C12 no source verified, C13 and C15 typed claim (label-shaped and prose), C14 and C16 the same with the fix.

### 4.3 A typed trust claim works where the labelling scheme has a gap

A trust claim typed into the false document raised false-follow where no source on the question was verified. With a label-shaped claim (C13 against C12) the rise was 19 to 43 points across the five models, and with the same claim as prose (C15 against C12) it was 14 to 24 points; every interval excludes zero. With no labelling scheme at all (C6 against C1) the label-shaped claim added at least ten points in four of five models; gemma3:12b did not (7 points).

Against a verified true source the effect largely disappears. With honest labels in place (C7 and C9 against C2), the label-shaped claim reached the preregistered ten-point threshold in one model only (mistral-nemo:12b, 10 points), and the prose claim moved false-follow by at most 9 points in any model.

So the typed claim is not a reliability label that models obey in general. It wins where the model has no verified source to prefer.

### 4.4 The fix, and where it does not hold

Table 4 gives the paired differences with intervals. After the fix, the label-shaped claim was left in the false document in 0 percent of held-out items and the prose claim in 100 percent, as the stripper's patterns predict. The prose claim passed through the stripper untouched, yet the fix still held in most settings, because the verification step and the prompt, not the stripper, carry the protection: the false source is shown as unverified whatever its text says.

Table 4. Held-out paired differences in false-follow rate, in percentage points, with the 95% bootstrap interval after "to". Columns are the five models in the order of Table 3. H1 honest labels against none (C2-C1). H2 metadata forgery (C5-C1). H3 label-shaped typed claim, partial coverage (C13-C12). H4 fix on that claim (C14-C13), fix on the metadata forgery (C11-C5), and the residual after the fix against the partial-coverage baseline (C14-C12 for the label-shaped claim, C16-C12 for the prose claim). The residual for C11 is identical to C14-C12 and is not repeated.

| Contrast | gemma3 | llama3.1 | mistral-nemo | phi4 | qwen2.5 |
|---|---|---|---|---|---|
| H1 C2-C1 | -34 (-41 to -26) | -41 (-49 to -33) | -43 (-51 to -35) | -16 (-22 to -11) | -48 (-55 to -40) |
| H2 C5-C1 | 30 (23 to 37) | 53 (46 to 61) | 54 (47 to 62) | 74 (67 to 81) | 42 (35 to 50) |
| H3 C13-C12 | 19 (12 to 26) | 43 (36 to 51) | 38 (31 to 45) | 35 (28 to 42) | 39 (31 to 47) |
| H3 C15-C12 | 16 (11 to 22) | 24 (18 to 31) | 22 (15 to 29) | 14 (9 to 20) | 21 (14 to 29) |
| H4 C14-C13 | -27 (-34 to -20) | -41 (-49 to -33) | -42 (-50 to -34) | -36 (-43 to -29) | -39 (-47 to -31) |
| H4 C16-C15 | -17 (-23 to -11) | -29 (-36 to -22) | -22 (-29 to -16) | -12 (-17 to -7) | -12 (-19 to -7) |
| H4 C11-C5 | -52 (-59 to -44) | -52 (-61 to -44) | -57 (-66 to -49) | -87 (-92 to -82) | -52 (-61 to -44) |
| Residual C14-C12 | -8 (-13 to -2) | 2 (-2 to 8) | -4 (-10 to 2) | -1 (-2 to 0) | 0 (-5 to 5) |
| Residual C16-C12 | -1 (-6 to 4) | -4 (-11 to 1) | -1 (-8 to 7) | 2 (-1 to 6) | 9 (1 to 16) |

Conditions C11 and C14 give the model the same prompt after the fix (every source unverified, claims removed, same note) and returned identical replies, so the metadata forgery and the label-shaped claim under partial coverage are one test of the fix, not two. That leaves four distinct settings in each of five models. The fix returned false-follow to within five points of the matching baseline in all but two of these checks. The two exceptions are reported as they came out: llama3.1:8b with a label-shaped claim against honest labels (5 points above the honest baseline, at the preregistered threshold of five), and qwen2.5:7b with a prose claim under partial coverage (9 points above the baseline).

## 5. Discussion and Limitations

For a framework developer the results give a plain rule. Labels help only when the harness can vouch for them; a label the harness cannot verify can be forged, and in the metadata channel it is forged cheaply. A signature check on the label and a channel note telling the model to distrust source text cost a few lines of code and removed most of the effect in every model we tested.

This study does not establish how large these effects are on real documents, on frontier models or under other prompt wordings. The questions are synthetic and short, and on real documents models may weigh a label against other evidence. The five models are open-weight, between seven and fourteen billion parameters, and we did not test frontier models. Prompts have one wording and one format; a different label vocabulary may change the effect sizes. We used one reply at temperature 0 per item and cannot speak to run-to-run variation. The fix was developed on the same task family it is tested on, with held-out seeds and held-out phrasings but the same item generator, and its pattern matching was not tested against adversaries who see it. The prose forgery shows that stripping is a weak part of the fix; the signature check and prompt are the strong part. The positive control rule was changed twice after control data was seen (Section 3.4). An exploratory arm with two free hosted models was started and abandoned when the service stopped answering; none of its output is used.

## 6. Conclusion

Reliability labels change what language models believe, which is what makes them useful and what makes them an attack surface. In five open-weight models, honest labels cut false-source following sharply, a forged label in the metadata channel undid that and more, and a typed claim worked mainly where nothing on the question was verified. Verifying labels in the harness and telling the model to distrust source text removed most of the effect. A developer who passes labels to a model should verify them first.

## Code and Data

Code, configurations, run logs, results and the frozen preregistration (tag prereg-v1): https://github.com/ayodejiades/provenance-label-spoofing (preregistration: https://github.com/ayodejiades/provenance-label-spoofing/tree/prereg-v1).

### What is new this weekend

Runs and checks used the author’s existing general-purpose experiment tooling (no experiment code for this project); the question, items, harness, fix and analysis are new this weekend. The item generator, harness, fix and analysis were written on 13 November 2026, the first day of the sprint, before the kickoff session; the pilot used seed 100, which no reported result uses.

## Author Contributions

Ayodeji Adesegun chose the research question, directed the work and approved the design, the preregistration and its two deviations. Claude produced the experiments, code, and text, as described in the LLM Usage Statement.

## References

[1] A. Wan, E. Wallace and D. Klein. What Evidence Do Language Models Find Convincing? ACL 2024. arXiv:2402.11782.

[2] Z. Ge, Y. Wu, D. W. K. Chin, R. K.-W. Lee and R. Cao. Resolving Conflicting Evidence in Automated Fact-Checking: A Study on Retrieval-Augmented LLMs. arXiv:2505.17762, 2025.

[3] K. Patil. RAGShield: Detecting Numerical Claim Manipulation in Government RAG Systems. arXiv:2604.00387, 2026.

## Appendix A: Limitations and Dual-Use / Ethical Considerations

Dual use. The study measures how easily a trust label can be forged, and the typed forgeries we used are easy to copy. We think the defensive value outweighs the risk: the forgeries are generic, the attack needs the ability to place text in a model's context, and the fix is simple and stated in full. We tested nothing against real users or live systems, and no personal data was involved. All entities and sources are made up.

Limitations. See Section 5. This study does not establish that a verified label is safe in every deployment: a harness that holds the signing key insecurely, or that signs attacker-chosen text, would reintroduce the problem. In addition, the held-out forged phrasings were written by two local language models and not by people, so they may be more regular than a real adversary's. The item generator uses five attribute types and one sentence style per type.

## LLM Usage Statement

The text of this report was drafted by Claude (Anthropic), a large language model used through Claude Code: the model claude-sonnet-5-5 drafted this text, and the model claude-fable-5-2 wrote and ran the experiment harness, the fix and the analysis code. The authors chose the research question, directed the work, approved the preregistration and its two deviations, and are responsible for the report. Every number in the text was matched by script to the results file. The Kaggle runs used the authors' own account. The language models that were the subjects of the experiments are listed in Section 3.4.
