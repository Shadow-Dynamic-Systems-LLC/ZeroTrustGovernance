# §9. Governance Consistency (ZTG-0e)

## Normative

The boundary MUST operate against a consistent view of governance state, and
governance state MUST change only through atomic, authorized, ordered transitions.
When a consistent governance view cannot be established, the boundary MUST refuse.

Governance state is the complete set of governing inputs a decision is evaluated
against: policy versions, the identity and credential registry, the surface and
sub-surface registry, harm-class and ceiling declarations, and the configuration
of the governance substrate itself. ZTG-0e governs the coherence of this set as a
whole, across change and across enforcement points.

### Atomic and Complete Transitions

A change to governance state MUST apply atomically and completely. No decision may
be evaluated against a partially-applied change — a new policy version live for one
component but not another, a revoked credential removed from one registry view but
not the registry the boundary consults, a surface re-registered with a new
harm-class default while its old default still routes some effects. A decision
evaluated against a half-applied change is evaluated against a governance state
that the ratifying principal never authorized, because the authorized state is the
complete transition, not an intermediate of it.

This is the property a ZTG-0c point-in-time snapshot presupposes. ZTG-0c requires
each decision to be evaluated against a coherent temporal cut of governance state;
ZTG-0e is the requirement that such a coherent cut exists to be taken — that
governance state is never, from the boundary's perspective, caught mid-transition.

### Governance Change as a Governance Event

A change to governance state is itself a governed action. Every transition MUST be
authorized under ZTG-0d, recorded under ZTG-0a, and ordered under ZTG-0c. The
authority to change policy, alter a registry, adjust a ceiling, or reconfigure the
governance substrate traces to a ratifying principal exactly as the authority to
take any other governed action does, and the change is attributable to that
principal.

This is where the introduction's claim of *continuous* ratifying authority (§1, Foundational Commitments)
becomes checkable at the point of change rather than only at the point of action.
A governance change made without attributable authority is not a legitimate change
to the governing order; it is an unauthorized mutation of it, and ZTG-0e requires
that such a mutation be detectable rather than silently effective. The governing
order is not self-modifying; it is modified by authority, on the record, in order.

### Consistency Across Enforcement Points

Where governance is enforced at more than one point, all enforcement points MUST
agree on the governance version in effect for a decision. A decision proceeds only
under a governance view established as consistent across the points that bear on
it; where enforcement points diverge — different policy versions, disagreeing
registry state — the boundary MUST refuse rather than proceed under an
indeterminate view.

This is a strong-consistency requirement on the governance plane, and it is a
deliberate choice of consistency over availability when the two conflict. A system
that continued to authorize action while its enforcement points disagreed about
the governing rules would be permitting action under a governance state that does
not single-valuedly exist — precisely the window of inconsistently-governed action
ZTG-0e exists to foreclose. Eventual consistency, in which points may diverge and
later reconcile, is not sufficient for the governance plane, because reconciliation
after the fact does not retroactively govern the actions taken during divergence.
The availability cost of refusing under partition is the fail-closed posture the
framework adopts everywhere: when the system cannot establish that invariants hold,
it does not proceed.

### Governance of the Governance Substrate

The configuration of the governance substrate is itself governance state.
Changes to the observability substrate (ZTG-0a) — its retention policy, record
schema, integrity mechanism, and access configuration — and to the evaluation
machinery's configuration are governance-state transitions subject to this
chapter's requirements: authorized under ZTG-0d, recorded under ZTG-0a, ordered
under ZTG-0c, and consistency-governed under ZTG-0e. The machinery that governs is
not exempt from governance; an actor who could silently alter retention or access
to the evidence store could defeat the audit on which every other guarantee rests.

ZTG-0e establishes this principle and does not specify its full mechanism. The
detailed treatment — including how substrate self-governance avoids infinite
regress and where its bootstrap authority is rooted — is deferred. The
prerequisite-level requirement is that substrate configuration is inside the
governed perimeter, not outside it. This resolves the observability-of-the-observer
question raised and deferred in ZTG-0a.

### Conformance Criteria

A conforming implementation can: evaluate decisions only against a complete,
consistent governance state and demonstrate that no decision sees a partially-
applied transition; demonstrate that every governance-state transition is
authorized, recorded, and ordered; establish a consistent governance view across
enforcement points and refuse when consistency cannot be established; demonstrate
that divergence between enforcement points produces refusal rather than action
under an indeterminate view; and demonstrate that changes to the governance
substrate's own configuration are governed transitions, not ungoverned
infrastructure changes.
