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
