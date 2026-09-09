# §7. Temporal Integrity (ZTG-0c)

## Normative

Every governance decision MUST be evaluated at a defined instant, against a
coherent state as of that instant, using time obtained from a source the governed
reasoning system does not control. The instant, the state, and the time source
are jointly the temporal context of the decision, and all three MUST be recorded
under ZTG-0a so the decision can be replayed under ZTG-0b.

### Decision-Time

Each governance decision has a single decision-time: the instant at which the
boundary evaluates the proposed action against policy. Decision-time is
established by the architecture, not chosen by the reasoning system, and it is the
reference instant for every time-dependent input to the decision — policy
effective dates, credential validity windows, rate and quota windows, and the
state snapshot defined below. An architecture that evaluates different inputs of a
single decision against different instants does not have a well-defined
decision-time and does not satisfy ZTG-0c.

### Trusted Time Source

Time MUST come from a source whose integrity is attestable, that advances
monotonically, and whose skew is bounded and recorded. The reasoning system MUST
NOT originate, supply, or influence the time a decision is evaluated against.

The structural reason is the same one ZTG-1 invokes to refuse memory-to-policy
bootstrap: a governance input that the governed subject controls is not a
governance input. A system that can set its own clock can defeat every
time-bounded policy — presenting an expired credential as valid, acting outside a
permitted window, or replaying a stale authorization — without the policy ever
being wrong. Monotonicity prevents silent rollback, which would otherwise allow a
later event to be presented as earlier; bounded, recorded skew makes the residual
uncertainty in "now" an audited quantity rather than an open one. Best-effort
wall-clock time supplied without these properties does not satisfy ZTG-0c,
because rollback and unbounded drift remain available as manipulation vectors.

### Point-in-Time State Consistency

A decision MUST be evaluated against a coherent temporal cut: a single,
consistent snapshot of every governance-relevant input — policy version, identity
state, surface and sub-surface registry, harm-class and ceiling declarations, and
prior governance state — drawn as of decision-time. The inputs to one decision
MUST NOT be assembled from different instants.

Point-in-time consistency, not mere freshness, is the requirement. A set of
individually-current inputs drawn from slightly different moments may correspond
to no single real state of the system, and a decision evaluated against such a set
cannot be faithfully replayed, because there is no coherent "world as of
decision-time" to reconstruct. The snapshot is what ZTG-0b replay reconstructs;
ZTG-0c is the requirement that such a snapshot exists and is coherent.

### No Stale, Future, or Temporally Inconsistent Inputs

The boundary MUST NOT evaluate against stale policy, future state, or temporally
inconsistent inputs. This is the requirement ZTG-1 names in its ZTG-0c
composition clause, stated here as a prerequisite in its own right. Stale inputs
evaluate a decision against a world that has already changed; future state
evaluates it against a world that does not yet exist; temporally inconsistent
inputs evaluate it against a world that never existed. Each breaks the
correspondence between the decision and a definite state, and each is a ZTG-0c
violation independent of whether the resulting verdict happens to be acceptable.

### Temporal Order and Causal Order

The system MUST maintain a coherent account of the order of governance events, and
that account MUST be reconcilable with recorded time. Where recorded wall-clock
time and the logical append order of ZTG-0a disagree, the logical/causal order is
authoritative for governance sequencing, and the disagreement MUST be detectable
and recorded as a temporal-integrity fault rather than silently resolved. A
timestamp that would place a later-appended event before an earlier one is
evidence of clock failure or manipulation, not a tiebreak to absorb. Recorded time
locates events; causal order sequences them; ZTG-0c requires the two to be
consistent and requires inconsistency to surface.

### Time-Bounded Authority

Where authority is time-bounded — credentials that expire, policies with
effective and expiry dates, authorizations valid only within a window — the bound
MUST be evaluated against trusted decision-time, never against time asserted by or
derivable from the reasoning system. The expiry of authority is a governance fact;
it cannot depend on a clock the governed system can move.

### Conformance Criteria

A conforming implementation can: establish a single decision-time per decision
from a non-model source; demonstrate that time advances monotonically and that
skew is bounded and recorded; evaluate each decision against a coherent
point-in-time snapshot and demonstrate the snapshot is reconstructable for replay;
reject or refuse on stale, future, or temporally inconsistent inputs; detect and
record disagreement between recorded time and causal order; and evaluate
time-bounded authority against trusted time only.
