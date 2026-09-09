# §8. Identity Integrity (ZTG-0d)

Identity Integrity is the fourth of the five structural prerequisites (ZTG-0a
through ZTG-0e), and the last of the input-trust prerequisites: with
Observability, Replayability, and Temporal Integrity it completes the set of
properties a decision's inputs must have before the boundary can be trusted to
act on them. ZTG-0d answers *by whose authority*. A decision can be recorded
(ZTG-0a), reproducible (ZTG-0b), and temporally well-anchored (ZTG-0c) and still
be ungoverned if the authority it claims to act under cannot be attributed to a
real, accountable party.

## Operational Questions

ZTG-0d sits in the prerequisite range serving **replayability** and **evidence
coupling** — an authorization is only fully reconstructable and only worth
coupling to an effect if *whose authority* it carried is part of the record. It is
also the prerequisite beneath **override visibility**: the appendix maps override
visibility to the framework's signing and lineage structure, and that structure is
exactly what ZTG-0d requires. An override is attributable only if the identity
that authorized it is cryptographically bound and recorded. ZTG-0d supplies the
*to whom* of every governance act; without it, attribution is asserted rather than
demonstrable.

## Further Considerations

**The delegated-authority grounding.** The law of agency worked out, long before
autonomous software, what it means for one party to act under another's authority.
An agent acts with the principal's authority only to the extent the principal
conferred it; an act beyond that authority is *ultra vires* — outside the power
granted — and does not bind the principal as authorized. Authority can be conveyed
in advance or ratified, but it always originates with a principal who is
accountable for its exercise, and an agent cannot enlarge its own authority by
asserting it. ZTG-0d is this structure applied to a governed autonomous system.
The system is an agent; its authority is delegated by a ratifying principal; an
action under authority that was never delegated is ultra vires and unauthorized;
and attribution back to the principal is what makes the principal accountable for
what was delegated. The requirement that the chain terminate at a human or
institutional principal is not a bureaucratic preference — it is the condition
under which the system's actions have an accountable author at all.

**Attribution is not the same as binding force.** ZTG-0d supplies the *to whom* of
a governance act: who authorized it, traceable to an accountable principal. It is
distinct from two neighboring properties it is easy to conflate. It is not
override *visibility* in the narrow sense — visibility is whether an override is
traceable; ZTG-0d is the identity machinery that makes such tracing possible, but
override visibility as a property is about the override record, not the identity
binding. And it is distinct from the question of whether authority *binds at the
point of exercise* rather than operating advisorily — that is a property of the
boundary's force (ZTG-1) and of the architecture as a whole, not of identity. A
correctly attributed authorization that the boundary treats as advisory is an
attribution success and a governance failure. ZTG-0d guarantees attribution; it
does not by itself guarantee that attributed authority binds. (The binding-force
question is tracked separately and is deliberately unplaced; see Draft Flags.)

**Identity as a trust boundary.** Identity is the third of the inputs the governed
subject must not control, alongside policy-relevant memory and time. The pattern
recurs because it is the same vulnerability each time: any governance check the
governed system can supply to itself is not a check. Reading ZTG-1 (memory),
ZTG-0c (time), and ZTG-0d (identity) together, the framework is drawing a single
line — the governed subject does not get to author the inputs that govern it —
across three different input types. The recurrence is evidence the line is real,
not three separate rules that happen to rhyme.

**Relationship to replayability and temporal integrity.** ZTG-0d depends on ZTG-0c
for the meaning of "valid at decision-time" and feeds ZTG-0b by making identity
state part of the reconstructable snapshot. The three compose into a single
property: a replayed decision reproduces not only the inputs and the verdict but
the authority and its validity status exactly as they stood. Attribution that
could not be replayed would be attribution one had to take on trust, which is the
condition ZTG-0b exists to eliminate.

**Institutional identity and key custody.** Terminating the chain at an
institutional principal raises real questions of institutional key custody,
rotation, and succession — whose keys represent the institution, and how
authority survives personnel change. These are genuine deployment concerns and
they are not reasons to weaken the requirement; an institution that cannot say
whose authority binds it has an institutional problem ZTG-0d surfaces rather than
creates. The chapter requires attributable institutional identity; it does not
specify custody mechanism, which is a deployment matter.
