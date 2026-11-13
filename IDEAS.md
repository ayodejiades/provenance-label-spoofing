# Ideas

| Rank | RQ | Score | Untested | Budget | Prior entries | Question |
|---|---|---|---|---|---|---|
| 1 | 1.6 | 1 | no | ? | 15 | Confidence Audit. Does the model know how solid its claims are? Calibration is already measured on cleanly resolvable questions (ForecastBench, consistency checks). |
| 2 | 1.2 | 0 | no | ? | 44 | Can you measure the gap between what a model implies and what it will defend (e.g. overselling, "flip-flopping", misrepresented evidence)? |
| 3 | 1.5 | 0 | no | ? | 29 | MisleadBench. Models can be technically accurate while leaving a false impression, and existing honesty benchmarks (MASK, DarkBench) mostly test single-turn lies. |
| 4 | 1.7 | 0 | no | ? | 1 | FlipRate. A model that agrees with whoever pushed back last is useless for decisions. |
| 5 | 1.8 | 0 | no | ? | 23 | Epistemic virtue eval suite. Forethought's collective-epistemics sketches propose evaluating calibration, honest uncertainty, manipulation resistance and claim-level scoring, but no maintained suite exists. |
| 6 | 2.1 | 0 | no | ? | 3 | Which source-reliability scoring techniques are hardest to cheat and easiest to audit? |
| 7 | 2.2 | 0 | no | ? | 86 | What minimal tamper-evident layer is missing from today's AI observability standards, so that records of what agents did and agreed can be audited and trusted? |
| 8 | 2.4 | 0 | no | ? | 14 | What fraction of a real domain's content (e.g. council minutes, health advice, financial news) can be automatically bound to checkable evidence today? |
| 9 | 3.2 | 0 | no | ? | 1 | What does a chatbot say to someone mid-dispute, and how often does it escalate rather than de-escalate? |
| 10 | 3.5 | 0 | no | ? | 98 | Dispute Escalation Benchmark. When someone describes a conflict with their landlord, employer or ex-partner, does the chatbot steer them towards repair or escalation (evidence this is a live harm)? Build realistic dispute scenarios, ask practising mediators to define graded good advice, and score frontier models after every release. |
| 11 | 4.1 | 0 | no | ? | 1 | What is this field's equivalent of the QALY: a defensible, comparable unit for "decision quality improved"? |
| 12 | 4.10 | 0 | no | ? | 23 | A wish registry for privacy-preserving matchmaking. Participants privately register offers and needs; an AI matcher reveals a connection only when both sides' criteria are met, with logs auditable by a neutral steward. |
| 13 | 4.4 | 0 | no | ? | 0 | Using only data downloadable this weekend, what can you measure about a live epistemic deployment, and what does that mean for the field? |
| 14 | 4.9 | 0 | no | ? | 10 | Do their numbers match? Pair quantitative claims from parliamentary transcripts and press releases with the statistical releases they cite, flag mismatches with links to primary sources, and publish as an auditable open dataset. |
| 15 | 1.1 | -1 | no | ? | 56 | Does the model understand how solid its claims are? Can you accurately measure its confidence in a decision and verify that against reality? |
| 16 | 1.3 | -1 | no | ? | 35 | Which model behaviours matter for real decision quality, and does ranking well on an honesty benchmark predict better decision-making? |
| 17 | 1.4 | -1 | no | ? | 4 | What does a benchmark need to stay meaningful over time? Which exploits make benchmarks gameable, and can you demonstrate and close one? |
| 18 | 1.9 | -1 | no | ? | 3 | Article 5 measurement protocol. The EU AI Act bans manipulative and deceptive AI techniques, yet regulators have no agreed test procedure. |
| 19 | 2.3 | -1 | no | ? | 30 | When an AI system uses a reliability or provenance tool, does its behaviour and accuracy actually improve? |
| 20 | 2.5 | -1 | no | ? | 35 | Track-Record Ledger. Pundits, forecasters and outlets make checkable public claims, but nobody keeps score in a form software can consume (Community Notes is the closest thing). |
| 21 | 2.6 | -1 | no | ? | 25 | Tamper-Evident Action Recorder. When an AI agent takes a consequential action, the operator's own logs are the only record, and they can be edited. |
| 22 | 2.7 | -1 | no | ? | 4 | Citation Binder. A large share of citations in papers, briefs and Wikipedia articles do not support the sentence they are attached to. |
| 23 | 2.8 | -1 | no | ? | 17 | Provenance Study. Everyone assumes provenance and reliability metadata will help AI systems behave better; nobody has measured it. |
| 24 | 3.1 | -1 | no | ? | 43 | Does advice users act on lead to choices they later endorse, and can you measure whether there is a gap? |
| 25 | 3.3 | -1 | no | ? | 15 | For a decision type (e.g. job offers, leases), does a briefing surface the considerations that actually matter, and how would you know? |
| 26 | 3.4 | -1 | no | ? | 24 | When a group compares its beliefs or forecasts, does surfacing the inconsistencies and cruxes change the decision? |
| 27 | 3.6 | -1 | no | ? | 42 | Decision-Brief Rubric. Use expertise in, for example, financial-guidance, careers or health charities to define a rubric, then build a grading harness scoring chatbot briefings against it. |
| 28 | 3.7 | -1 | no | ? | 11 | Crux Mapper. Groups argue past each other because nobody knows which factual questions actually divide them. |
| 29 | 4.2 | -1 | no | ? | 6 | Which specific certification, budget and approval chokepoints keep official AI tools out of legislatures while staffers use personal accounts? |
| 30 | 4.3 | -1 | no | ? | 10 | Why do institutions ignore forecasts they asked for: access and legibility, or the accountability that explicit predictions create? |
| 31 | 4.5 | -1 | no | ? | 76 | Scenario planning on tap for resilience teams. Run hundreds of LLM narrative simulations & forecasts from a plain-language situation brief and report recurring failure points in the two-page format emergency planners already use. |
| 32 | 4.6 | -1 | no | ? | 6 | Fast facilitation for communities that cannot afford a mediator. An assistant that interviews each participant asynchronously, maps where people actually agree and disagree, and drafts candidate consensus statements for human sign-off. |
| 33 | 4.7 | -1 | no | ? | 18 | QALY for epistemics. Health economics got serious when the QALY gave decision-makers one comparable unit; epistemic interventions have nothing similar, so budgets go to whatever demos well. |
| 34 | 4.8 | -1 | no | ? | 23 | Procurement Gap Report. Legislative staff use personal AI accounts because official procurement cannot keep up. |

