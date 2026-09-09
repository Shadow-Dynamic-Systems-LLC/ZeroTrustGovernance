# §5. Observability (ZTG-0a)

## Normative

All governance-relevant events MUST be recorded with sufficient fidelity to
support deterministic post-hoc audit. A governance-relevant event is any state
transition, decision point, boundary check, policy evaluation, authorization
grant, refusal, escalation, identity validation, time-source check,
surface-routing decision, Stasis entry or exit, harm-class assignment, liability
ceiling assignment, or evidence-record emission that bears on what the governed
system was permitted to do, under what conditions, and with what accountability.

Observability in ZTG-0a is not logging in the ordinary operational sense.
Operational logging serves debugging, performance analysis, and service health.
Governance observability serves audit, replay, and attribution. A system may
satisfy its operational logging needs completely and still fail ZTG-0a. The
distinguishing requirement is decision-level reconstruction: for any
governance-relevant event, the record MUST allow an authorized reviewer to
reconstruct what was evaluated, under which policy version, by what identity, at
what time, and with what result.

### Governance-Relevant Events

The class of events that MUST be observable is defined by governance relevance,
not by event volume or operational convenience. An implementation MUST be able to
enumerate the governance-relevant event types its architecture can produce and
demonstrate that each produces a record. At minimum the class includes:
authorization requests; boundary evaluations and their verdicts; policy-version
selection; identity validation; time-source checks; surface- and sub-surface
routing decisions; Stasis entry, exit request, and exit ratification; harm-class
and liability-ceiling assignment; evidence-record emission; input normalization;
and any promotion of memory content into policy-relevant input.

Grants and refusals are equally governance-relevant. An architecture that records
authorizations but not refusals does not satisfy ZTG-0a. Because the boundary's
default disposition toward any model-derived action is refusal (ZTG-1), refusals
are not an exceptional case to be sampled; they are the larger share of the
boundary's decisions and the share most diagnostic of its behavior under
pressure. Escalations MUST likewise be recorded, including the condition that
triggered the escalation and the authority to which it was routed.

### Fidelity Requirements

A governance record MUST carry enough information to reconstruct the decision it
documents without recourse to the live system. This includes, at minimum: the
event type; the invariant or prerequisite the event bears on; the policy version
in effect; the identity exercising or requesting authority; the time of the
event against a ZTG-0c-consistent time source; a representation of the inputs
evaluated, sufficient for ZTG-0b replay; and the verdict or resulting state
transition.

Aggregate operational metrics do not satisfy ZTG-0a. Counters, rates, and
dashboard summaries report how many events of a kind occurred; they do not permit
reconstruction of any individual decision. "How many actions were refused this
hour" is not a substitute for "why was this action refused." Metrics are a
permitted derived view computed downstream of the record substrate; they are
never a substitute for it. A conforming system retains decision-level records and
MAY compute metrics from them, not the reverse.

This requirement is a specific guard against constructed formalism: the
substitution of a measurable proxy for the thing it was meant to preserve.
Decision-level reconstruction is the thing; metrics are the proxy. ZTG-0a holds
the line at the thing.

### Completeness and Negative Space

Missing records are governance facts, not gaps in telemetry. An action path that
produces a governed effect with no corresponding observable record is a violation
of ZTG-0a, not merely a monitoring deficiency. Silence MUST NOT be read as
evidence of normal operation.

This is the property that makes the rest of the framework auditable, and it
depends on the recording of refusals established above. If a correct refusal
leaves a record, then the absence of any record on an action path is
distinguishable from a correct refusal, and absence can be treated as a
violation. If refusals were unrecorded, silent bypass and correct refusal would
be indistinguishable, and negative space would carry no information. A conforming
implementation MUST treat the absence of an expected record as a detectable
condition with defined consequences, rather than as ordinary missing data.

### Record Integrity

Observability requires integrity, not merely emission. A record that can be
altered or forged after the fact does not support audit; it supports a
reconstruction the system cannot vouch for. ZTG-0a therefore requires that
governance records be tamper-evident to a degree sufficient for auditability:
unauthorized alteration, deletion, or insertion of a record MUST be detectable.

This integrity requirement is intrinsic to ZTG-0a and is not deferred to ZTG-4.
ZTG-4 couples evidence to externally observable effects — it guarantees that an
effect and its evidence stand or fall together. But many governance-relevant
events produce no external effect: refusals, escalations, policy-version
selection, identity validation. ZTG-4's effect-coupling does not reach these,
yet ZTG-0a must keep their records trustworthy. Sourcing ZTG-0a's integrity from
ZTG-4 would also invert the framework's dependency order, in which invariants
depend on prerequisites and not the reverse. ZTG-0a owns record integrity; ZTG-4
owns the atomic binding of evidence to effect. The two cross-reference, and a
conforming system satisfies both, but neither requirement is discharged by the
other.

The integrity standard follows the introduction's load-bearing rule. A
governance guarantee that rests on a forgeable record reduces to a probabilistic
claim about whether the record is accurate. A cannot-have-been-altered property
that reduces to probably-was-not is not an integrity property.

### Privacy and Confidentiality

Operational evidence may contain sensitive data, and access to it may be
restricted. Confidentiality controls MUST NOT compromise record integrity,
completeness, or auditability. Confidentiality is an access-control property; it
governs who may read a record. It is not a license to omit.

An implementation MAY store sensitive payloads in protected form — encrypted or
vaulted, with access gated to authorized auditors — provided a cryptographic
digest of the protected content is bound into the tamper-evident record so that
the record's integrity and the payload's correspondence remain verifiable.
Permitted: protection that restricts access while preserving recoverability and
verifiability. Disallowed: redaction in the sense of omission, where an
authorized auditor or a ZTG-0b replay can no longer reconstruct the decision.

Deletion of inputs that are load-bearing for ZTG-0b replay — for example, under a
data-erasure obligation — sits at a genuine tension between confidentiality
regimes and replayability. ZTG-0a requires that any such deletion is itself a
recorded, attested governance event, so that a degraded record is a documented
and attributable state rather than a silent gap. The full resolution of how
erasure and replay fidelity compose belongs to ZTG-0b.

### Conformance Criteria

A conforming implementation can: enumerate its governance-relevant event types
and demonstrate record coverage for each; produce decision-level records for both
grants and refusals, and for escalations; demonstrate that aggregate metrics are
derived from, not substituted for, decision-level records; detect the absence of
an expected record and treat it as a violation rather than missing telemetry;
detect tampering with governance records; and demonstrate that confidentiality
controls restrict access without defeating audit or replay reconstruction.
