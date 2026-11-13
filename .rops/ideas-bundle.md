# Ideas bundle

## 1.6: Confidence Audit. Does the model know how solid its claims are? Calibration is already measured on cleanly resolvable questions (ForecastBench, consistency checks).
untested: no; budget: ?
Confidence Audit. Does the model know how solid its claims are? Calibration is already measured on cleanly resolvable questions (ForecastBench, consistency checks). Design a protocol that elicits a model's confidence in its own recommendations across domains where ground truth arrives later, then verify elicited confidence against outcomes.

## 1.2: Can you measure the gap between what a model implies and what it will defend (e.g. overselling, "flip-flopping", misrepresented evidence)?
untested: no; budget: ?


## 1.5: MisleadBench. Models can be technically accurate while leaving a false impression, and existing honesty benchmarks (MASK, DarkBench) mostly test single-turn lies.
untested: no; budget: ?
MisleadBench. Models can be technically accurate while leaving a false impression, and existing honesty benchmarks (MASK, DarkBench) mostly test single-turn lies. Build a multi-turn benchmark that first elicits what a model implies, then challenges it to defend the claim, scoring the gap between implied and defended positions, with a question-rotation protocol so scores stay meaningful.

## 1.7: FlipRate. A model that agrees with whoever pushed back last is useless for decisions.
untested: no; budget: ?
FlipRate. A model that agrees with whoever pushed back last is useless for decisions. Single-turn agreement is already measured (SycEval, ELEPHANT). Measure flip curves: how a model's answer and stated confidence change across one, two and three escalating rebuttals, separating warranted updating from capitulation.

## 1.8: Epistemic virtue eval suite. Forethought's collective-epistemics sketches propose evaluating calibration, honest uncertainty, manipulation resistance and claim-level scoring, but no maintained suite exists.
untested: no; budget: ?
Epistemic virtue eval suite. Forethought's collective-epistemics sketches propose evaluating calibration, honest uncertainty, manipulation resistance and claim-level scoring, but no maintained suite exists. Build them as Inspect tasks with transparent rubrics, run them across frontier models, and publish grader disagreements as part of the result.

## 2.1: Which source-reliability scoring techniques are hardest to cheat and easiest to audit?
untested: no; budget: ?


## 2.2: What minimal tamper-evident layer is missing from today's AI observability standards, so that records of what agents did and agreed can be audited and trusted?
untested: no; budget: ?


## 2.4: What fraction of a real domain's content (e.g. council minutes, health advice, financial news) can be automatically bound to checkable evidence today?
untested: no; budget: ?


## 3.2: What does a chatbot say to someone mid-dispute, and how often does it escalate rather than de-escalate?
untested: no; budget: ?


## 3.5: Dispute Escalation Benchmark. When someone describes a conflict with their landlord, employer or ex-partner, does the chatbot steer them towards repair or escalation (evidence this is a live harm)? Build realistic dispute scenarios, ask practising mediators to define graded good advice, and score frontier models after every release.
untested: no; budget: ?
Dispute Escalation Benchmark. When someone describes a conflict with their landlord, employer or ex-partner, does the chatbot steer them towards repair or escalation (evidence this is a live harm)? Build realistic dispute scenarios, ask practising mediators to define graded good advice, and score frontier models after every release.

## 4.1: What is this field's equivalent of the QALY: a defensible, comparable unit for "decision quality improved"?
untested: no; budget: ?


## 4.10: A wish registry for privacy-preserving matchmaking. Participants privately register offers and needs; an AI matcher reveals a connection only when both sides' criteria are met, with logs auditable by a neutral steward.
untested: no; budget: ?
A wish registry for privacy-preserving matchmaking. Participants privately register offers and needs; an AI matcher reveals a connection only when both sides' criteria are met, with logs auditable by a neutral steward.

## 4.4: Using only data downloadable this weekend, what can you measure about a live epistemic deployment, and what does that mean for the field?
untested: no; budget: ?