## 1.6: Confidence Audit. Does the model know how solid its claims are? Calibration is already measured on cleanly resolvable questions (ForecastBench, consistency checks).
Score: novelty=0 fit=2 cost=0 crowding=-1 → 1
Confidence Audit. Does the model know how solid its claims are? Calibration is already measured on cleanly resolvable questions (ForecastBench, consistency checks). Design a protocol that elicits a model's confidence in its own recommendations across domains where ground truth arrives later, then verify elicited confidence against outcomes.

## 1.2: Can you measure the gap between what a model implies and what it will defend (e.g. overselling, "flip-flopping", misrepresented evidence)?
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0


## 1.5: MisleadBench. Models can be technically accurate while leaving a false impression, and existing honesty benchmarks (MASK, DarkBench) mostly test single-turn lies.
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0
MisleadBench. Models can be technically accurate while leaving a false impression, and existing honesty benchmarks (MASK, DarkBench) mostly test single-turn lies. Build a multi-turn benchmark that first elicits what a model implies, then challenges it to defend the claim, scoring the gap between implied and defended positions, with a question-rotation protocol so scores stay meaningful.

## 1.7: FlipRate. A model that agrees with whoever pushed back last is useless for decisions.
Score: novelty=0 fit=0 cost=0 crowding=0 → 0
FlipRate. A model that agrees with whoever pushed back last is useless for decisions. Single-turn agreement is already measured (SycEval, ELEPHANT). Measure flip curves: how a model's answer and stated confidence change across one, two and three escalating rebuttals, separating warranted updating from capitulation.

