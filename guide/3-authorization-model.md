# §3. The Authorization Model

The Authorization Model specifies the decision at the center of the framework: how a
proposed action becomes — or fails to become — an authorized governed effect. The
other normative sections specify the parts the decision composes. The Mechanistic
Boundary (ZTG-1) specifies the structural separation the decision sits inside; Identity
Integrity (ZTG-0d) specifies whose authority the decision recognizes; Irreversibility
of Harm (ZTG-5) specifies the consequence dimension the decision is graded against; the
structural prerequisites specify the recorded, reproducible, temporally-anchored,
consistent substrate the decision runs over. §3 specifies the decision that binds them
into a single verdict.

## Operational Questions

§3 is the section mapped to **admissibility** — *was this action actually authorized
under valid, human-governed conditions?* It owns the general form of that question;
ZTG-5 owns the consequence-specific portion of it (harm class, ceiling, gate). §3 is
also where the **convergence test** is situated as the discipline that keeps an
admissibility determination checkable rather than asserted, with its full method
deferred to §22. The authorization model conditions every other operational question,
because each of them — evidence coupling, fail-closed semantics, replayability,
governance continuity, override visibility, execution-boundary enforcement — is a
property of, or a precondition for, the authorization decision this section defines.

## Further Considerations

**The reference-monitor grounding.** Security engineering arrived, half a century ago,
at the conditions a component must meet to be trusted to mediate access: it must be
invoked on every access (complete mediation), it must be tamperproof, and it must be
small and simple enough to be verified. The authorization model is the reference
monitor for a governed autonomous system's effects on the world. Complete mediation is
ZTG-1; tamperproofing is the boundary's isolation from the reasoning it gates;
verifiability is replay (ZTG-0b) and the convergence test. The discipline is the same
one the reference-monitor concept established — a mediator you cannot bypass, cannot
tamper with, and can independently check — applied to authorization rather than to file
access. The older idea sets the bar; §3 is what clears it for this domain.

**Admissibility is not correctness.** The model guarantees that an authorized action was
permitted under valid human-governed conditions. It does not guarantee that the action
was wise, optimal, or good. A correctly-authorized action can still be a mistake — the
policy that permitted it may have been ill-judged, the principal who attested it may
have erred. The framework is precise about which of these it provides: it makes
consequential action *governed and attributable*, so that a mistake has a responsible
author and a reconstructable basis, not that mistakes do not occur. Conflating
admissibility with correctness would overclaim; the model's value is that it makes the
governance of an action a checkable fact, which is the precondition for holding anyone
to account for the action's merits.

**Refusal is the common case, and that is the design.** Because the default disposition
is refusal and admissibility is a conjunction of conditions every one of which must
hold, most evaluations end in refusal, and the refusals carry most of the diagnostic
information about how the boundary behaves under pressure (ZTG-0a). A model that
authorized by default and refused by exception would invert the burden of proof the
framework places on action: under ZTG, action bears the burden of establishing its
admissibility, not the architecture the burden of establishing a reason to refuse.

**Escalation as the third path.** Much of the value of the model is in not collapsing
the verdict space to grant-or-refuse. A two-valued model forces every decision policy
wishes to reserve for human judgment into either a mechanical grant or a refusal that
reads as inadmissibility. The third verdict is what lets the architecture route a
decision to human authority as a positive act — the human engaging the decision the
policy chose to reserve for them — rather than as a failure of the machine to decide.
