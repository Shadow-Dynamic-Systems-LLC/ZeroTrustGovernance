# §6. Replayability (ZTG-0b)

## Normative

Every governance decision MUST be deterministically reconstructable from its
recorded substrate. Given the recorded inputs, the policy version in effect, and
the evaluation-engine semantics under which the decision was made, replay MUST
produce the same verdict the system produced at decision-time. Replay that
produces an equivalent-but-different verdict does not satisfy ZTG-0b; the
requirement is reproduction of the verdict, not approximation of it.

Replayability is a property of the Invariant decision procedure, not of the
reasoning system whose outputs that procedure governs. The reasoning system is
non-deterministic and is not required to be replayable. ZTG-0b requires that the
deterministic evaluation the boundary performs over recorded inputs reproduces
exactly.

### The Decision Procedure

Deterministic reproduction requires that the entire decision procedure be
reconstructable, not only its inputs. A governance decision is a function of
three things: the recorded inputs, the policy version in effect, and the
semantics of the evaluation engine that applied that policy to those inputs. All
three MUST be recoverable for a decision to be replayable.

Recording inputs and policy version while allowing the evaluation engine to drift
does not satisfy ZTG-0b. A policy text evaluated under a later engine version may
yield a different verdict for reasons unrelated to any governance decision —
changed evaluation order, altered numeric handling, modified built-in semantics.
An implementation MUST therefore pin or otherwise freeze the evaluation-engine
semantics associated with each decision, so that the procedure can be
reconstructed as it operated, not as a later version of the engine would operate.
The conformance question is not "is this policy still on file" but "can this
verdict be regenerated."

### Discrete and Deterministic Evaluation

Replayability constrains the form of the evaluation, not only its recording.
Decision procedures MUST be discrete and deterministic. Continuous-valued
assessments are disallowed where they introduce floating-point or
implementation-dependent variation, because such variation makes verdicts
non-reproducible across conforming implementations and across time. This is the
constraint ZTG-5 invokes when it requires harm and liability assessment to use
discrete banded algebra rather than continuous values: the banding exists so that
the assessment replays identically. ZTG-0b is the prerequisite that requirement
serves.

### Replay Reconstructs Verdicts, Not Effects

Replay reconstructs the decision; it MUST NOT re-emit the effect. Re-dispatching
a governed action during replay — sending the message again, moving the funds
again, writing to the external system again — is not reproduction of a decision;
it is a second irreversible action. A conforming replay path is structurally
incapable of producing external effects. It reads recorded inputs and re-runs the
evaluation to recover the verdict; it does not traverse the effect surface.

This separation mirrors the Mechanistic Boundary (ZTG-1): just as reasoning
reaches the world only through the boundary, replay examines past boundary
decisions without itself becoming a path to the world.

### The Non-Determinism Boundary

The governed system contains a non-deterministic component — the reasoning model
— whose output cannot be reproduced and is not required to be. ZTG-0b draws the
line precisely: the model's output is a *recorded input* to the boundary, and
replay re-evaluates the boundary's decision over that recorded output. Replay
does not re-run the model and does not require the model to be deterministic.

This is what keeps replayability in the Invariant layer and consistent with the
introduction's load-bearing rule that the Invariant MUST NOT depend on the
Envelope. If replay required reproducing the model's output, ZTG-0b would inherit
the Envelope's statistical character and cease to be a deterministic guarantee.
Because replay operates over the recorded output rather than regenerating it, the
boundary's decision is reproducible even though the reasoning that produced its
input is not.

### Replay Status and Degradation

Each governance record carries a replay status with three values: `replayable`,
`degraded-by-attested-deletion`, and `failed`.

- `replayable` — the recorded substrate is sufficient to reconstruct the verdict.
- `degraded-by-attested-deletion` — a replay-load-bearing input has been deleted
  under an authorized, recorded deletion event, and the verdict can no longer be
  reconstructed for that documented reason.
- `failed` — the verdict cannot be reconstructed and no attested deletion
  accounts for it.

Deletion of a replay-load-bearing input — for example, under a data-erasure
obligation — MUST transition the affected record to `degraded-by-attested-
deletion`, bound to the deletion event that caused it. Replay of a degraded
record returns this documented degraded state; it MUST NOT return a silent
absence or a substitute verdict. A degraded record is conformant only because the
deletion that degraded it was itself authorized and recorded as a governance
event under ZTG-0a. A record that cannot be replayed and is not accounted for by
an attested deletion is `failed`, and a `failed` status is a violation, not a
documented limitation.

This resolves the erasure-versus-replay tension that ZTG-0a named and deferred to
this chapter. ZTG-0b does not subordinate erasure to replay or replay to erasure;
it requires that any loss of replay fidelity be attributable. The framework's
position is that an honest, documented inability to replay is conformant, and a
silent one is not.

### Conformance Criteria

A conforming implementation can: reconstruct the verdict of any `replayable`
record from its recorded inputs, policy version, and pinned engine semantics, and
obtain the original verdict; demonstrate that its replay path cannot produce
external effects; demonstrate that engine-semantic drift does not silently change
replayed verdicts; demonstrate that its evaluation is discrete and deterministic;
assign and honor the three replay-status values; and demonstrate that every
`degraded-by-attested-deletion` record is bound to an authorized, recorded
deletion event and that `failed` records are surfaced as violations.
