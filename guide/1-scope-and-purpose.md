# §1. Scope and Purpose

## Purpose

This specification states the structural requirements under which a system whose behavior is
generated non-deterministically may produce effects in the world. It specifies what must hold
architecturally — not what a model should be trained to do, nor what an operator should be
trusted to notice — for the consequential actions of such a system to remain attributable to
human authority and bounded by it.

It is written for three readers: implementers building a governance substrate, deployers
operating a governed system under one, and assessors evaluating a conformance claim about
either.

Conformance to this specification establishes a property about an architecture's guarantees.
It does not establish that a deployment is safe, that its policy is wise, or that its
operators are diligent. What it establishes, and the shape of the claim it supports, is
specified in §22 and §23.

**This specification is the normative document.** Any essays, deployment guidance, tutorials,
or other accompanying material are not adopted as part of this specification and hold
interpretive, not normative, authority. They may explain a requirement, motivate it, or
demonstrate one way of satisfying it; they do not create, extend, or relax it. Where
accompanying material and this specification appear to differ, this specification governs, and
a requirement stated only in accompanying material is not a requirement of this specification.

## Scope

Zero Trust Governance specifies the architecture for governed autonomous execution. It does
not specify, and cannot supply, the human authority under which that execution is governed.
This section fixes what a deployment must already have for the rest of this specification to
apply to it, and states plainly what ZTG does and does not guarantee about that authority.

The distinction this section draws is between a *precondition of applicability* and a
*requirement of conformance*. A deployment that fails a conformance requirement has a
governed system that falls short. A deployment that fails an applicability precondition does
not have a governed system at all, and its conformance claim has no subject.

## Operational Questions

§1, like §22 and §23, is not mapped to one of the seven operational questions. It states the
condition under which the seven are askable. Each of the seven presupposes an authority whose
exercise is being mediated, recorded, or bounded — admissibility presupposes someone whose
policy determines what is admissible; override visibility presupposes someone whose override
it is. This section names that presupposition rather than leaving it to be inferred from the
framing essays.

## Further Considerations

### Preconditions and invariants grade differently

The asymmetry stated above is a general one. Preconditions are binary: required or not
required for a given deployment, and where required, present or absent. Invariants are graded
above a minimum supporting structure — an invariant claim is not made at all below its floor,
and above that floor it reports a position rather than a checkmark.

The reason is that a precondition is a condition on the *subject* of the claim, while an
invariant is a property of the *architecture* being claimed about. A subject either exists or
does not. A property can hold to a degree, and the degree is what a conformance instrument
reports. Grading a precondition would produce the incoherent result of a partially-existing
subject; treating an invariant as binary would produce the floor-washing §23 names.

The full treatment of graded conformance, including the minimum supporting structure below
which an invariant claim is not made, belongs to §23 and is under development. This section
states only the asymmetry, and §23 governs where the two are reconciled.

### Genealogy: authorization as a documented human act

The structure this section requires is not novel. It is the existing discipline of
authorization, applied at a granularity the existing discipline was not built for.

NIST SP 800-53 (Rev. 5, Release 5.2.0) states the requirement directly. **CA-6 Authorization**
requires an organization to "assign a senior official as the authorizing official for the
system," and requires that official, before operations begin, to authorize the system to
operate. Its discussion is explicit about what that assignment means: authorizing officials
"explicitly accept the risk to organizational operations and assets, individuals, other
organizations, and the Nation based on the implementation of agreed-upon controls," and are
"both responsible and accountable for security and privacy risks." NIST SP 800-37 Rev. 2 makes
this the Authorize step of the Risk Management Framework, producing an authorization decision
over a defined authorization boundary. For federal systems these are binding requirements
under FISMA, not recommendations.

The correspondence to this section is close and deliberate. The authorizing official is the
ratifying principal. The authorization decision is the documented act. The authorization
boundary is the enumerated surface over which the claim is scoped. ZTG adopts the structure
and relocates it.

**What ZTG changes is granularity.** The RMF authorizes *the system*, periodically, with
ongoing authorization as the mature form of the practice. ZTG authorizes *the action*, at
every decision. The change is forced by operating tempo rather than chosen for rigor: a
periodic authorization of a system whose consequential actions are proposed by a
non-deterministic component at machine speed authorizes a distribution of behavior rather than
a behavior. The accountability structure is the same one; what changes is that the exercise of
it is continuous rather than an interval judgment about an interval's worth of conduct.

