# §5. Observability (ZTG-0a)

Observability is the first of the five structural prerequisites (ZTG-0a through
ZTG-0e). It is drafted first because it is upstream of every later invariant:
ZTG-1 boundary decisions, ZTG-2 Stasis events, ZTG-3 surface registry
declarations, ZTG-4 evidence-coupled effects, and ZTG-5 harm-class provenance all
presuppose that governance-relevant events are recorded with sufficient fidelity
to be examined after the fact.

## Operational Questions

Of the seven operational questions the framework answers, ZTG-0a is the
substrate beneath two: **replayability** and **evidence coupling**. Neither is
meaningful without it. A decision cannot be replayed (ZTG-0b) if the system did
not record what it decided and against what inputs. An effect cannot be coupled
to evidence (ZTG-4) if the evidence is not produced and retained in a form that
survives examination. ZTG-0a does not itself deliver replayability or coupling;
it establishes the recorded substrate those invariants operate on. It also
conditions a third question — **override visibility** — because an override that
is not observed cannot be attributed.

## Further Considerations

**Observation is not governance.** Observability is a prerequisite for
governance, not an instance of it. Recording an action does not bind it.
Monitoring that reports what a system did, after it did it, is the retrospective
posture the introduction identifies as inadequate for AI operating tempo (§1.2).
ZTG-0a exists so that the binding decisions made at the boundary (ZTG-1) and the
gates (ZTG-5) can be audited, replayed, and attributed — not so that observation
can stand in for binding. A reviewer who can see everything and bind nothing is
the failure mode this prerequisite serves to avoid, not the goal it serves to
reach.

**The cybernetic grounding.** Observability is the framework's feedback channel,
and cybernetics treats feedback as constitutive of regulation rather than
additional to it. A controller acting on a system without feedback at the
resolution of the variable it regulates is not regulating; it is operating
open-loop and hoping. This is why decision-level fidelity, not aggregate metrics,
is the conformance standard: a regulator fed only summary statistics has feedback
at the wrong resolution for the decisions it must govern. Ashby's requisite
variety makes the same point from the other side — a regulator must command
variety at least equal to the disturbances it controls, and a record that
collapses distinct decisions into a count has discarded exactly the variety the
governance function needs. ZTG-0a specifies the feedback path that closes the
loop the rest of the architecture depends on.

**Auditability and institutional accountability.** The introduction grounds
governance in the continuous authority of a ratifying officer (§1.2). That
authority is only reviewable if the system records how the officer's policies
actually operated — which actions they admitted, which they refused, and under
which version of policy. Without observability, institutional authority over an
autonomous system is asserted but not attributable: there is no record connecting
an outcome to the policy and identity that produced it. Observability is what
makes the ratifying officer's authority an auditable fact rather than a nominal
claim.

**Dashboard sedation.** High-level operational presentation can manufacture calm
while unresolved governance conditions persist beneath it. A dashboard that
renders refusals as a smooth low line, or aggregates escalations into a healthy
green tile, can suppress operator urgency precisely when attention is most
warranted. This is the constructed-formalism risk in operational dress: the
comfort of the summary replaces the signal it was meant to convey. ZTG-0a's
fidelity requirement is partly a defense against this — observability must
preserve signal, not operator comfort — but the chapter does not specify operator
interface behavior, which is a deployment concern.

**Evidence volume and evidence confidentiality.** Decision-level fidelity across
every governance-relevant event produces large, and often sensitive, evidence
stores. This is a real operational cost, and it is not a reason to weaken ZTG-0a.
The framework does not soften a conformance requirement to fit institutions not
yet ready to operate it. Volume is addressed by deployment-level retention,
tiering, and storage architecture; sensitivity is addressed by the
protect-don't-omit discipline above. Neither is addressed by recording less.

**Relationship to replayability.** Observability and replayability are
co-required but distinct. Observability records what happened with enough
fidelity to examine it; replayability (ZTG-0b) requires deterministic
reconstruction of a decision from those records. Observability is necessary for
replayability and does not guarantee it: a record can be complete and faithful
and still fail to replay if the decision procedure was non-deterministic. ZTG-0a
establishes the substrate; ZTG-0b establishes the reconstruction. The fidelity
fields ZTG-0a requires — inputs sufficient for replay, policy version, time — are
the interface between the two.

