# §14. Irreversibility of Harm (ZTG-5)

## Normative

Every governed action MUST be classified by the restorability of the harm it
produces, and that classification MUST govern the action's gate, its liability
ceiling, and the criticality of its evidence. Classification is over harm, not over
the action, and the availability of forward remediation does not lower it.

### Harm Classification

Every governed action MUST carry one of three harm classes:

- `Restorable` — affected parties can be returned to a materially equivalent state
  by an action available to the system.
- `Mitigable` — affected parties cannot be returned to the equivalent prior state,
  but harm can be reduced by a defined forward action.
- `Irreversible` — no available forward action reduces harm to the Mitigable class.

Classification is over the harm, not over the action that produces it. Two actions
with identical mechanics may carry different harm classes because their
consequences in the world differ, and the same action may be reclassified as its
consequences change. Critically, forward remediation mechanisms — refund,
retraction, settlement, compensation — do not by themselves lower harm class. A
harm is not Restorable because money can be offered for it; it is Restorable only
if the affected party can actually be returned to a materially equivalent state.
This distinction is the load-bearing one in the whole invariant: it refuses the
move, common in disinhibited deployments, of treating the availability of
after-the-fact compensation as if it made an irreversible act reversible.

### Harm-Class Declaration on Surfaces

Harm-class declarations attach to the enumerated surfaces and sub-surfaces of
ZTG-3 at registration, not to individual actions chosen by the governed system. A
sub-surface declaration may tighten its surface's default — declaring a higher harm
class — but MUST NOT relax it. Attaching the classification to the declared channel
rather than to the model-proposed act is what keeps harm class a governed property:
the system proposes an action and routes it through a surface, but the harm class
the action carries is a property of that surface, registered and changed under
governance (ZTG-0e), not a label the system assigns to its own act. ZTG-3 owns the
enumeration and closure of surfaces; ZTG-5 owns what the harm-class declaration on
them means and how it propagates.

### Liability Ceilings

Each authorization request carries a liability ceiling, and the ceiling MUST appear
in the ZTG-4 evidence record for the action. Ceilings are policy-assigned: the
system never originates ceiling authority, exactly as it originates no other
authority (ZTG-0d). A ceiling is the policy-set bound on the exposure an action is
permitted to carry, and it is set by the ratifying principal's policy, not derived
by the system from its own assessment of what it should be allowed to risk.

### Compositional Multipliers and Banded Algebra

Each surface declares a compositional multiplier, and composite assessment is the
product of component assessments and surface multipliers. Composition is recursive,
so assessment grows faster than linearly across extended action sequences: a long
chain of individually-modest actions can compose into a high composite assessment,
which is the intended behavior, because extended autonomous sequences accumulate
exposure that no single step reveals.

Assessments MUST be expressed in discrete, deterministic bands. Continuous-valued
assessments are disallowed, because floating-point and implementation-dependent
variation in a continuous assessment would make the same action assess differently
across conforming implementations and across time — which would violate ZTG-0b
replayability. The banding is not a loss of precision to be apologized for; it is
the form an assessment must take to be reproducible, and reproducibility is the
precondition for the assessment being auditable at all.

### Gate Selection

Gate selection follows from harm class and computed composite assessment, and
either condition alone is sufficient to promote an action to the high-end gate:

- An Irreversible-class action routes to the high-end gate regardless of its
  computed assessment.
- An over-threshold computed assessment routes to the high-end gate regardless of
  harm class.

Elevated gates MUST be architecturally distinct, not the same gate running
conditional additional checks. A high-end gate that is the ordinary gate "with more
validation turned on" shares the ordinary gate's failure modes and its bypass
surface; the requirement that elevated gates be distinct structures is what makes
promotion mean something stronger than a longer checklist. This composes with
ZTG-1: speculative execution, where permitted at all, is confined to Restorable-class
actions below the promotion threshold, because a speculatively-executed
Irreversible action is simply an Irreversible action.

### Evidence Record Requirements

The ZTG-4 evidence record for every governed action MUST carry its harm-class
classification and its liability ceiling. In addition: Mitigable-class actions MUST
record their residual harm — the harm that remains after the defined forward
mitigation — and Irreversible-class and over-threshold actions MUST produce the
highest-criticality audit records the substrate supports. The gravity of the record
tracks the gravity of the consequence, so that the evidence an institution holds for
its most consequential actions is its most durable and most tamper-resistant.

### Orthogonality to ZTG-3 reversal_strategy

ZTG-5 harm class is orthogonal to the ZTG-3 `reversal_strategy`, and both fields
MUST be present in decision provenance. The `reversal_strategy` describes what the
system can undo or compensate; the harm class describes the consequence in the
world. They are independent: a surface may have a capable reversal strategy and an
Irreversible harm class, and when it does, the action is gated by its harm class and
not rescued by its reversal strategy. Recording both, side by side, is what lets an
auditor confirm that the reversal strategy was not quietly used to discount the harm
class — the same non-relaxation discipline ZTG-3 states from its side.

### Conformance Criteria

A conforming implementation can: assign one of the three harm classes to every
governed action by the restorability of its harm, independent of available
remediation; attach harm-class declarations to ZTG-3 surfaces with monotonic
sub-surface tightening; carry a policy-assigned liability ceiling into the ZTG-4
evidence record; compute composite assessment as a recursive product in discrete
deterministic bands that replay identically; promote to an architecturally distinct
high-end gate on either Irreversible class or over-threshold assessment; record
residual harm for Mitigable actions and highest-criticality evidence for
Irreversible and over-threshold actions; and carry both harm class and
`reversal_strategy` in provenance without the latter relaxing the former.
