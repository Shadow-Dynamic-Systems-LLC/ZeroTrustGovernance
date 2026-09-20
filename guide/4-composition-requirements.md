# §4. Composition Requirements

ZTG does not run in isolation. It governs a reasoning system it did not build, draws
time and identity from external services, reaches the world through external effect
targets, and may itself sit upstream or downstream of other systems. The Composition
Requirements specify what must be true of the systems ZTG composes with, so that its
invariants survive composition rather than being silently weakened at the seams. Where
§3 specifies the decision at the center and §22 specifies how conformance is verified,
§4 specifies the architecture's perimeter: which composing systems are inside the trust
boundary, which are outside it, and what each must guarantee.

## Operational Questions

§4 is not mapped to one of the seven operational questions; it is what keeps the seven
true across the architecture's boundary with other systems. Each invariant holds within
the governed perimeter; §4 is the requirement that nothing crossing that perimeter —
an input, a time value, an identity, an effect, an evidence record — degrades the
invariant it touches. A guarantee that holds internally but dissolves at the first
composition seam is not a guarantee an institution can rely on, and §4 is where the
seams are governed.

## Further Considerations

**The end-to-end grounding.** Systems engineering settled, decades ago, a question about
where a guarantee must live. The end-to-end argument observed that a property such as
reliable or correct delivery can be completely guaranteed only by the endpoints that
understand it; implementing it in a lower layer the endpoints merely trust produces a
function that is, from the endpoint's standpoint, incomplete and not fully relied upon.
ZTG's composition stance is this argument applied to governance. A governance property
must be enforced at the layer that owns the invariant — the boundary, the gate, the
evidence substrate — and MUST NOT be assumed of a composing layer that does not itself
guarantee it. When ZTG accepts a time value, an identity, or an input from a composing
system, it does not inherit a governance guarantee from that system; it either verifies
the property at its own boundary or treats the system as untrusted. The end-to-end
argument explains why: a guarantee assumed of a lower layer one does not control is not a
guarantee, only a hope wearing its name.

**Composition is asymmetric.** ZTG is built to be composed *into* untrusted environments —
governing a reasoning system it cannot trust is the entire point — but its guarantees do
not propagate *outward* by composition. A system that wraps or invokes a ZTG-conformant
component does not thereby become governed; it becomes governed only by meeting the
requirements itself. This asymmetry is worth stating because it is easy to assume the
reverse: that touching a governed system confers governance. It does not. Governance is a
property of an architecture meeting the invariants, not a contagion spread by adjacency.

**The perimeter is where overclaiming happens.** Most overstatements of what a governance
architecture provides occur at the seams: a conformant core composed with a non-conformant
input source, effect target, or downstream consumer, described as if the whole were
governed. §4 exists partly to make the bound honest — the guarantee holds to the
perimeter and no further, and a composition that crosses the perimeter into an ungoverned
system is exactly where the guarantee stops. Naming the perimeter is what keeps the claim
truthful.

**Multi-system governance is the open frontier.** The composition of governed systems with
each other — agent-to-agent, governed-pipeline-to-governed-pipeline — is where the most
interesting and least settled questions live: how delegation chains compose, how exposure
accumulates across organizational boundaries, how Stasis in one system propagates to
those depending on it. §4 sets the principle (invariants hold end-to-end, attestations are
verified not trusted, exposure composes) and is candid that the full treatment is future
work.

## How We Do It (Constable reference implementation — non-normative)

Constable's perimeter is a small set of named composition surfaces, each explicitly placed
inside or outside the trust boundary.

**Inside the boundary.** The trusted time service (ZTG-0c), the identity and credential
system (ZTG-0d), the Monotonic Logger (ZTG-0a), the surface registry and adaptors (ZTG-3),
and HumanSeal (the human-authority path) are inside the boundary; each is held to the
requirement its invariant states, and Constable's conformance regime (§22) verifies that
it meets it rather than assuming it does.

**Outside the boundary.** The agent runtime composes as proposer-only; Airlock sanitizes
its output and every other input (§18) before the gate sees it; Memoria exposes the
attested promotion gate through which memory content may become policy-relevant input. No
governance input is taken from any of these on trust.

**Effect targets and consumers.** External effect targets are reachable only through
registered surface adaptors; Constable acquires a new effector only by registering a
surface for it under governance (ZTG-0e). Evidence consumers — operator dashboards,
exports — read derived views computed from the Logger and cannot write back into the
decision path.

**Composition checks.** Constable's conformance tests for §4 confirm that no governance
input resolves to an outside system, that the agent holds no time/identity/promotion
authority, that every input path traverses Airlock, and that effect targets are reachable
only through registered surfaces. The protocol is documented in the conformance
verification specification referenced in §22.
