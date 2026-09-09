# §4. Composition Requirements

## Normative

Every system ZTG composes with is either inside the trust boundary or outside it, and
the architecture MUST treat it accordingly. A system inside the boundary is one whose
guarantees ZTG depends on; it MUST meet the composition requirement stated for its role,
and that requirement MUST be one ZTG can verify, not one it assumes. A system outside the
boundary is treated as untrusted: it may propose, supply candidate data, or receive
derived output, but it MUST NOT be a source of any governance input ZTG relies on. There
is no third category — no system trusted because trusting it is convenient, and no
governance input accepted on the strength of a composing system's good behavior.

Where a composing system that would need to be inside the boundary cannot meet its
requirement, the architecture MUST either relocate it outside the boundary and treat it
as untrusted, or refuse to compose. It MUST NOT compose with the unmet requirement and
proceed as if it were met. This is the perimeter form of fail-closed: an unverifiable
composition is not a smaller guarantee, it is the absence of one.

### The Reasoning System

The reasoning system composes as a proposer only. It is inside the deployment but
outside the trust boundary: it originates candidate actions and their parameters, and
nothing else ZTG relies on. It MUST NOT hold an authorizing identity (ZTG-0d), supply or
influence decision-time (ZTG-0c), or elevate its own memory contents into policy
(ZTG-1). The reasoning system's outputs are untrusted input and are sanitized as such
before they enter an authorization request (§18). Composing a more capable or
better-aligned model does not move it inside the boundary; capability and alignment are
Envelope properties, and the boundary's guarantees MUST NOT depend on them (§1.3).

### Memory Subsystems

A memory subsystem composes through an explicit, attested promotion protocol. Raw memory
contents MUST NOT be visible to policy evaluation, and memory content becomes a
policy-relevant input only by being promoted through a protocol that requires named human
attestation, recorded as a governance event (ZTG-1, ZTG-0a). The structural reason is the
one ZTG draws for time and identity: memory is typically writable by the same reasoning
system whose outputs the boundary gates, so unpromoted memory is a governance input the
governed subject controls, which is not a governance input. A composing memory subsystem
that cannot expose such a promotion protocol is outside the boundary, and its contents
reach policy only after passing through one that can.

### Time and Identity Services

A composing time source MUST meet ZTG-0c: attestable integrity, monotonic advance,
bounded and recorded skew, and no path by which the reasoning system can set or influence
it. A composing identity and credential service MUST meet ZTG-0d: non-repudiable,
revocable cryptographic credentials whose delegation chains terminate at a human or
institutional ratifying principal. These services are inside the trust boundary by
necessity — the architecture's guarantees rest on them — so the requirement on them is
not negotiable, and a service that cannot meet it cannot supply ZTG's time or identity.

### Input Sources

Every input that reaches governance evaluation MUST pass the Input Sanitization Boundary
(§18) first, and the gate MUST accept only sanitized inputs. This applies to all input
classes without exception: end-user input, reasoning-system output, promoted memory, and
external data pulled into the decision. Input sanitization is the specific composition
requirement that §18 details; §4 establishes that it is mandatory for every input-bearing
composition and that there is no input path into evaluation that bypasses it.

### Effect Targets

An external system that an effect acts upon composes only through a registered surface
(ZTG-3). The architecture holds no ambient capability to reach an effect target outside
the enumerated surfaces, so composing a new effect target is the governed act of
registering a surface for it, not the ad-hoc acquisition of a new effector. Where ZTG-4
reconciliation of an indeterminate effect requires establishing what actually happened at
the target, the target's queryability is a composition property: a target that cannot be
queried to establish an effect's disposition raises the cost of an indeterminate effect,
which is a reason to classify effects through it conservatively (ZTG-5), not a reason to
weaken the coupling requirement.

### Evidence Consumers

A system that consumes ZTG's records — a dashboard, an analytics pipeline, a downstream
report — composes as a reader of derived views. It MUST NOT be the system of record
(ZTG-0a owns that), and its derived outputs MUST NOT feed back as governance inputs
unless they re-enter through a governed path: a metric computed downstream is not a
governance fact, and an architecture that let its own dashboards become inputs to its
decisions would have created a path for derived presentation to influence governance
unattributably. Evidence consumers read; they do not govern.

### Composition With Other Governed Systems

The hardest seam is ZTG composing with ZTG: one governed system's effect becoming
another governed system's input, or governed systems acting in concert. Across such a
seam, the invariants MUST hold end-to-end, not merely within each system. A downstream
governed system MUST treat an upstream system's outputs as untrusted input subject to its
own sanitization and authorization, and MUST verify any attestation an upstream system
carries rather than honoring it on trust — the delegation chain (ZTG-0d) must be
checkable across the seam, or it does not cross it. Exposure composes across the seam
rather than resetting: a sequence that crosses governed systems accumulates assessment as
ZTG-5 composition does across surfaces, so that routing an action chain through multiple
systems does not launder its exposure. This chapter establishes the principle; the full
treatment of multi-system and multi-agent composition is larger than §4 and is flagged
as partially specified.

### Conformance Criteria

A conforming implementation can: classify every composing system as inside or outside the
trust boundary and demonstrate that no governance input derives from an outside system;
demonstrate that the reasoning system composes as proposer-only, holding no authorizing
identity, time, or unpromoted-memory authority; demonstrate that time and identity
services meet ZTG-0c and ZTG-0d; demonstrate that every input path passes §18; demonstrate
that effect targets are reachable only through registered surfaces; demonstrate that
evidence consumers cannot feed derived views back as governance inputs unattributably; and
demonstrate that, where it composes with another governed system, attestations are
verified and exposure composes across the seam. Where a composing system cannot meet its
requirement, the implementation can show it is treated as untrusted or that composition is
refused, never composed-and-degraded.