**Observability of the observer.** A governance record substrate is itself part
of the governed system, and changes to it — retention policy changes, schema
changes, access-grant changes to the evidence store — are governance-relevant.
An implementation should determine whether and how operations on the
observability substrate are themselves observed, and document the determination
as part of conformance. This chapter does not fully specify the recursion; it
flags it.

## How We Do It (Constable reference implementation — non-normative)

Constable implements ZTG-0a as an append-only governance evidence substrate that
every governance-relevant component writes to, structurally separated from the
agent runtime so that the recorded subject cannot edit the record.

**Authorization and Effect Record.** Constable records governance events into a
monotonic evidence substrate. Each record carries event type, the invariant or
prerequisite tag it bears on, policy version, identity, a ZTG-0c-consistent
timestamp, an input digest, the output verdict, residual-harm and
liability-ceiling fields where ZTG-5 applies, and correlation identifiers linking
the records of a single authorization across components. The input digest, rather
than raw input, is what binds into the chain by default; protected payloads are
stored separately and referenced by digest, satisfying the protect-don't-omit
discipline.

**Event taxonomy.** Constable's governance event types include, at minimum:
`AUTHORIZATION_REQUESTED`, `BOUNDARY_EVALUATED`, `AUTHORIZATION_GRANTED`,
`AUTHORIZATION_REFUSED`, `AUTHORIZATION_ESCALATED`, `POLICY_VERSION_SELECTED`,
`IDENTITY_VALIDATED`, `TIME_SOURCE_CHECKED`, `SURFACE_ROUTE_SELECTED`,
`STASIS_ENTERED`, `STASIS_EXIT_REQUESTED`, `STASIS_EXIT_RATIFIED`,
`EVIDENCE_APPENDED`, `EFFECT_DISPATCHED`, `HARM_CLASS_ASSIGNED`,
`LIABILITY_CEILING_ASSIGNED`, `INPUT_NORMALIZED`, and
`MEMORY_PROMOTION_REFERENCED`. The taxonomy is maintained so that every action
path through the gate maps to a coverage expectation, making negative space
testable.

**Monotonic Logger integration.** The substrate is an append-only,
tamper-evident record chain. Records are hash-linked so that alteration,
deletion, or insertion is detectable, satisfying ZTG-0a's intrinsic integrity
requirement independently of ZTG-4's effect-coupling. High-consequence events —
Irreversible-class and over-threshold authorizations per ZTG-5 — are written as
critical-class records. The Logger's integrity is a ZTG-0a property; its atomic
coupling of an effect to its evidence, where an effect occurs, is the ZTG-4
property. Constable satisfies both through the same substrate but does not
conflate the requirements.

**Airlock and Memoria signals.** Airlock emits input-normalization evidence
(`INPUT_NORMALIZED`) so that the inputs a policy evaluated are reconstructable.
Memoria emits promotion evidence (`MEMORY_PROMOTION_REFERENCED`) whenever memory
content becomes policy-relevant input, preserving the ZTG-1 requirement that
memory-to-policy elevation occur through explicit, attested promotion rather than
implicit interpretation — and making that elevation observable.

**Operator views.** HumanSeal surfaces observability to operators. The UI is
constructed to avoid converting unresolved conditions into ambient calm:
escalations and refusals under pressure are surfaced rather than aggregated away.
Operator presentation is derived from the decision-level substrate; it is never
the system of record.

**Conformance tests.** Constable's internal testing for ZTG-0a includes:
event-coverage tests asserting every action path produces its expected records;
negative-path tests asserting refusals and escalations are recorded with
reconstruction-sufficient fidelity; tamper tests asserting that altered, deleted,
or inserted records are detected; gap tests asserting that a missing expected
record triggers violation handling rather than passing silently; and
metric-derivation tests asserting that operator metrics are computed from, and
reconcile against, the decision-level records. The protocol is documented in the
conformance verification specification referenced in §22.