## 4.9: Do their numbers match? Pair quantitative claims from parliamentary transcripts and press releases with the statistical releases they cite, flag mismatches with links to primary sources, and publish as an auditable open dataset.
untested: no; budget: ?
Do their numbers match? Pair quantitative claims from parliamentary transcripts and press releases with the statistical releases they cite, flag mismatches with links to primary sources, and publish as an auditable open dataset.

## 1.1: Does the model understand how solid its claims are? Can you accurately measure its confidence in a decision and verify that against reality?
untested: no; budget: ?


## 1.3: Which model behaviours matter for real decision quality, and does ranking well on an honesty benchmark predict better decision-making?
untested: no; budget: ?


## 1.4: What does a benchmark need to stay meaningful over time? Which exploits make benchmarks gameable, and can you demonstrate and close one?
untested: no; budget: ?


## 1.9: Article 5 measurement protocol. The EU AI Act bans manipulative and deceptive AI techniques, yet regulators have no agreed test procedure.
untested: no; budget: ?
Article 5 measurement protocol. The EU AI Act bans manipulative and deceptive AI techniques, yet regulators have no agreed test procedure. Draft a protocol mapping DarkBench and MASK-style measurements onto Article 5(1)(a) legal language, with worked examples and thresholds.

## 2.3: When an AI system uses a reliability or provenance tool, does its behaviour and accuracy actually improve?
untested: no; budget: ?


## 2.5: Track-Record Ledger. Pundits, forecasters and outlets make checkable public claims, but nobody keeps score in a form software can consume (Community Notes is the closest thing).
untested: no; budget: ?
Track-Record Ledger. Pundits, forecasters and outlets make checkable public claims, but nobody keeps score in a form software can consume (Community Notes is the closest thing). Build a public API that records dated claims, resolves them against primary sources, and serves reliability summaries per source, plus a first consumer: a browser extension or feed-reader plugin showing a source's track record beside their latest claim.

## 2.6: Tamper-Evident Action Recorder. When an AI agent takes a consequential action, the operator's own logs are the only record, and they can be edited.
untested: no; budget: ?
Tamper-Evident Action Recorder. When an AI agent takes a consequential action, the operator's own logs are the only record, and they can be edited. An example project here could be to build a signed, secure logging layer on the OpenTelemetry GenAI conventions so instrumented agent frameworks emit append-only, verifiable traces (Certificate Transparency is the precedent), plus a viewer for auditors.

## 2.7: Citation Binder. A large share of citations in papers, briefs and Wikipedia articles do not support the sentence they are attached to.
untested: no; budget: ?
Citation Binder. A large share of citations in papers, briefs and Wikipedia articles do not support the sentence they are attached to. Build a tool that locates each cited source and verifies whether it genuinely supports the specific claim, with per-citation verdicts and quoted passages (evaluation data exists: AVeriTeC).

## 2.8: Provenance Study. Everyone assumes provenance and reliability metadata will help AI systems behave better; nobody has measured it.
untested: no; budget: ?
Provenance Study. Everyone assumes provenance and reliability metadata will help AI systems behave better; nobody has measured it. Run a controlled experiment: the same research tasks with and without machine-readable signals (C2PA manifests, track records, Community Notes context), measuring accuracy, citation quality and susceptibility to planted false sources. Users: agent-framework developers deciding whether consuming signals is worth the cost.

## 3.1: Does advice users act on lead to choices they later endorse, and can you measure whether there is a gap?
untested: no; budget: ?


## 3.3: For a decision type (e.g. job offers, leases), does a briefing surface the considerations that actually matter, and how would you know?
untested: no; budget: ?


## 3.4: When a group compares its beliefs or forecasts, does surfacing the inconsistencies and cruxes change the decision?
untested: no; budget: ?