## 1.8: Epistemic virtue eval suite. Forethought's collective-epistemics sketches propose evaluating calibration, honest uncertainty, manipulation resistance and claim-level scoring, but no maintained suite exists.
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0
Epistemic virtue eval suite. Forethought's collective-epistemics sketches propose evaluating calibration, honest uncertainty, manipulation resistance and claim-level scoring, but no maintained suite exists. Build them as Inspect tasks with transparent rubrics, run them across frontier models, and publish grader disagreements as part of the result.

## 2.1: Which source-reliability scoring techniques are hardest to cheat and easiest to audit?
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0


## 2.2: What minimal tamper-evident layer is missing from today's AI observability standards, so that records of what agents did and agreed can be audited and trusted?
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0


## 2.4: What fraction of a real domain's content (e.g. council minutes, health advice, financial news) can be automatically bound to checkable evidence today?
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0


## 3.2: What does a chatbot say to someone mid-dispute, and how often does it escalate rather than de-escalate?
Score: novelty=0 fit=0 cost=0 crowding=0 → 0


## 3.5: Dispute Escalation Benchmark. When someone describes a conflict with their landlord, employer or ex-partner, does the chatbot steer them towards repair or escalation (evidence this is a live harm)? Build realistic dispute scenarios, ask practising mediators to define graded good advice, and score frontier models after every release.
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0
Dispute Escalation Benchmark. When someone describes a conflict with their landlord, employer or ex-partner, does the chatbot steer them towards repair or escalation (evidence this is a live harm)? Build realistic dispute scenarios, ask practising mediators to define graded good advice, and score frontier models after every release.

## 4.1: What is this field's equivalent of the QALY: a defensible, comparable unit for "decision quality improved"?
Score: novelty=0 fit=0 cost=0 crowding=0 → 0


## 4.10: A wish registry for privacy-preserving matchmaking. Participants privately register offers and needs; an AI matcher reveals a connection only when both sides' criteria are met, with logs auditable by a neutral steward.
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0
A wish registry for privacy-preserving matchmaking. Participants privately register offers and needs; an AI matcher reveals a connection only when both sides' criteria are met, with logs auditable by a neutral steward.

## 4.4: Using only data downloadable this weekend, what can you measure about a live epistemic deployment, and what does that mean for the field?
Score: novelty=0 fit=0 cost=0 crowding=0 → 0


## 4.9: Do their numbers match? Pair quantitative claims from parliamentary transcripts and press releases with the statistical releases they cite, flag mismatches with links to primary sources, and publish as an auditable open dataset.
Score: novelty=0 fit=1 cost=0 crowding=-1 → 0
Do their numbers match? Pair quantitative claims from parliamentary transcripts and press releases with the statistical releases they cite, flag mismatches with links to primary sources, and publish as an auditable open dataset.

## 1.1: Does the model understand how solid its claims are? Can you accurately measure its confidence in a decision and verify that against reality?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 1.3: Which model behaviours matter for real decision quality, and does ranking well on an honesty benchmark predict better decision-making?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 1.4: What does a benchmark need to stay meaningful over time? Which exploits make benchmarks gameable, and can you demonstrate and close one?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 1.9: Article 5 measurement protocol. The EU AI Act bans manipulative and deceptive AI techniques, yet regulators have no agreed test procedure.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Article 5 measurement protocol. The EU AI Act bans manipulative and deceptive AI techniques, yet regulators have no agreed test procedure. Draft a protocol mapping DarkBench and MASK-style measurements onto Article 5(1)(a) legal language, with worked examples and thresholds.

## 2.3: When an AI system uses a reliability or provenance tool, does its behaviour and accuracy actually improve?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 2.5: Track-Record Ledger. Pundits, forecasters and outlets make checkable public claims, but nobody keeps score in a form software can consume (Community Notes is the closest thing).
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Track-Record Ledger. Pundits, forecasters and outlets make checkable public claims, but nobody keeps score in a form software can consume (Community Notes is the closest thing). Build a public API that records dated claims, resolves them against primary sources, and serves reliability summaries per source, plus a first consumer: a browser extension or feed-reader plugin showing a source's track re

