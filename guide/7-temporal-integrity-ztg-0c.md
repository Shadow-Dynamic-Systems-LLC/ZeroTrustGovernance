# §7. Temporal Integrity (ZTG-0c)

Temporal Integrity is the third of the five structural prerequisites (ZTG-0a
through ZTG-0e). Observability records what happened and Replayability
reconstructs it; both presuppose that the *when* of a decision — and the state it
was evaluated against — is itself trustworthy. ZTG-0c establishes that
presupposition. A governance decision is meaningful only relative to a definite
instant and a coherent state at that instant; if time can drift, roll back, or be
supplied by the governed system, every time-bounded guarantee and every replay
loses its anchor.

## Operational Questions

ZTG-0c sits in the prerequisite range that serves **replayability** and
**evidence coupling**, and it is what those properties stand on. Replay (ZTG-0b)
reconstructs a decision *as of decision-time*; that phrase has no content unless
decision-time is a definite, trustworthy instant against a definite state — which
is exactly what ZTG-0c supplies. ZTG-0c also conditions **governance continuity**
(ZTG-0e): the ordering of governance events across policy changes depends on a
coherent temporal and causal account of which event preceded which. And it
underwrites **admissibility**: a decision is only independently checkable if
*when* it was made, and against what, can be trusted rather than asserted.

## Further Considerations

**The distributed-systems grounding.** Concurrency theory established decades ago
that a distributed system has no free, globally-shared "now": independent
components cannot share a perfect instantaneous clock, so coherent reasoning about
order must be constructed rather than assumed. Lamport's happens-before relation
makes causal order — not wall-clock time — the reliable account of what preceded
what, and the consistent-global-snapshot result shows that a coherent system-wide
state "as of an instant" is something a distributed system must deliberately
capture, not something it can read off a clock. ZTG-0c is these results applied to
governance. Its insistence that causal order is authoritative on conflict, and
that a decision evaluate against a deliberately-captured coherent snapshot rather
than a bag of individually-fresh inputs, is not over-engineering; it is what the
distributed character of any real governed system requires. A governance
architecture that assumed a perfect global clock would be assuming away a problem
the field proved is not assumable.

**Time as an attack surface.** Most governance bypasses that route through time do
not require defeating policy; they require defeating the clock. Backdating an
action into a permitted window, presenting an expired credential under a
rolled-back clock, or reordering events to manufacture a favorable causal story
are all attacks on temporal integrity, not on the policy logic. This is why ZTG-0c
treats the time source as a trust boundary as serious as identity or policy: the
weakest link in a time-bounded guarantee is usually the time, not the bound.

**Relationship to replayability.** ZTG-0c and ZTG-0b are tightly coupled. The
point-in-time snapshot ZTG-0c requires is precisely the object ZTG-0b replays, and
the decision-time ZTG-0c fixes is the reference instant ZTG-0b reconstructs
against. ZTG-0b's requirement to pin the policy and engine "in effect at
decision-time" is well-defined only because ZTG-0c defines decision-time and the
coherent state at it. The two prerequisites should be read together: ZTG-0c
establishes the temporal anchor, ZTG-0b reconstructs from it.

**Relationship to observability.** ZTG-0c's guarantees are only auditable because
ZTG-0a records them: the decision-time, the time-source check
(`TIME_SOURCE_CHECKED`), the recorded skew, and any detected time/order
inconsistency are all governance-relevant events. ZTG-0c says what must be true of
time; ZTG-0a is why an auditor can confirm it was.

**Bounded skew is a parameter, not a softening.** Requiring skew to be *bounded
and recorded* is not a relaxation of the trusted-time requirement; it is the
honest form of it. No physical clock is exact, so the conformant move is to bound
the uncertainty and record it, making "now" an audited interval rather than a
false point. Choosing the bound is a deployment decision; having a bound, and
recording it, is the requirement.

**Loss of temporal integrity and Stasis.** When the system cannot establish
trusted decision-time, cannot obtain a coherent snapshot, or detects a time/order
inconsistency it cannot resolve, it has lost a precondition for sound governance
decisions. Consistent with the boundary's fail-closed posture, the correct
response is to refuse rather than to proceed against uncertain time, and sustained
loss of temporal integrity is a candidate Stasis (ZTG-2) trigger. The precise
trigger semantics belong to the ZTG-2 chapter; ZTG-0c establishes that degraded
temporal integrity is a refuse-not-proceed condition.

## How We Do It (Constable reference implementation — non-normative)

Constable establishes decision-time and a coherent snapshot from infrastructure
the agent runtime cannot reach, and reconciles recorded time against the monotonic
log.

**Trusted time service.** Constable draws decision-time from a time service
outside the agent runtime, attested and monotonic, with a configured skew bound.
The agent runtime has no path to set, advance, or roll back this clock. Each
decision records its decision-time, the time-source attestation, and the skew
bound in effect, emitting a `TIME_SOURCE_CHECKED` event under ZTG-0a.

**Snapshot pinning.** At decision-time the gate pins a coherent snapshot of policy
bundle version, identity state, surface registry, and prior governance state, and
evaluates against that snapshot rather than against live values that may move
during evaluation. The pinned snapshot is the same object the ZTG-0b replay
harness reloads, which is what lets a replay correspond to the world as of
decision-time rather than to a later state.

**Order reconciliation with the Monotonic Logger.** The append-only Monotonic
Logger provides causal/append order; recorded wall-clock timestamps provide time.
Constable reconciles the two and treats a timestamp that contradicts append order
as a temporal-integrity fault — recorded, surfaced, and, where unresolved, routed
to refusal. Causal order is authoritative for sequencing governance events;
wall-clock time locates them.

**Time-bounded checks.** Credential expiry, policy effective and expiry dates, and
windowed authorizations are evaluated against trusted decision-time only. No
time-bounded check consults a clock value supplied through the agent runtime or
derived from model output.

**Conformance tests.** Constable's internal testing for ZTG-0c includes:
non-model-time tests confirming the agent runtime cannot influence decision-time;
monotonicity and rollback tests confirming the clock cannot be moved backward
silently; skew-bound tests confirming skew is bounded and recorded;
snapshot-coherence tests confirming a decision's inputs derive from one cut and
replay against it; staleness and future-state tests confirming such inputs are
refused; and time/order reconciliation tests confirming timestamp-versus-append
conflicts are detected and surfaced. The protocol is documented in the conformance
verification specification referenced in §22.
