# §14. Irreversibility of Harm (ZTG-5)

Irreversibility of Harm is the fifth and last system invariant (ZTG-1 through
ZTG-5). The other invariants govern whether and how an action reaches the world:
the boundary mediates it (ZTG-1), Stasis withholds authority when guarantees fail
(ZTG-2), the effect surface is closed and enumerated (ZTG-3), and effect and
evidence are coupled (ZTG-4). ZTG-5 governs the *consequence* dimension: it
requires every governed action to be classified by the restorability of the harm
it produces, and it makes that classification drive how stringently the action is
gated, ceilinged, and recorded.

## Operational Questions

ZTG-5 is the invariant mapped, in part, to **admissibility** — *was this action
actually authorized under valid, human-governed conditions appropriate to its
consequences?* — and it is the home of the **convergence test**, the discipline by
which an action's harm classification is checked rather than asserted. ZTG-5 also
feeds **replayability and evidence coupling**: its assessments are banded precisely
so they reproduce under ZTG-0b, and its required fields land in the ZTG-4 evidence
record. Where the other invariants answer "may this act occur and is it bound to
its evidence," ZTG-5 answers "how grave is it if it does, and is the architecture
treating it with gravity proportional to its irreversibility."

## Further Considerations

**The legal grounding: reparable and irreparable harm.** The distinction ZTG-5
draws is one equity worked out over centuries. Courts of equity issue an injunction
— they stop an act before it happens — precisely when a legal remedy after the fact
would be inadequate because the harm would be *irreparable*: a remedy in money
cannot restore what would be lost. The whole doctrine turns on the same line ZTG-5
draws, that the availability of compensation does not make a harm reparable, because
reparability is about whether the prior state can be restored, not whether a payment
can be offered for its loss. ZTG-5's three classes are this doctrine made
operational: Restorable harm is harm a legal remedy can actually undo, Irreversible
harm is the equitable category of the irreparable, and Mitigable sits between. That
the architecture routes Irreversible-class actions to a distinct, more stringent
gate is the mechanical analogue of equity intervening *before* the act rather than
compensating after it — because for irreparable harm, after is too late.

**The actuarial substrate property.** The banded, ceilinged, compositional
structure is what makes governed action *priceable*. Insurance and actuarial
practice require exposure to be expressible as discrete, bounded, composable
quantities; a risk that cannot be banded and bounded cannot be underwritten. By
requiring discrete bands, policy-assigned ceilings, and recursive compositional
multipliers, ZTG-5 produces a substrate over which exposure can be assessed
actuarially — not because the framework prices risk (it explicitly does not assign
the values), but because it produces the structural form priced risk must take. An
institution can attach its own actuarial values to ZTG-5's bands and ceilings; the
framework guarantees the bands and ceilings exist, are discrete, and compose
deterministically.

**Classification authority.** Harm classification is a governed declaration, not a
system judgment. The system does not decide that its own act is Restorable; the harm
class is declared on the surface by policy and attached to the action at routing.
This keeps ZTG-5 on the right side of the recurring line — the governed subject does
not author the inputs that govern it — and it locates the authority for
classification with the ratifying principal whose policy declares the surfaces.

**Composite irreversibility.** Irreversibility is not only a property of single
actions. A sequence of individually-Restorable actions can compose into an outcome
that is, in aggregate, irreversible, and the recursive faster-than-linear growth of
composite assessment is the mechanism that surfaces this. The framework does not
assume that safety at each step implies safety of the sequence; the composition
algebra is precisely the refusal of that assumption.

**Neutrality of composite records.** The composite assessment record is neutral
evidence: it records what the assessment was, under what multipliers and bands,
without itself asserting that the action was good or bad. This neutrality is what
lets the same record serve audit, actuarial pricing, and institutional review
without being tuned to any one of them.

**Iterative calibration of multipliers.** The multipliers and band thresholds are
expected to be calibrated iteratively against operational experience. This is a
policy activity under governance (ZTG-0e), not a system self-tuning loop: changing a
multiplier is a governance-state transition, authorized and recorded, never a
parameter the system adjusts for itself.

**Cross-surface composition.** When an action sequence crosses surfaces, the
composite assessment composes their multipliers, so exposure accumulated across
heterogeneous channels is captured rather than reset at each surface boundary. This
is what prevents laundering exposure by routing a sequence through many low-multiplier
surfaces.

