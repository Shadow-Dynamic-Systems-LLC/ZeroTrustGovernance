# §10. Mechanistic Boundary (ZTG-1)

## Normative

A deterministic boundary MUST separate reasoning from irreversible action. The
boundary exists in code, not in policy interpretation, intent reconstruction, or
post-hoc evaluation. It is architectural rather than procedural. Its operation
does not depend on any property of the reasoning system whose outputs it gates.

No component within the governed system may bypass, reinterpret, defer, or
negotiate the boundary at runtime. The boundary is not a service the reasoning
system requests authorization from; it is the structural separation through
which the reasoning system's outputs must pass to become actions.

Authorization MUST occur before irreversible action. An architecture in which
actions execute speculatively and are evaluated for authorization in parallel,
with rollback if authorization fails, does not satisfy ZTG-1 for irreversible
actions. Speculative execution of irreversible actions is irreversible
execution.

No action derived from model output may execute without explicit structural
approval. Authorization is not inferred from context, derived from absence of
denial, or implied by continued operation. The architecture's default
disposition toward any model-derived action is refusal; authorization is the
explicit grant that converts refusal into permission.

Boundaries are code-enforced, not intent-interpreted. The architecture does not
reason about what the model meant, what a reasonable agent would do, or what the
model should be permitted to do given context. It evaluates the proposed action
against policies in effect and produces a deterministic decision.

### Boundary Composition

**With ZTG-0a (Observability).** The boundary's operation MUST be fully
observable. Every authorization decision — grant, refusal, and escalation alike —
is recorded with decision-level fidelity (inputs, policy version, identity,
decision-time, verdict, and action taken), and those records carry ZTG-0a's
intrinsic tamper-evidence. Recording only grants, or treating refusals as
unrecorded, does not satisfy ZTG-0a.

**With ZTG-0b (Replayability).** Boundary decisions MUST be replayable. Given the
same recorded inputs, the same policy version, and the same pinned
evaluation-engine semantics, the boundary MUST reproduce the same verdict. Replay
reconstructs the verdict and never re-emits the effect. Non-deterministic boundary
behavior violates ZTG-1.

**With ZTG-0c (Temporal Integrity).** Boundary decisions occur at a single
decision-time, established from a trusted time source the reasoning system does not
control, against a coherent point-in-time snapshot of governance state. The
boundary MUST NOT evaluate against stale policy, future state, or temporally
inconsistent inputs.

**With ZTG-0d (Identity Integrity).** Authorization at the boundary requires
attributable authority. Every recognized authorization traces, through its
delegation chain, to a human or institutional ratifying principal, bound by
non-repudiable, revocable credentials satisfying ZTG-0d. The reasoning system holds
no authorizing identity.

**With ZTG-0e (Governance Consistency).** The boundary MUST operate against a
single consistent view of governance state, agreed across enforcement points and
applied atomically. During governance-state inconsistency, the boundary MUST refuse
authorization.

### Memory Subsystem Interaction

Memory subsystems may inform boundary evaluation, but memory contents MUST NOT
bootstrap policy authority. Memory contents are inputs to evaluation, not
sources of additional policy.

The boundary MUST NOT recognize memory-resident content as authorizing,
declaring exceptions, or modifying policy. Memory-to-policy elevation is
governed by the relevant memory subsystem specification, outside ZTG. ZTG
specifies that elevation must occur through an explicit promotion protocol
rather than implicit interpretation.

This matters because memory contents are typically writable by the same model
whose outputs the boundary gates. Accepting memory-resident content as
authorizing creates a path for the model to author its own authorization.

### Boundary Scope

The boundary applies to all actions producing externally observable effects.
The scope includes obvious cases and less obvious cases:

- Reads from external systems whose access pattern itself signals the target.
- Internal state changes whose visibility extends beyond local reasoning scope.
- Resource consumption patterns observable beyond the reasoning system.
- Speech-to-user output where receipt of communication has consequences.
- Memory writes consulted by other systems.

Scope determination is conformance-relevant. An implementation enforcing the
boundary on only a subset of supported effectful actions does not satisfy ZTG-1.

### Boundary Integrity

The boundary's integrity requires:

- Boundary code separately auditable from reasoning-system code.
- Policy evaluation in a context the reasoning system cannot influence.
- Decision communication to the action surface through a channel the reasoning
  system cannot intercept or modify.
- Audit emission atomic with the decision through a path the reasoning system
  cannot affect.

The boundary is a separate architectural component, operating in isolation from
the reasoning it gates.
