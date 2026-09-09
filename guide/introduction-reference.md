# ZTG v1.0 — Introduction Reference

The introduction develops the framework's foundational positions through six
essays plus a scope section. Each essay opens with a deployment-relevant
question that helps institutional readers enter the argument.

## Reading This Specification

Zero Trust Governance specifies the architecture for governed autonomous
execution in AI systems. The introductory essays can be read in order or by
institutional question.

| Question | Essay |
|---|---|
| Why isn't our existing safety, security, or governance staffing catching AI failures? | §1.1 The Unified Substrate |
| Why does our current governance process feel inadequate when applied to AI? | §1.2 A New Mode of Governing |
| Should we invest in alignment research, or in governance architecture? | §1.3 Capability and Control: A False Choice |
| Doesn't adding inhibitory architecture reduce what our AI can do? | §1.4 Executive Function as Constitutive of Capability |
| If the principle is balance, why does ZTG advocate specifically for inhibitory architecture right now? | §1.5 The Current Asymmetry |
| Is ZTG a constraint on our AI deployment, or an enabler of it? | §1.6 The Capability Multiplier |

The body of the specification (§2 onward) presents the normative content: five
structural prerequisites (ZTG-0a through ZTG-0e), five system invariants (ZTG-1
through ZTG-5), the authorization model, composition requirements, and
conformance verification. The introduction grounds why the normative content
takes the shape it does.

## §1.1 The Unified Substrate

Deployment question: Why isn't our existing safety, security, or governance
staffing catching AI failures?

Core answer: the failures live in seams between AI Governance, AI Safety, and AI
Security. Each field's methodology is constituted by what it engages with and
what it defers. Seam failures are structurally invisible to the fields
individually.

ZTG proceeds from the premise that governance, safety, and security are views
onto a single substrate: the authorization architecture that determines what an
autonomous system can do, under what conditions, with what accountability.

The framework is not a refinement of existing governance, safety, or security
practice. It specifies the substrate those practices have been addressing in
fragments. The institutional response is not to add more staffing in any one
category; it is to operate at the substrate layer those categories address in
fragments.

## §1.2 A New Mode of Governing

Deployment question: Why does our current governance process feel inadequate
when applied to AI?

Core answer: current governance was designed for an operating regime with
self-limiting properties that AI breaks. Human-scale governance depended on
employment relationships, professional norms, slow action tempo, and inherent
legal accountability. AI systems operate without those self-limiting properties.

Real governance of AI systems requires mechanistic enforcement, deterministic
evaluation, structural binding between authorization and action, and evidence
that is constitutive rather than merely descriptive.

Institutions adopting this mode will find governance bodies operating more like
enforcers at the point of action than adjudicators reviewing prior action. The
authority of the ratifying officer is exercised continuously through the
architecture rather than periodically through assembly.

The framework cannot prevent institutions from choosing not to govern this way,
but it does not pretend the second choice constitutes governance.

## §1.3 Capability and Control: A False Choice

Deployment question: Should we invest in alignment research, or in governance
architecture?

Core answer: this is a false choice. Alignment operates in the Envelope; ZTG
governance operates in the Invariant.

| Property | Envelope Layer | Invariant Layer |
|---|---|---|
| Mechanism type | Non-deterministic / statistical | Deterministic / structural |
| Output character | Probabilistic improvement | Hard guarantee |
| Examples | Alignment training, RLHF, moderation filters, behavioral heuristics, instruction-tuning | Authorization gates, evidence chains, harm-class registration, ceiling enforcement, Stasis |
| Failure mode | Statistical degradation under distribution shift; out-of-distribution behavior; reward hacking | Categorical breach |
| Operates over | Reasoning, generation, output distribution | Effect surface; actions touching the world |
| Time of operation | Training, fine-tuning, runtime inference | Authorization-time, gate-time, evidence-emission-time |
| What it provides | Better behavior on average | Cannot-do guarantees regardless of behavior |
| Dependency relation | MAY depend on Invariant for bounded operating context | MUST NOT depend on Envelope |

The bottom row is load-bearing. Invariant guarantees that depend on Envelope
properties reduce to those properties' statistical character. Cannot-do
guarantees that reduce to probably-won't are not guarantees.

## §1.4 Executive Function as Constitutive of Capability

Deployment question: Doesn't adding inhibitory architecture reduce what our AI
can do?

Core answer: no. Executive function is not subtracted from capability; it makes
capability operative. Current AI deployments lack executive function, which
makes them less capable than they appear.

The clinical neuroscience and neuropsychology literature on executive function
and its failure modes grounds the point. Phineas Gage, frontal lobotomy
literature, Luria's neuropsychology, and Sperry's split-brain work each support
architectural specificity: preserved component abilities do not equal
operational capability when executive coordination and gating are damaged.

ZTG specifies the executive-function layer for artificial cognition. It is not
adding constraint; it is restoring the architecture required for capability.

## §1.5 The Current Asymmetry

Deployment question: If the principle is balance, why does ZTG advocate
specifically for inhibitory architecture right now?

Core answer: current deployments are at one specific failure mode of executive
function. They cluster at the under-strict, disinhibited failure mode.

Over-strict executive function produces deliberation and selection collapse.
Under-strict executive function produces local output without coherent
goal-advancement. Current AI deployments resemble the second failure mode:
generative capacity is high, while selection is left to Envelope mechanisms or
external human review.

Institutions rarely accidentally hyper-constrain deployments because the cost is
immediate and legible. Disinhibited deployments produce delayed, externalized
exposure. ZTG's advocacy reflects the current failure mode; it is not a
permanent preference for inhibition.

## §1.6 The Capability Multiplier

Deployment question: Is ZTG a constraint on our AI deployment, or an enabler of
it?

Core answer: enabler. Without executive function, AI is a candidate-generator
bottlenecked by human selection. With ZTG-conformant architecture, AI becomes an
operational capability.

ZTG automates the selection function along with generative work. Humans engage
at points the architecture routes to them: high-consequence decisions, edge
cases, and situations requiring institutional authority.

This is a different value proposition from "ZTG provides safety for your AI
deployment." It is "ZTG is what makes your AI deployment actually capable rather
than nominally capable but operationally bottlenecked."

## Scope of This Specification

ZTG specifies architecture for governed autonomous execution as a specific
instance of the more general structural problem of architecting interventions in
bound complex systems.

ZTG operates at the interaction layer between AI systems and institutional
structures. It is not a contribution to characterizing AI as an isolated system.

This specification specifies:

- Architecture for governed autonomous execution at the interaction layer.
- Structural prerequisites for the architecture to operate.
- Invariants the architecture must satisfy.
- Composition requirements for systems that compose with the architecture.
- Conformance verification for implementations.

This specification does not specify:

- Behavioral constraints on agent reasoning, output, or epistemic posture.
- Post-deployment behavioral envelope and drift measurement.
- Specific institutional adoption patterns.
- Substantive risk pricing of multipliers and ceilings.

The specification is open. Constable is the reference implementation built and
maintained by Shadow Dynamic Systems. Other implementations satisfying the
specified invariants and prerequisites are ZTG-conformant.

The normative content begins in §2.
