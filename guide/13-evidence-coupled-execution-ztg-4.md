# §13. Evidence-Coupled Execution (ZTG-4)

Evidence-Coupled Execution is the fourth system invariant (ZTG-1 through ZTG-5).
It is where the framework's claim that governance evidence is *constitutive* rather
than *descriptive* (§1.2) becomes a structural requirement, and where the division
established in ZTG-0a — that observability owns record integrity while ZTG-4 owns
the binding of evidence to effect — lands. ZTG-3 enumerates the channels through
which effects reach the world and routes authorized actions to them; ZTG-4 requires
that each such effect and its evidence are coupled so tightly that neither can exist
without the other.

## Operational Questions

ZTG-4 is the invariant mapped most directly to **evidence coupling**, and it
completes the **replayability** chain: the prerequisites make a decision recorded,
reproducible, anchored, and attributed, and ZTG-4 guarantees that the effects those
decisions produce cannot escape the record. It also underwrites **admissibility**.
Evidence that an effect occurred is admissible as proof of governance only if it is
bound to the effect rather than asserted alongside it — a log that *says* an effect
was authorized, but that could exist whether or not the effect happened and whether
or not it was authorized, proves nothing. ZTG-4 is the requirement that makes the
evidence load-bearing.

## Further Considerations

**The transaction-systems grounding, and its honesty about limits.** Database
systems solved durable, recoverable state change decades ago, and ZTG-4 adopts their
core mechanism: write-ahead logging, in which a durable record of an intended change
is committed before the change is performed, so that recovery can always reconstruct
what was in flight. But database systems also established the limits of atomicity.
Atomic commit across multiple independent participants requires those participants to
cooperate in a commit protocol, and the foundational impossibility results —
two-generals, and the broader limits on agreement over unreliable channels — show
that perfect agreement with a party you neither control nor can assume will respond
is unattainable. The external world an irreversible effect touches is exactly such a
party. ZTG-4's design is what these two results jointly license: write-ahead gives a
one-sided guarantee (the record is never behind the world), and the residual
two-sided uncertainty is bounded and made explicit as the indeterminate-effect case
rather than wished away. A framework that claimed perfect effect/evidence atomicity
would be claiming to have refuted an impossibility result; ZTG-4 instead takes the
strongest guarantee the result permits and is honest about the remainder.

**The constitutive-evidence grounding, convergent with it.** Law has long
distinguished evidence that describes an act from evidence that constitutes it. Most
records are descriptive: they document a transaction that is already complete and
valid without them. But some formalities are constitutive — a deed that must be
recorded to convey, an instrument that must be written and signed to be enforceable,
a notarization without which the act has no legal effect. For these, the record is
not proof of a valid act; it is a condition of the act's validity. ZTG-4 places
governance evidence in this second category by construction: the effect has no
sanctioned existence except as the committing of its evidence. That a transaction-
systems tradition (reasoning about durability and recovery) and an evidentiary-law
tradition (reasoning about what makes an act valid) converge on the same structure —
the record precedes and conditions the act rather than following and describing it —
is the cross-tradition agreement the framework treats as evidence the requirement is
structural rather than stylistic.

**Why coupling, not just logging, is the requirement.** It is tempting to think
thorough logging achieves what ZTG-4 asks. It does not, and the gap is the whole
point. Logging is descriptive and severable: a system that logs its effects can, by
failure or by design, perform an effect and not log it, or log an effect it did not
perform, and nothing in the logging discipline forbids it. The disinhibited
deployments the introduction describes (§1.5) typically log copiously and govern
nothing, because the log is downstream of the act and optional to it. Coupling
inverts the relationship: the evidence is upstream of the act and necessary to it.
The difference between a system that logs and a system that couples is the difference
between one that can tell you what it did when it chooses to and one that cannot act
except by recording that it did.

**Reconciliation is a governed activity, not a cleanup.** Establishing the true
disposition of an indeterminate effect — did the irreversible email send or not —
often requires querying the external system the effect touched, and that query and
its result are themselves governance-relevant. Reconciliation is therefore not an
out-of-band repair but a governed activity that produces its own evidence and, where
it changes the recorded disposition of an effect, does so as an attributed, recorded
act. The framework does not let the resolution of a coupling gap be the one
ungoverned moment in the system.

**Relationship to replay.** ZTG-0b reconstructs the verdict of a decision; ZTG-4
guarantees the effect that followed the verdict is bound to the record ZTG-0b
replays. Read together they close the loop from decision to effect: the decision is
reproducible, and the effect is coupled to the reproduced decision, so the entire
arc — what was decided, and what was done about it — is both reconstructable and
non-severable. Replay never re-emits effects (ZTG-0b), so the coupled effect record
is examined, never re-performed.

## How We Do It (Constable reference implementation — non-normative)

Constable implements ZTG-4 by committing effect evidence to the Monotonic Logger
before dispatching the effect through the ZTG-3 surface, and by holding on any
effect whose coupling it cannot confirm.

**Write-ahead to the Monotonic Logger.** For every authorized effect, Constable
commits the ZTG-4 evidence record durably to the Monotonic Logger before the effect is
dispatched. The record carries the decision provenance, the ZTG-5 harm class and
liability ceiling, and the ZTG-3 surface routing and reversal strategy. Only after
the evidence is durably committed is the effect dispatched through the registered
surface; the dispatch and its result are then recorded (`EVIDENCE_APPENDED`,
`EFFECT_DISPATCHED`). The agent runtime has no path to dispatch an effect that
bypasses this ordering.

**Critical-class records for high harm class.** Irreversible-class and over-threshold
effects (ZTG-5) are written as the highest-criticality records the Logger supports,
with the durability and integrity guarantees those classes require, before dispatch.
The narrowness of the write-ahead window is most rigorously enforced where harm class
is highest.

**Indeterminate-effect handling.** If Constable cannot confirm that an effect's
evidence was committed and the effect dispatched as a coupled pair — a failure in the
write-ahead window, or a detected effect without a committed record — it marks the
effect indeterminate and enters Stasis (ZTG-2). Resolution runs as governed
reconciliation: the disposition of the effect is established, often by querying the
target surface, and recorded; or an authorized principal ratifies acceptance of the
indeterminate state via HumanSeal. Normal operation resumes only after reconciliation
or ratified acceptance.

**Coupling path isolation.** The evidence-commit-then-dispatch sequence executes in
the gate and surface mechanism, structurally separated from the agent runtime, so the
agent can neither dispatch an effect while suppressing its evidence nor emit evidence
for an effect it did not dispatch. The coupling is a property of the architecture, not
of agent cooperation.

**Conformance tests.** Constable's internal testing for ZTG-4 includes: ordering
tests confirming no effect dispatches before durable evidence commit; orphan tests
confirming no effect-evidence exists without a dispatch; crash-injection tests in the
write-ahead window confirming the result is a recorded indeterminate effect and Stasis,
never a silent gap; evidence-record tests confirming all prerequisite, ZTG-5, and
ZTG-3 fields are present; reconciliation tests confirming indeterminate effects are
resolved as governed, recorded activity; division tests confirming ZTG-4 coupling and
ZTG-0a integrity are independently satisfied; and isolation tests confirming the agent
cannot sever the coupling. The protocol is documented in the conformance verification
specification referenced in §22.