## 2.6: Tamper-Evident Action Recorder. When an AI agent takes a consequential action, the operator's own logs are the only record, and they can be edited.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Tamper-Evident Action Recorder. When an AI agent takes a consequential action, the operator's own logs are the only record, and they can be edited. An example project here could be to build a signed, secure logging layer on the OpenTelemetry GenAI conventions so instrumented agent frameworks emit append-only, verifiable traces (Certificate Transparency is the precedent), plus a viewer for auditors

## 2.7: Citation Binder. A large share of citations in papers, briefs and Wikipedia articles do not support the sentence they are attached to.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Citation Binder. A large share of citations in papers, briefs and Wikipedia articles do not support the sentence they are attached to. Build a tool that locates each cited source and verifies whether it genuinely supports the specific claim, with per-citation verdicts and quoted passages (evaluation data exists: AVeriTeC).

## 2.8: Provenance Study. Everyone assumes provenance and reliability metadata will help AI systems behave better; nobody has measured it.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Provenance Study. Everyone assumes provenance and reliability metadata will help AI systems behave better; nobody has measured it. Run a controlled experiment: the same research tasks with and without machine-readable signals (C2PA manifests, track records, Community Notes context), measuring accuracy, citation quality and susceptibility to planted false sources. Users: agent-framework developers 

## 3.1: Does advice users act on lead to choices they later endorse, and can you measure whether there is a gap?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 3.3: For a decision type (e.g. job offers, leases), does a briefing surface the considerations that actually matter, and how would you know?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 3.4: When a group compares its beliefs or forecasts, does surfacing the inconsistencies and cruxes change the decision?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 3.6: Decision-Brief Rubric. Use expertise in, for example, financial-guidance, careers or health charities to define a rubric, then build a grading harness scoring chatbot briefings against it.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Decision-Brief Rubric. Use expertise in, for example, financial-guidance, careers or health charities to define a rubric, then build a grading harness scoring chatbot briefings against it.

## 3.7: Crux Mapper. Groups argue past each other because nobody knows which factual questions actually divide them.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Crux Mapper. Groups argue past each other because nobody knows which factual questions actually divide them. Run short asynchronous AI interviews with each member, extract claims and probabilities, and render a disagreement map showing shared ground, genuine cruxes and internal inconsistencies (cf. the Habermas Machine, which drafts agreement; this maps disagreement).

## 4.2: Which specific certification, budget and approval chokepoints keep official AI tools out of legislatures while staffers use personal accounts?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 4.3: Why do institutions ignore forecasts they asked for: access and legibility, or the accountability that explicit predictions create?
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1


## 4.5: Scenario planning on tap for resilience teams. Run hundreds of LLM narrative simulations & forecasts from a plain-language situation brief and report recurring failure points in the two-page format emergency planners already use.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Scenario planning on tap for resilience teams. Run hundreds of LLM narrative simulations & forecasts from a plain-language situation brief and report recurring failure points in the two-page format emergency planners already use.

## 4.6: Fast facilitation for communities that cannot afford a mediator. An assistant that interviews each participant asynchronously, maps where people actually agree and disagree, and drafts candidate consensus statements for human sign-off.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Fast facilitation for communities that cannot afford a mediator. An assistant that interviews each participant asynchronously, maps where people actually agree and disagree, and drafts candidate consensus statements for human sign-off.

## 4.7: QALY for epistemics. Health economics got serious when the QALY gave decision-makers one comparable unit; epistemic interventions have nothing similar, so budgets go to whatever demos well.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
QALY for epistemics. Health economics got serious when the QALY gave decision-makers one comparable unit; epistemic interventions have nothing similar, so budgets go to whatever demos well. Design a candidate decision-quality metric and measurement kit, then stress-test it retroactively on documented decisions.

## 4.8: Procurement Gap Report. Legislative staff use personal AI accounts because official procurement cannot keep up.
Score: novelty=0 fit=0 cost=0 crowding=-1 → -1
Procurement Gap Report. Legislative staff use personal AI accounts because official procurement cannot keep up. Trace, at the document level, exactly which rules block a legislature from getting access to the best AI and decision-making tools.
