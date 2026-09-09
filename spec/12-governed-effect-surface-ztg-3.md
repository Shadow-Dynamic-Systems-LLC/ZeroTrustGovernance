# §12. Governed Effect Surface (ZTG-3)

## Normative

All governed effects MUST occur through enumerated surfaces and sub-surfaces, and
the architecture MUST make unenumerated effect channels structurally unreachable.
Every channel capable of producing a governed effect MUST be registered before it
can be used, with its governance-relevant properties declared at registration.
Effects through unenumerated channels are unauthorized, and the capacity to
produce such effects MUST NOT exist as an ambient capability of the governed
system.

### Enumeration and Closure

The set of effect channels is closed. An effect channel that is not registered is
not merely prohibited; under ZTG-3 it MUST NOT be reachable. This is the
distinction between declaring a rule and enforcing a structure, and ZTG-3 takes the
structural side, exactly as ZTG-1 takes it for the boundary: a closure that depends
on the governed system choosing not to use an available unregistered channel is
not closure, because the governed system's choices are the thing under governance.

Structural closure means the registered surface mechanism is the only path from the
governed system to the world. The system holds no ambient authority to act outside
the enumerated surfaces — no general-purpose effect capability it can direct at an
unregistered target. An effect can reach the world only by being dispatched through
a registered surface, because there is no other reachable way to produce one. This
is what makes ZTG-1's complete mediation complete: mediation of every action
presupposes that every action route is known, and ZTG-3 is the requirement that the
route set is both known and exclusive.

### Surface Declarations

Each surface and sub-surface declares its governance-relevant properties at
registration. At minimum these include its harm-class default and compositional
multiplier (ZTG-5) and its reversal strategy (below). A sub-surface declaration may
tighten its surface's defaults but MUST NOT relax them: a sub-surface may declare a
higher harm class or a more conservative reversal strategy than its parent surface,
never a lower or laxer one. Monotonic tightening ensures that narrowing the channel
can only increase governance stringency, so that no effect is governed more weakly
by virtue of being routed through a more specific sub-surface.

### Reversal Strategy

Each surface declares a `reversal_strategy`: a description of what the system can
undo or compensate for effects dispatched through it. The reversal strategy is
descriptive provenance. It records a capability of the system, and it MUST appear
in the decision provenance of every effect through the surface.

The reversal strategy MUST NOT relax governance. It does not lower the harm class,
and it does not select a lighter gate. This is the orthogonality ZTG-5 requires:
harm class describes consequences in the world, while reversal strategy describes
what the system can do about them, and the two are independent. A surface with a
strong reversal strategy and an Irreversible harm class is routed by its harm
class, not rescued by its reversal strategy; forward remediation such as refund,
retraction, or compensation is recorded as available but does not by itself reduce
the consequence the action produces. Both the harm class and the reversal strategy
are present in provenance precisely so that an auditor can see that the second was
not silently used to discount the first.

### Effect Routing

Every governed effect MUST be routed through the registered surface or sub-surface
that matches it, and the routing decision MUST be recorded (`SURFACE_ROUTE_SELECTED`,
ZTG-0a). Routing is the point at which an authorized action becomes an effect
through a specific declared channel, carrying that channel's harm class,
multiplier, and reversal strategy into the action's provenance. The boundary
(ZTG-1) decides whether the action is authorized; the surface (ZTG-3) is the
declared channel through which an authorized action reaches the world.

### Registry as Governance State

The surface registry is governance state under ZTG-0e. Registering a surface,
retiring one, or changing a declaration is an authorized, recorded, ordered, and
consistency-governed transition: authorized under ZTG-0d, recorded under ZTG-0a,
ordered under ZTG-0c, and applied atomically and consistently under ZTG-0e. The set
of effect channels and their declared properties is therefore not a static
configuration but a governed object whose every change is attributable. A decision
evaluates against the registry as of decision-time (ZTG-0c snapshot), so the
surface declarations in force for an effect are exactly those that replay (ZTG-0b)
reconstructs.

### Breach of Closure

Discovery at runtime of a reachable effect channel that is not registered is a
breach of the closure ZTG-3 requires, and MUST be treated as an integrity
violation in the tamper family rather than as an ordinary configuration gap. A
reachable unregistered channel means the system can no longer guarantee complete
mediation — there exists, or may exist, a path to the world the boundary does not
govern. Consistent with fail-closed semantics, this is a Stasis (ZTG-2) trigger:
the system holds rather than continuing to operate while a path around its
mediation is known to exist. Under structural closure such a channel should not
arise in normal operation; its appearance indicates a defect or tampering, which is
why the response is to hold and escalate, not to quietly register the channel and
proceed.

### Conformance Criteria

A conforming implementation can: enumerate every effect channel it can reach and
demonstrate that no reachable effect channel is unregistered; demonstrate that the
capacity to produce effects outside registered surfaces does not exist as an
ambient capability; attach harm class, multiplier, and reversal strategy at
registration and enforce monotonic tightening across sub-surfaces; carry reversal
strategy into provenance without using it to relax harm class or gate; route every
effect through its registered surface and record the routing; treat the registry as
ZTG-0e governance state; and escalate the discovery of a reachable unregistered
channel to Stasis.