**Stasis interaction.** The asymmetry between wrongly holding and wrongly proceeding
tracks harm class, and this is where ZTG-5 meets ZTG-2. Wrongly holding a
Restorable-class capability is recoverable; wrongly proceeding on an
Irreversible-class action under unestablished guarantees is not. The willingness to
enter Stasis, and the threshold for it, should reflect this asymmetry rather than be
uniform across harm classes. The precise coupling — whether Stasis sensitivity is
harm-class-aware — is a composition concern owned jointly with ZTG-2 (see Draft
Flags).

**Convergence test discipline.** A harm classification is admissible only if it can
be checked, and the convergence test is that check: independent assessments of an
action's harm class should converge, and a classification that cannot be
independently reproduced is not yet admissible. This is the discipline that keeps
classification honest — it is why classification is banded and recorded rather than
asserted, and it is the part of ZTG-5 that most directly serves the admissibility
question.

**Institutional binding through policy ratification.** Harm classes, multipliers,
and ceilings are all policy-set and ratified, which is what binds the institution to
its own consequence model. The ratifying principal's acceptance of a surface's harm
class and ceiling is an attested acceptance of responsibility for actions through
that surface — the chapter's connection back to the §1.0 thesis that every
authorization traces to a human-attested acceptance of responsibility.

**Adoption maturity.** Operating ZTG-5 well — calibrated multipliers, well-chosen
ceilings, surfaces classified to reflect real consequence — is a maturity an
institution grows into, not a switch it flips. The framework does not soften the
conformance requirement to fit institutions not yet ready to operate it; an
institution early in adoption runs ZTG-5 with conservative defaults and matures its
calibration, rather than running a relaxed ZTG-5.

## How We Do It (Constable reference implementation — non-normative)

Constable implements ZTG-5 as harm-class and ceiling declarations on its surface
registry, a composite-analysis subsystem that bands assessment deterministically,
and architecturally distinct gates for high-consequence actions.

**Surface and sub-surface registration.** Constable registers harm-class defaults
and compositional multipliers on surfaces and sub-surfaces in the same ZTG-3 surface
registry, carried in the ZTG-0e governance bundle. Default classifications ship as
*starting points*, not normative classifications: they are conservative defaults a
deploying institution is expected to review and tighten for its context, not
framework assertions about what a given surface's harm class is.

**Liability ceiling computation.** Ceilings are computed from deployment-level
policy and attached to each authorization request, then written into the ZTG-4
evidence record. Constable originates no ceiling itself; the values come from the
ratifying principal's policy. Harm-class assignment and ceiling assignment are
recorded as `HARM_CLASS_ASSIGNED` and `LIABILITY_CEILING_ASSIGNED` events under
ZTG-0a, so both are observable and replayable as of decision-time.

**Composite-analysis subsystem.** A composite-analysis subsystem computes assessment
as the recursive product of component assessments and surface multipliers, in
discrete bands, so the result replays identically through the ZTG-0b harness. No
continuous-valued computation enters the governance-determining path.

**Irreversible-class gates.** Constable routes Irreversible-class and over-threshold
actions to architecturally distinct high-end gates — separate gate structures, not
the ordinary gate with extra checks. HumanSeal presents high-consequence
authorizations to operators with the harm class, ceiling, and composite assessment
surfaced, so a human engaging an Irreversible-class action sees its gravity rather
than an undifferentiated approval prompt.

**Critical-class evidence binding.** Irreversible-class and over-threshold actions
are written as critical-class records on the Monotonic Logger, with the highest
durability and integrity the substrate supports, bound write-ahead of the effect per
ZTG-4. Mitigable-class actions record their residual harm.

**Operator support and certification.** Constable provides operator support for
calibrating multipliers and ceilings against experience, as a governed (ZTG-0e)
activity, and forthcoming certification covers whether a deployment's ZTG-5
configuration meets conformance. Conformance tests cover harm-class assignment,
monotonic sub-surface tightening, banded deterministic assessment and its replay,
distinct-gate promotion on either sufficient condition, ceiling presence in
evidence, and reversal_strategy non-relaxation. The protocol is documented in the
conformance verification specification referenced in §22.
