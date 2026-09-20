# §9. Governance Consistency (ZTG-0e)

Governance Consistency is the fifth and last of the structural prerequisites
(ZTG-0a through ZTG-0e). The first four establish that a decision's inputs can be
trusted: recorded (ZTG-0a), reproducible (ZTG-0b), temporally anchored (ZTG-0c),
and attributable (ZTG-0d). ZTG-0e establishes that the governing rules themselves
remain coherent — across the enforcement points that apply them and across the
moments at which they change. It is the prerequisite that lets governance be
*amended* without ever leaving a window in which action is ungoverned or
inconsistently governed.

## Operational Questions

ZTG-0e is the prerequisite mapped to **governance continuity** — the one
operational question none of ZTG-0a through ZTG-0d answers. The others make a
single decision trustworthy; ZTG-0e makes the governing order trustworthy *through
change*. It also closes loops left open by the earlier prerequisites: it is where
the ordering of governance-state transitions (flagged from ZTG-0c), the
consistency of revocation and delegation-chain changes (flagged from ZTG-0d), and
the governance of the observability substrate itself (flagged from ZTG-0a) are
resolved. Governance continuity is the property that a system does not become
ungoverned in the act of re-governing itself.

## Further Considerations

**The constitutional grounding.** Durable governing orders have always had to
solve a specific problem: how to change the rules without dissolving the order in
the interim. A constitution that could not be amended would ossify; a constitution
that dissolved the legal order each time it was amended would produce a gap in
which nothing governed. The solution every durable order converges on is the same
in structure: the rules provide for their own amendment through an authorized,
recorded, ordered procedure, and the existing order remains in force until the
amendment completes. There is no moment of ungoverned interregnum. ZTG-0e is this
principle for governed autonomous execution. Atomic transition is the no-
interregnum requirement; governance-change-as-governance-event is the amendment-by-
authorized-procedure requirement. The framework does not invent a novel solution to
governing-through-change; it adopts the one that constitutional orders and durable
institutions arrived at and makes it mechanical.

**The distributed-systems grounding, convergent with it.** The same structure
arrives independently from distributed systems. A governance plane enforced at
multiple points is a replicated state machine, and keeping replicas coherent under
change is the consensus problem. The CAP result makes the tradeoff explicit:
under partition, a replicated system must choose between remaining available and
remaining consistent. ZTG-0e chooses consistency, which is the fail-closed posture
in the vocabulary of distributed systems. That a constitutional tradition
reasoning about legitimacy and a distributed-systems tradition reasoning about
replicated state arrive at the same requirement — change through an authorized,
ordered procedure that never exposes an inconsistent intermediate — is exactly the
cross-tradition convergence the framework treats as strong evidence that the
requirement is structural rather than stylistic.

**Continuity is what makes the prerequisite set whole.** ZTG-0a through ZTG-0d make
any single decision trustworthy at the instant it is made. Without ZTG-0e, that
trust would not survive the system's own evolution: the first policy update applied
non-atomically, or the first divergence between two gates, would reopen everything
the other prerequisites closed. Governance continuity is therefore not a fifth
independent property bolted on; it is the requirement that the other four remain
true as the system changes. The set is closed by it.

**Refusal during change is the architecture working.** A system that refuses while
a governance transition is settling, or while enforcement points reconcile, will be
read operationally as unavailability, and there will be pressure to relax ZTG-0e to
preserve throughput during policy rollouts. As with the boundary under Stasis
(ZTG-2), the refusal is the architecture functioning as designed. The brief
unavailability of a consistent governance view is a real cost; proceeding under an
inconsistent one is a governance failure. The framework does not trade the second
to avoid the first.

**Relationship to Stasis.** Persistent inability to establish a consistent
governance view is more than a momentary refusal; it is a candidate Stasis (ZTG-2)
condition, in the same family as persistent loss of temporal integrity (ZTG-0c).
The boundary-level response is refusal; the system-level response to sustained
inconsistency belongs to ZTG-2. ZTG-0e establishes the refuse-not-proceed
condition; ZTG-2 owns escalation from repeated refusal to held state.

## How We Do It (Constable reference implementation — non-normative)

Constable treats governance state as a single versioned, consistently-distributed
object, changes it only through authorized atomic transitions, and refuses when its
enforcement points cannot agree on the version in effect.

**Versioned governance bundles.** Policy, registries, harm-class and ceiling
declarations, and substrate configuration are assembled into versioned governance
bundles. The gate evaluates against a single bundle version, pinned at
decision-time per ZTG-0c. A bundle is the unit of atomic transition: a change is a
new bundle version that becomes effective as a whole, never field-by-field, so no
decision sees a partially-applied change.

**Authorized, recorded, ordered transitions.** A bundle transition is itself an
authorized action: it is signed by a ratifying principal under ZTG-0d, emitted as a
governance event under ZTG-0a, and ordered against the Monotonic Logger under
ZTG-0c. A bundle that does not trace to a ratifying principal is not adopted. The
record of which principal moved governance from version N to version N+1, and when,
is part of the evidence substrate.

**Consistent distribution across gates.** Where Constable runs more than one gate,
all gates resolve the governance bundle version for a decision through a
consistently-distributed mechanism, and a gate that cannot confirm it is operating
the agreed version refuses rather than evaluating against a possibly-stale bundle.
Constable chooses consistency under partition: a gate isolated from the governance
plane fails closed.

**Substrate configuration inside the perimeter.** Changes to Monotonic Logger
retention, record schema, integrity mechanism, and access configuration are carried
as part of the governance bundle, so reconfiguring the evidence substrate is an
authorized, recorded, ordered, consistency-governed transition rather than an
out-of-band infrastructure change. The mechanism for rooting the substrate's
bootstrap authority is documented separately and flagged below as not fully settled.

**Conformance tests.** Constable's internal testing for ZTG-0e includes:
atomicity tests confirming no decision observes a partially-applied bundle
transition; authorization tests confirming unsigned or unattributed transitions are
not adopted; cross-gate consistency tests confirming divergent gates refuse rather
than act; partition tests confirming an isolated gate fails closed; and
substrate-governance tests confirming evidence-store reconfiguration is a governed
transition. The protocol is documented in the conformance verification
specification referenced in §22.
