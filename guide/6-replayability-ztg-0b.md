# §6. Replayability (ZTG-0b)

Replayability is the second of the five structural prerequisites (ZTG-0a through
ZTG-0e). It is drafted after Observability (ZTG-0a) because it depends on it:
there is nothing to replay unless governance-relevant events were recorded with
sufficient fidelity. ZTG-0a establishes the recorded substrate; ZTG-0b
establishes that decisions can be deterministically reconstructed from it.

## Operational Questions

ZTG-0b is the prerequisite directly named by the **replayability** operational
question, and it is load-bearing for two others. It conditions **evidence
coupling** (ZTG-4): evidence that cannot be replayed documents that a decision
was made but cannot demonstrate that it was made correctly. And it conditions
**admissibility**: the convergence test and any external audit of a governed
decision rest on the ability to reconstruct that decision and obtain the same
verdict. A record that cannot be replayed is a claim; a record that replays is a
checkable fact.

## Further Considerations

**The control-theory grounding.** Control theory does not accept a controller
whose response to a given state cannot be reproduced. Reproducibility of the
control law is a precondition for verifying, tuning, or certifying a controller
at all: an actuator whose behavior cannot be reproduced under identical
conditions cannot be characterized, and an uncharacterizable controller cannot be
trusted with a process. Replayability is this property for governed autonomous
execution. It is what allows a governance decision to be examined as the output
of a definite procedure rather than as an unrepeatable event. Without it, the
governance function is observed but not verifiable — present in the record, but
not demonstrable as correct.

**Replay is reproduction, not re-litigation.** Replay reconstructs the verdict a
decision produced under the policy then in effect. It is not a re-decision under
current policy. Running an old decision against today's policy answers a
different and sometimes useful question — "what would we decide now" — but it is
not ZTG-0b replay and MUST NOT be confused with it. The value of replay is
precisely that it holds policy and engine fixed at their decision-time state;
substituting current policy discards the property that makes replay an audit of
what happened.

**Admissibility and the convergence test.** Replayability is what makes
governance evidence admissible rather than merely asserted. The convergence test
and external audit both depend on a third party being able to take the recorded
substrate and regenerate the verdict. A decision that replays is a decision an
auditor, a counterparty, or a court can independently check; a decision that
cannot be replayed is one they must take on trust. The framework's claim to
produce checkable governance, not just documented governance, rests on this
prerequisite.

**Engine longevity is a real cost.** Pinning evaluation-engine semantics across
the retention horizon of governance records imposes a genuine archival burden:
the implementation must preserve the ability to evaluate under engine versions
that may be years out of date. This is a deployment cost, addressed by engine
version archival, containerized evaluators, or semantic specifications precise
enough to re-implement. It is not a reason to weaken the requirement. A guarantee
of reproducibility that lapses when the engine is upgraded is not a guarantee of
reproducibility.

**Degraded records and audit honesty.** The `degraded-by-attested-deletion`
status is deliberately a first-class, visible state rather than a quiet failure.
Its purpose is to keep the record honest under legal regimes that compel
deletion: the system can comply with erasure and still tell an auditor exactly
which decisions can no longer be reconstructed and why. The alternative — letting
deleted inputs produce silent replay failures — would let genuine violations hide
among lawful deletions. Distinguishing the two is the point.

**Relationship to observability and to evidence coupling.** ZTG-0a records what
happened; ZTG-0b reconstructs it; ZTG-4 binds evidence to effects. The three are
ordered by dependency: coupling presupposes reconstruction presupposes recording.
ZTG-0b's fidelity demands flow back into ZTG-0a as requirements on what the record
must contain — inputs sufficient for replay, policy version, engine version — and
forward into ZTG-4 as the reason its coupled evidence is worth coupling.
