# §1. Scope and Purpose

## Normative

### The Governed System

A **Governed System** is the machine together with the human and institutional structure that
authorizes its operation. ZTG governs the machine. It is specified for deployment as a
component of a Governed System and has no application outside one.

The division of supply is fixed:

The **Governed System** supplies the authority. Specifically: ratifying principals; the
documented acts by which those principals exercise authority — typically the adoption of
policy; and the institutional structure that makes those acts attributable, revocable, and
answerable.

**ZTG** supplies the mediation of that authority. Specifically: complete mediation of every
effect (ZTG-1, ZTG-3); the record that makes each exercise checkable rather than asserted
(ZTG-0a, ZTG-0b); binding of the exercise to a specific decision, identity, and governance
version at decision-time (ZTG-0c, ZTG-0d, ZTG-0e); and refusal when the connection between an
effect and an exercise of authority cannot be established (ZTG-2).

ZTG does not originate authority, does not hold authority, and MUST NOT be the terminus of a
delegation chain. The system is a mediating component; the principal is the author. This is
stated as a requirement on the architecture, not as an aspiration about its use: an
architecture in which the machine could be the terminus of authority is not a ZTG
architecture, whatever else it enforces.

### Foundational Commitments

Three commitments are stated here as requirements because the normative chapters
rest on them. Each is also argued in the introduction; the argument is informative,
the commitment is not.

**Binding at the point of execution.** Governance under this specification is
exercised in the execution path, not beside it. An authorization decision MUST be a
precondition of the effect it authorizes: no path from proposal to effect MAY exist
that does not pass through the decision. A control that evaluates an action and
reports on it, but whose verdict is not a precondition of the action, is advisory
and does not satisfy any requirement in this specification that calls for
authorization, mediation, or refusal. Every authorization MUST trace to a
principal's attested acceptance of responsibility for the effect authorized —
directly, or through policy that principal ratified. The system MUST NOT be that
principal.

**Continuous ratification.** The authority of a ratifying principal is exercised at
every authorization decision, not at intervals between which the system operates on
its own. Each decision MUST be evaluated against the governance state in force at
that decision's time (ZTG-0c, ZTG-0e), and that state MUST be attributable to the
principal who ratified it (ZTG-0d). Ratification is therefore never in the past
relative to a decision: a decision evaluated against governance state whose
ratifying principal cannot be identified at decision-time, or whose ratification has
been revoked, MUST refuse. Periodic human review of past decisions MAY exist; it does
not substitute for this requirement and MUST NOT be represented as satisfying it.

**Invariant independence from the Envelope.** The Invariant layer MUST NOT depend on
any property of the Envelope (§2). *Depend* is defined operationally: an Invariant
guarantee depends on the Envelope if there exists any Envelope behavior under which
the guarantee fails to hold. Consequently every guarantee this specification assigns
to the Invariant layer MUST hold under substitution of the Envelope by an arbitrary
proposal source, including an adversarial one. Envelope output enters the Invariant
layer only as a proposal subject to sanitization (§18) and authorization (§3); no
Invariant-layer evaluation MAY read Envelope-internal state, confidence, alignment
status, or provenance as an input to a verdict. Improving the Envelope MAY reduce how
often the Invariant refuses; it MUST NOT be a condition of any Invariant guarantee.

### Applicability Preconditions

Preconditions are **binary**. A deployment either satisfies them or this specification does
not apply to it; there is no partial satisfaction and no graded credit. A deployment is within
the scope of this specification if and only if:

1. **A ratifying principal exists and is identified.** At least one human or institutional
   party is designated as accountable for the system's operation, and is identifiable to the
   architecture under ZTG-0d.

2. **Every governing policy traces to a documented adoption act.** Each policy the boundary
   evaluates against was adopted by a ratifying principal in a recorded act, bound to that
   principal's identity and to the governance version it produced (ZTG-0e). A policy present
   in the governance state with no adoption lineage is not adopted, and a deployment operating
   on such policy is outside scope.

3. **Authority is revocable by the institution.** The principal's authority, and any
   delegation of it, can be withdrawn by the Governed System without the machine's
   cooperation. An architecture in which the machine can decline or outlast its own
   revocation is outside scope.

4. **The machine is not the terminus.** No delegation chain terminates at a system identity.
   Service and automated identities may be intermediate links only (§2 Definitions;
   ZTG-0d).

A deployment failing any precondition is **out of scope**, not non-conformant, and MUST NOT be
described as conforming to this specification at any grade. Non-applicability is not a low
grade. A conformance claim asserted over a deployment that fails a precondition is void rather
than weak, and this distinction MUST be preserved in any conformance report.

### What This Specification Does Not Guarantee

ZTG guarantees the **attribution** of an exercise of authority, not its **quality**. That a
policy was adopted by an identified principal in a recorded act does not establish that the
principal understood it, deliberated over it, or exercised judgment worth the name. A
ratification that is attributable but inattentive is a real failure, and it is a failure this
architecture bounds rather than closes.