## 3.6: Decision-Brief Rubric. Use expertise in, for example, financial-guidance, careers or health charities to define a rubric, then build a grading harness scoring chatbot briefings against it.
untested: no; budget: ?
Decision-Brief Rubric. Use expertise in, for example, financial-guidance, careers or health charities to define a rubric, then build a grading harness scoring chatbot briefings against it.

## 3.7: Crux Mapper. Groups argue past each other because nobody knows which factual questions actually divide them.
untested: no; budget: ?
Crux Mapper. Groups argue past each other because nobody knows which factual questions actually divide them. Run short asynchronous AI interviews with each member, extract claims and probabilities, and render a disagreement map showing shared ground, genuine cruxes and internal inconsistencies (cf. the Habermas Machine, which drafts agreement; this maps disagreement).

## 4.2: Which specific certification, budget and approval chokepoints keep official AI tools out of legislatures while staffers use personal accounts?
untested: no; budget: ?


## 4.3: Why do institutions ignore forecasts they asked for: access and legibility, or the accountability that explicit predictions create?
untested: no; budget: ?


## 4.5: Scenario planning on tap for resilience teams. Run hundreds of LLM narrative simulations & forecasts from a plain-language situation brief and report recurring failure points in the two-page format emergency planners already use.
untested: no; budget: ?
Scenario planning on tap for resilience teams. Run hundreds of LLM narrative simulations & forecasts from a plain-language situation brief and report recurring failure points in the two-page format emergency planners already use.

## 4.6: Fast facilitation for communities that cannot afford a mediator. An assistant that interviews each participant asynchronously, maps where people actually agree and disagree, and drafts candidate consensus statements for human sign-off.
untested: no; budget: ?
Fast facilitation for communities that cannot afford a mediator. An assistant that interviews each participant asynchronously, maps where people actually agree and disagree, and drafts candidate consensus statements for human sign-off.

## 4.7: QALY for epistemics. Health economics got serious when the QALY gave decision-makers one comparable unit; epistemic interventions have nothing similar, so budgets go to whatever demos well.
untested: no; budget: ?
QALY for epistemics. Health economics got serious when the QALY gave decision-makers one comparable unit; epistemic interventions have nothing similar, so budgets go to whatever demos well. Design a candidate decision-quality metric and measurement kit, then stress-test it retroactively on documented decisions.

## 4.8: Procurement Gap Report. Legislative staff use personal AI accounts because official procurement cannot keep up.
untested: no; budget: ?
Procurement Gap Report. Legislative staff use personal AI accounts because official procurement cannot keep up. Trace, at the document level, exactly which rules block a legislature from getting access to the best AI and decision-making tools.

## Winning traits
# What 2026 placed entries had in common (from PLAYBOOK.md §4)

- W1 The title states the finding.
- W2 A positive control and a negative or decoy control, both reported in Results.
- W3 An intervention arm (change something, measure the effect), reported whatever it shows.
- W4 An attempt to break your own instrument: an attack, a decoy, or decisions sealed before unblinding.
- W5 Ground truth that is not an unvalidated LLM judge; judge agreement with hand labels when a judge is used.
- W6 A decision rule frozen before the held-out data.
- W7 Claims sized to the evidence; one number with its scale in the abstract.
- W8 A usable artefact for a named user (a rule, a recipe, a standard, a dataset).
- W9 AI use and pre-sprint work disclosed.

## Team profile
strengths: detect, evidence, audit, confound, calibrat, baseline, monitor, decoy, false
avoid: residual-stream or probe work when the sprint is about behaviour; parameter sweeps across model sizes; two entries in one sprint
- stopped at measurement with no intervention arm (Aug, Jun)
- abstract claimed more than the paper showed (Jul x2, Sep)
- known confound left untested before writing the headline (Sep token cap, Jul audit comparison)
- methods described the plan, not the run (Sep)
- missing prereg and code links (Aug, Sep)
- prose read as LLM-written (Aug)

Propose, for each of the top three questions by score, two question
cards in QUESTION.md `key: value` format, each with an intervention
arm, a decoy control and a positive control.
