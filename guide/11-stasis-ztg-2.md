# §11. Stasis (ZTG-2)

Stasis is the second system invariant (ZTG-1 through ZTG-5) and the system-level
expression of fail-closed semantics. Where the Mechanistic Boundary (ZTG-1)
refuses an individual action it cannot authorize, Stasis is the held state the
system enters when it cannot guarantee its invariants hold at all. The structural
prerequisites (ZTG-0a through ZTG-0e) each identify conditions under which the
boundary must refuse rather than proceed; ZTG-2 is where sustained or structural
loss of those guarantees escalates from per-decision refusal to a held system
state, and where the path back to normal operation is defined.

## Operational Questions

ZTG-2 is the invariant mapped to **fail-closed semantics**: it specifies what the
system does when it cannot establish that acting is safe. It is the destination of
the refuse-not-proceed conditions the prerequisite chapters defer to it —
sustained loss of temporal integrity (ZTG-0c) and persistent governance
inconsistency (ZTG-0e) both escalate here, and the same pattern applies to loss of
the ability to record (ZTG-0a), attribute authority (ZTG-0d), or evaluate the
boundary (ZTG-1). ZTG-2 also bears on **override visibility** and **governance
continuity**: entry into and exit from Stasis are themselves attributable,
recorded governance events, and exit is an exercise of ratifying authority.

## Further Considerations

**The safety-engineering grounding.** Safety-critical control has a settled answer
for what a system does when it loses confidence that it can act safely: it reverts
to a defined safe state, and it does so by default rather than by decision. A
reactor inserts its control rods; a fail-closed valve shuts; an elevator's
governor grips the rails when the cable tension that proves the car is supported is
lost. The discipline these share is that the safe state is entered on *loss of a
positive guarantee*, not on positive detection of danger — the elevator does not
wait to detect a fall, it acts on the loss of the evidence that it is held.
Stasis is this principle for governed autonomous execution. The triggers are
losses of positive guarantee — that time is trustworthy, that governance is
consistent, that authority is attributable — and the response is reversion to a
state that withholds action. A governance architecture that waited to detect harm
before holding would be the elevator that waits to detect the fall.

**Fail-closed must be closed at the edges too.** The value of a fail-safe state
depends entirely on its not having a convenient override, because the moments it
matters most are the moments operators most want to proceed. Safety engineering
learned this the expensive way: interlocks defeated "just this once," alarms
silenced during the incident they were warning of. The non-bypassability
requirement is the lesson encoded. It is also why exit is ratified rather than
automatic: an automatic exit on apparent clearance is an override with a
plausible-sounding trigger, and the failure modes that put a system into Stasis are
exactly the ones that can make a condition *appear* clear while it is not — a
spoofed-back time source, a transiently-agreeing set of partitioned gates.

**Stasis as held authority, not lost capability.** It is worth being precise that
Stasis withholds *authority*, not *capability*. The system in Stasis is fully
capable — it can reason, it can record, it can describe its own state — it simply
cannot act, because it grants itself no authority to. This mirrors the
executive-function framing of the introduction (§1.4): capability and the
authority to exercise it are separable, and an architecture that separates them can
hold the second while preserving the first. A held system that retained no capacity
would be useless to the operators who must diagnose and resolve the condition; a
held system that retained capacity but not the discipline to withhold authority
would not be held at all. Stasis is the deliberate occupation of the space between.

**The cost of holding is real and is the point.** Stasis trades availability for
the guarantee that the system does not act ungoverned. Under partition, under a
degraded clock, during an unsettled governance change, a ZTG-conformant system may
be unavailable precisely when an operator wants it most. This is the same
consistency-over-availability posture ZTG-0e takes explicitly, raised to the system
level. The framework does not present this cost as negligible; it presents it as
the correct trade. An autonomous system that remains available by acting under
guarantees it cannot establish is not more useful, only more dangerous, and the
usefulness is the kind that shows up as throughput now and as externalized exposure
later (§1.5).

**Relationship to harm class.** The cost of being wrong about whether to hold is
asymmetric and tracks ZTG-5 harm class. Wrongly holding a Restorable-class
capability is recoverable; wrongly proceeding on an Irreversible-class action under
unestablished guarantees is not. The escalation threshold and the willingness to
hold should reflect this asymmetry, and an implementation that tunes its Stasis
sensitivity uniformly across harm classes is leaving the asymmetry unused. The
precise coupling between harm class and Stasis sensitivity is a composition concern
between ZTG-2 and ZTG-5 rather than a property of either alone.