The boundary is stated here so that no conformance claim implies more. An implementation MUST
NOT represent attributable ratification as attentive ratification, and a conformance report
MUST NOT report the presence of adoption lineage as evidence of the adequacy of the
deliberation behind it.

The quality of ratification is a deployment obligation, borne by the Governed System. This
specification states it as **goals rather than mechanisms**, for a structural reason: any
specific control that could be mandated here — a sampling rate, a reviewer count, a
justification field — is arbitrary at the threshold and satisfiable in form while defeated in
substance. A requirement no assessor can evaluate is not a requirement; it is an invitation to
claim conformance over an unverifiable property, which is the failure this specification names
elsewhere as floor-washing.

The goals a deployment's ratification design is directed at are:

1. **Bounded load** — the volume and rate of decisions requiring ratification remain within
   what the ratifying principals can actually consider.
2. **Recorded basis** — the record captures the basis on which a ratification was given, not
   only that it was given.
3. **Detectable degradation** — a decline in the quality of ratification over time is
   observable by a party other than the ratifier.
4. **Structural distinctness** — the party ratifying an action is structurally distinct from
   the party proposing it, and does not derive its account of the action solely from the
   proposer.

A deployment MUST state how its ratification design addresses each goal, or state that it does
not address it and why. The conformance defect is **silence**, not the absence of any
particular mechanism: an unaddressed goal that is disclosed is a known, priced residual, while
an unaddressed goal that is not disclosed is a misrepresented claim. Methods of addressing
these goals are treated in the companion deployment guidance, which is interpretive and
mandates nothing.

### Composition

This section is a precondition on all of the others; it composes by being presupposed rather
than by being invoked.

The authorization model (§3) states that every authorization traces to human-attested
authority, either direct attestation or derivation from ratified policy, and that the model
admits no self-bootstrapped authority. §1 is where that premise is fixed; §3 is where it is
realized as the decision the boundary runs. §3 states the rule for the decision; §1 states the
condition on the deployment.

ZTG-0d (§8) provides the identity structure by which a ratifying principal is bound to an act
and by which delegation chains terminate at a principal rather than a system. ZTG-0e (§9)
provides the adoption act itself: a governance bundle is signed by a ratifying principal and
emitted as an authorized action, and a bundle that does not trace to a ratifying principal is
not adopted. §1 states as a scope condition what §8 and §9 enforce as mechanism.

ZTG-2 (§11) governs the case where the connection to authority is lost after operation begins.
Loss of the preconditions during operation is not a return to out-of-scope status — a
deployment that begins in scope and loses its authority linkage is a deployment that has lost
a positive guarantee, and MUST enter Stasis rather than continue issuing authority. Scope is
assessed at deployment; the guarantee is maintained continuously.

### Conformance Criteria

A conforming implementation can, for any authorization it has issued, exhibit: the policy
under which the decision was made; the adoption act by which that policy entered the
governance state; the ratifying principal bound to that act; and the path by which that
principal's authority may be revoked. It can state the boundary of its Governed System —
which parties are principals, and under what institutional structure — as a matter of record
rather than description.

An implementation that can exhibit a decision and its policy, but cannot exhibit the adoption
act behind the policy, does not meet this section. That gap is the failure mode this section
exists to make visible.

**Assessing a ratification-design statement.** The statement required above is a disclosure,
not a testable property, and it is assessed as one. The test is two-part: *did the deployment
disclose*, and *does the disclosure demonstrate an attempt to satisfy the goals it addresses*.
An assessor evaluates the disclosure, not the attentiveness of the ratifiers — the latter is
outside what any conformance procedure can establish, and a procedure claiming to establish it
is making the representation this section forbids.

The second part fails on **non-responsiveness**: a statement that restates a goal without
describing a design decision addressing it discloses nothing, and MUST be assessed as silence
rather than as a weak answer. A statement that declines a goal and gives its reason — a single
ratifying principal with no independent reviewer available, and the residual that leaves —
satisfies both parts. An honest declination conforms; an unresponsive affirmation does not.
This asymmetry is intended: the instrument is built to reward disclosure of a residual over
assertion of a control.

**Foundational commitments.** For binding at the point of execution, the
implementation exhibits, for every registered effect surface (ZTG-3), that the
surface's effect path is unreachable without a prior authorization record for that
specific effect (ZTG-4); a surface reachable by any path that lacks such a record
fails. For continuous ratification, the implementation exhibits, for any sampled
authorization, the governance-state version evaluated, the ratifying principal of
that version, and that the principal's ratification was unrevoked at the recorded
decision-time; an authorization for which any of the three cannot be produced fails.
For Invariant independence, the implementation exhibits that its authorization
verdict is reproducible by replay (ZTG-0b) from the sanitized proposal and the
governance state alone, with no Envelope-side input, and that each Invariant-layer
guarantee is asserted to hold under an arbitrary proposal source; a guarantee whose
stated conditions include any Envelope property — model version, alignment method,
evaluation score, or provider — fails as an Invariant guarantee and MAY be restated
as an Envelope property.
