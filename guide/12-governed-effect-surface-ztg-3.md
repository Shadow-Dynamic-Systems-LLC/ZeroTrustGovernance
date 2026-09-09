# §12. Governed Effect Surface (ZTG-3)

The Governed Effect Surface is the third system invariant (ZTG-1 through ZTG-5)
and the structural counterpart to the Mechanistic Boundary. ZTG-1 specifies the
gate every action must pass through; ZTG-3 specifies the closed, enumerated set of
channels there are to act through at all. Together they make execution-boundary
enforcement complete: a boundary can only mediate the effects it can see, and
ZTG-3 is the requirement that every channel capable of affecting the world is
enumerated, declared, and reachable only through the mediated path.

## Operational Questions

ZTG-3 is mapped, with ZTG-1, to **execution-boundary enforcement** — it is the
half that closes the surface so the boundary's mediation is complete rather than
partial. It also serves **replayability and evidence coupling**: surface and
sub-surface registration, the declarations attached to them, and the routing of
each effect are recorded (ZTG-0a) and reconstructable (ZTG-0b), so that which
channel an effect took, under what declared harm class and reversal strategy, is
part of decision provenance. ZTG-3 is what lets the framework claim not merely
that authorized actions are gated, but that there is no ungated way to act.

## Further Considerations

**The capability-security grounding.** Security engineering distinguishes two ways
a system can hold the power to act: ambient authority, where a component can act on
any target it can name, and capability authority, where a component can act only
through unforgeable capabilities it has been explicitly granted. Decades of
security experience established that ambient authority is the source of a large
class of failures — confused-deputy problems, privilege escalation, effects through
paths no one intended to expose — because the set of things a component *can* do is
not enumerated and not bounded. The capability discipline answers this by making
the grantable capabilities the complete and exclusive set of things a component can
do. ZTG-3 is this discipline applied to a governed autonomous system's effects on
the world. The registered surfaces are the capabilities; structural closure is the
absence of ambient authority; an unregistered reachable channel is exactly the
ambient-authority hole capability security exists to eliminate. The framework does
not treat the effect surface as an attack surface to be monitored; it inverts it
into a declared capability set to be enumerated.

**Convergent with control theory.** The same requirement arrives from control. A
controller affects a plant only through its actuators, and control theory is
explicit that an unmodeled actuator — a path by which the controller influences the
plant that the control law does not account for — is an uncontrolled coupling that
invalidates the controller's guarantees. One does not certify a controller while
conceding it may have effectors no one has characterized. ZTG-3's enumeration
requirement is the governance statement of "know your actuators": the set of
channels through which the system affects the world must be closed and declared,
because a guarantee about governed effects is void in the presence of an
ungoverned effector. That capability security (reasoning about authority) and
control theory (reasoning about actuation) converge on the same closed-set
requirement is the cross-tradition agreement the framework reads as evidence the
requirement is structural.

**Enumeration completeness is the hard part.** The difficulty ZTG-3 concentrates is
not stating that effect channels must be enumerated but knowing that they have
been. The boundary-scope discussion in ZTG-1 already noted how subtle the
model-to-world distinction can be: reads whose access pattern signals a target,
resource-consumption patterns observable beyond the system, memory writes consulted
by others, mid-generation tool calls. Each is a candidate effect channel that must
be either registered or rendered unreachable. Structural closure helps by making the
question concrete — not "have we listed every effect" but "is there any reachable
path to the world that does not go through a registered surface" — which is a
property of the architecture that can be analyzed, rather than an open-ended
enumeration that can only be added to. The conformance burden is real and is borne
at the architecture level; ZTG-3 does not pretend the enumeration is easy, only that
it is mandatory and that its completeness is checkable as a reachability property.

**Why the surface is where harm class lives.** Harm class and multiplier attach to
surfaces rather than to individual actions because the surface is the stable,
enumerable, governable object; an individual action is transient and
model-proposed. Attaching consequence declarations to the channel rather than to the
act means the declarations are registered, authorized, and changed under governance
(ZTG-0e), not asserted per-action by the system whose actions are under governance.
This is the same anti-self-authorization logic seen elsewhere: the governed system
proposes an action, but the harm class it carries is a property of the declared
channel it must route through, not a label the system gets to choose for its own
act.

**Retirement and the closed set over time.** Closure is a property that must hold as
the registry changes, not only at a single moment. Retiring a surface must render it
unreachable, not merely mark it deprecated while leaving the channel live; adding a
surface is the authorized act of extending the effect set. Because the registry is
ZTG-0e governance state, these changes inherit atomicity and consistency — there is
no interval in which a half-retired surface is both unregistered and reachable. The
closed-set guarantee and the governance-consistency guarantee are the same guarantee
viewed from the effect surface.
