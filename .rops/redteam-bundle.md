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

# <<FILL: paper title>>

## Abstract
<<FILL>>

## 1. Introduction
<<FILL>>

## 2. Related Work
<<FILL>>

## 3. Methods
<<FILL>>

## 4. Results
<<FILL>>

## 5. Discussion and Limitations
<<FILL>>

## 6. Conclusion
<<FILL>>

## Code and Data
<<FILL>>

### What is new this weekend
<<FILL>>

## References
<<FILL>>

## Appendix A: Limitations and Dual-Use / Ethical Considerations
<<FILL>>

## LLM Usage Statement
<<FILL>>
