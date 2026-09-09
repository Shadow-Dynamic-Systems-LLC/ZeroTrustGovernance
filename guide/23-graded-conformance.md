# §23. Graded Conformance

Graded Conformance turns the verification methods of §22 into an assurance instrument. §22
specifies *how* an implementation demonstrates that a requirement holds; §23 specifies *what
the demonstration yields* when conformance is reported not as a single pass/fail bar but as a
position on a spectrum — a floor, a ceiling, and the nameable delta between them. This is the
resolution of §22's deferred binary-vs-graded question (`section-22…`, Draft Flags): ZTG
conformance is graded. The methods §22 defines are stable under that choice; §23 is where the
grade they produce is defined.

## Operational Questions

§23, like §22, is not mapped to one of the seven operational questions; it is the section that
states what a conformance *claim* asserts once the seven are individually demonstrable. Its
subject is the shape of the guarantee: that an implementation's conformance is a graded
statement of the architecture's maximum guarantee and how much of that maximum a given
deployment realizes — not a checkmark. Its discipline is that a grade which cannot separate
what the architecture can guarantee from what the deployment has operated is not a conformance
claim but a marketing one.

## Further Considerations

**The conformance ledger and the underwriting instrument are the same document.** Because the
ceiling is the failure profile of a diligent operator — bounded, evidenced, attributable — rather
than superhuman correctness, conformance grade tracks risk grade: the floor is *insurable at all*
(bounded but coarse), the ceiling is *finely priceable and settlement-capable*, and the min→max
climb is the curve a control warranty prices. Widening reach and pricing the delta are the same
move.

**Referee posture.** Defining the floor as a *category* — execution governance, earned by
surviving a named attack class — means other implementations can conform to it. This is a
standards-author position, not a product moat by exclusion; the moat is the reference
implementation at the ceiling plus ownership of the conformance instrument, not gatekeeping of
the floor.

**Relationship to §22.** §22's methods are indifferent to grading: a reachability argument, a
reproduction corpus, an injection result establish a property whether that property is scored
pass/fail or placed on a frontier. §23 depends on §22 for *how* each survival claim is
demonstrated; it adds only *how the demonstrated claims compose into a grade*.
