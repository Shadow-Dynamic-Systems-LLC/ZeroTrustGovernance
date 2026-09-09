# §13. Evidence-Coupled Execution (ZTG-4)

## Normative

Every governed effect and its evidence MUST be atomically coupled: no effect may
occur without its evidence being durably committed, and no evidence of an effect may
exist without the effect having been dispatched. The evidence is a precondition of
the effect, not a record of it. The coupling MUST be enforced through a path the
reasoning system cannot influence.

### The Coupling Guarantee

The guarantee is bidirectional. In one direction, no effect without evidence: an
effect that reaches the world without durably committed evidence is a ZTG-4
violation, not a missing log entry. In the other, no evidence without effect:
evidence must correspond to a dispatched effect, so that the record cannot be
inflated with effects that did not occur. The two directions together make the
evidence and the effect a single coupled fact — they stand or fall together. An
auditor reading a coupled evidence record is reading proof that the effect occurred
under the recorded authorization, not a claim that happens to sit near the effect.

This is the precise content of "constitutive, not descriptive." A descriptive log
is written about an act that is already complete; its presence or absence does not
bear on whether the act was valid. Constitutive evidence is part of what makes the
act an authorized governed effect at all: the effect is not permitted to occur
except as the committing of its evidence, so an effect without evidence is not an
unlogged action but an unauthorized one. ZTG-4 moves governance evidence from the
first category to the second.

### Ordering: Evidence Before Effect

Perfect atomicity between a local evidence commit and an irreversible external
effect is not achievable, because the external world is not a transactional
participant the system can two-phase-commit. ZTG-4 does not pretend otherwise. It
specifies the achievable guarantee: durable evidence of the authorized effect MUST
be committed before the effect is dispatched, and the effect's completion MUST be
recorded after. This is the write-ahead discipline — intent is made durable before
the irreversible operation, so that the record is never behind the world.

The ordering yields a definite guarantee: no effect occurs whose authorizing
evidence was not already durably committed. It does not eliminate the failure
window between evidence commit and confirmed dispatch; it relocates the residual
uncertainty into a place where it is recorded rather than silent. A failure in that
window leaves durable evidence of an effect that was authorized and attempted but
whose completion is unconfirmed — an indeterminate effect, handled below — never an
effect with no evidence at all. The framework's honesty here is the point: it bounds
a known impossibility rather than claiming to have solved it.

### Indeterminate Effects

An effect whose coupling cannot be confirmed — the write-ahead failure window where
dispatch status is unknown, or any detected effect lacking committed evidence — is a
loss of the ZTG-4 guarantee and MUST be treated as an integrity violation in the
tamper family. Consistent with fail-closed semantics, an unreconciled indeterminate
effect is a Stasis (ZTG-2) trigger: the system holds rather than continuing to act
while the coupling between its effects and its evidence is in doubt. The
indeterminate effect MUST be reconciled — its true disposition established and
recorded — or its acceptance explicitly ratified by an authorized principal, before
normal operation resumes. The system does not silently absorb a coupling gap, and it
does not resolve one on its own authority.

The cost of an indeterminate effect tracks ZTG-5 harm class. An indeterminate
Restorable-class effect is a reconciliation task; an indeterminate Irreversible-class
effect is a serious condition, because the world may have changed in a way that
cannot be undone while the record of whether it did is incomplete. This is why the
write-ahead ordering and the narrowness of the failure window matter most for
high-harm-class surfaces, and why those surfaces warrant the highest-criticality
evidence.

### The ZTG-4 Evidence Record

The ZTG-4 evidence record is where the outputs of every other invariant and
prerequisite converge for a single effect. It MUST carry: the decision provenance
established by the prerequisites — verdict, policy version (ZTG-0b), decision-time
(ZTG-0c), and authorizing identity traced to its ratifying principal (ZTG-0d); the
harm-class classification and liability ceiling (ZTG-5); and the surface routing and
`reversal_strategy` (ZTG-3). Mitigable-class effects record residual harm, and
Irreversible-class and over-threshold effects produce the highest-criticality
records the substrate supports, per ZTG-5.

Because every invariant's output lands in this record, the coupled evidence is the
single artifact an auditor, a counterparty, or a court examines to see the whole
governance of an effect at once: that it was authorized, by whom, under what policy,
at what time, through which declared channel, at what harm class and ceiling, and
with what result. The convergence is not incidental; it is what makes a governed
effect accountable as a unit rather than as scattered fragments across subsystems.

### Division from Observability

ZTG-4 and ZTG-0a are distinct and neither discharges the other. ZTG-0a requires that
governance records be complete and tamper-evident: records that exist cannot be
silently altered, and governance-relevant events that produce no effect — refusals,
escalations, policy selection, identity validation — are recorded with integrity.
ZTG-4 requires that records of effects be coupled to those effects: the record exists
if and only if the effect does. A system could satisfy ZTG-0a's integrity and still
violate ZTG-4 — its existing records unforgeable, yet an effect having slipped to the
world with no record at all. It could satisfy ZTG-4's coupling for effects and still
owe ZTG-0a the integrity and completeness of its non-effect records. The two compose
to a single property — every governance fact is recorded, with integrity, and every
effect is bound to its record — but they are reached by different requirements, and
ZTG-4 is the effect-coupling half.

### Coupling Path Integrity

The coupling MUST be enforced on a path the reasoning system cannot influence,
consistent with ZTG-1's requirement that audit emission be atomic with the decision
through a channel the reasoning system cannot intercept or modify. A coupling the
governed system could sever — dispatching an effect while suppressing its evidence,
or emitting evidence for an effect it did not dispatch — would return the evidence to
the descriptive category and defeat the invariant. The evidence commit and the effect
dispatch are bound by the architecture, not by the cooperation of the system whose
effects are being recorded.

### Conformance Criteria

A conforming implementation can: demonstrate that no effect is dispatched before its
authorizing evidence is durably committed; demonstrate that no evidence of an effect
exists without a corresponding dispatch; produce the ZTG-4 evidence record with all
required prerequisite, ZTG-5, and ZTG-3 fields for every governed effect; detect
indeterminate effects and escalate unreconciled ones to Stasis; reconcile or obtain
ratified acceptance for indeterminate effects before resuming; demonstrate the
coupling path is not influenceable by the reasoning system; and demonstrate that its
ZTG-4 coupling and its ZTG-0a integrity are both satisfied without one being assumed
from the other.