Two control enhancements in the same family have direct analogues here. **AC-3(2) Dual
Authorization** — "enforce dual authorization for [organization-defined] privileged commands
and/or other actions" — is the precedent for the direct-attestation path, where authority is
exercised against a specific act rather than delegated through policy. **AC-3(10) Audited
Override of Access Control Mechanisms** is the precedent for override visibility: the
recognition that overrides are legitimate, expected, and must be recorded as such.

NIST SP 800-207 supplies the component lineage. Its policy decision point divides into a
policy engine, "responsible for the ultimate decision to grant access," which "makes and logs
the decision (as approved, or denied)," and a policy administrator, which executes it; the
policy enforcement point mediates the connection itself. ZTG's boundary (ZTG-1) is a
component of this class, with the constraint that its decision procedure is deterministic and
its enforcement closed (ZTG-3).

**ZTG diverges from SP 800-207 on policy provenance, and the divergence is deliberate.** SP
800-207 permits data access policies to be "encoded in (via management interface) **or
dynamically generated by the policy engine**." This specification does not. A policy engine
that authors the policy it evaluates against is a system that is the terminus of its own
authority, which precondition 4 excludes and which §3 makes unrepresentable. The permission is
reasonable in the setting SP 800-207 addresses, where policy generation is a configuration
convenience within a human-run enterprise. It is not reasonable where the component proposing
the actions and the component generating the policy that permits them are the same statistical
system. This specification tightens that provenance requirement, and states the tightening
rather than eliding it.

The same caution applies to the practice guidance built on that lineage. NIST SP 1800-35,
*Implementing a Zero Trust Architecture* (final, 10 June 2025), documents end-to-end ZTA
implementations across a large vendor set. Its subject is the enterprise case: human and
device subjects requesting access to enterprise resources. That guidance is sound for its
subject and **would be misleading if applied to the governance of stochastic systems**, which
is this specification's subject. The enterprise case assumes a subject whose requests are
generated by a party with independent standing — a person, or a device acting on a person's
behalf — and its controls are calibrated to authenticate and authorize that party. A
stochastic proposer has no independent standing: it is not a party whose requests carry
authority of their own, and treating it as a ZTA subject imports an assumption that does not
hold. This specification takes the component lineage from SP 800-207 and the accountability
structure from SP 800-37 / CA-6; it does not take the deployment pattern from SP 1800-35, and
a deployer should not read that guide as covering this case.

**On the standing of these references.** SP 800-53 and SP 800-37 are binding for federal
systems under FISMA; SP 800-207 and the AI Risk Management Framework (NIST AI 100-1) are
voluntary guidance. This section cites all of them as genealogy — the lineage of the structure
it requires — and claims conformance to none of them. A ZTG conformance claim is not a claim
of conformance to any NIST publication, and MUST NOT be represented as one. Mapping ZTG
requirements onto a control catalog would make this specification's guarantees depend on a
document it does not control, which is the dependency ZTG-0e forbids at the substrate level
and prudence forbids at the document level.

### Why this is scope and not an invariant

Every invariant in this specification is structurally load-bearing: remove ZTG-1 and effects
escape mediation; remove ZTG-3 and mediation has an unclosed complement; remove ZTG-0b and no
decision is checkable. Remove the requirement of human authority and the machine still
functions coherently — it mediates, records, refuses, and replays exactly as before. It simply
governs on behalf of no one.

That is why this is a precondition rather than an invariant. It is not a mechanism the other
mechanisms depend on. It is the reason the mechanisms are worth having, and the condition
under which their guarantees mean anything. An architecture that satisfied every invariant in
this specification while terminating its own delegation chains would be a complete, coherent,
and fully self-authorizing system — which is precisely the artifact this framework exists to
make unbuildable.

## How We Do It (Constable reference implementation — non-normative)

Constable is deployed as a component of the deploying institution's Governed System. Its
ratifying principals are that institution's officers, bound by ZTG-0d identity structure with
key custody held outside the system. Policy adoption is an authorized action: a governance
bundle is signed by a principal and emitted through the same gate as any other governed
effect, so that the adoption of policy is itself a governed act with a record, not a
configuration change.

Constable refuses to operate on a bundle with no adoption lineage. This is the enforcement
point for precondition 2: the failure is not detected at audit but at load, and the response
is refusal rather than a warning. A deployment that cannot produce a signed adoption for its
active policy does not run.
