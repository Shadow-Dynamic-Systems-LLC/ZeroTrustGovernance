# §22. Conformance Verification

Conformance Verification is the section every other section defers to. Each
prerequisite and invariant states what an implementation must do and closes with the
tests that demonstrate it does; §22 specifies what those demonstrations must establish,
and by what method, so that conformance to ZTG is itself a checkable fact rather than an
asserted one. This is not a peripheral appendix. The framework's central claim is that
it produces *checkable* governance — governance an auditor, a counterparty, or a court
can independently verify, not merely a system's account of its own good behavior — and
that claim is only as strong as the verification §22 defines. Until conformance can be
demonstrated, every "Conformance Criteria" list in the preceding chapters is a statement
of intent.

## Operational Questions

§22 is not mapped to one of the seven operational questions; it is the section that
makes all seven *verifiable*. Each question is answered by some prerequisite or
invariant, and §22 specifies how an implementation demonstrates that the answer holds:
how it shows admissibility is actually established before a grant, that fail-closed
semantics actually fire, that replay actually reproduces, that the effect surface is
actually closed. The section's subject is therefore the verifiability of the whole, and
its discipline is that a guarantee which cannot be demonstrated is, for governance
purposes, not yet a guarantee.

## Further Considerations

**The assurance-case grounding.** Safety-critical and high-assurance engineering long
ago stopped accepting "we tested it" as a sufficient account of why a system can be
trusted, and developed the assurance case: an explicit, auditable argument that a
system meets its claims, structured so the claims decompose into sub-claims and bottom
out in evidence a reviewer can examine. Independent-evaluation regimes — the kind that
certify a cryptographic module or an avionics component — institutionalize the same idea:
the developer does not certify their own product by assertion; an independent party
reaches the conclusion from the evidence. §22 asks an implementation to assemble exactly
this: a structured argument that each ZTG requirement holds, decomposed by property
class, bottoming out in reachability analyses, reproduction corpora, and injection
results a party who distrusts the implementer can re-examine. The tradition's central
lesson is the one §22 encodes — that testing demonstrates the presence of behavior, not
its absence, so the absence claims (no bypass, no unregistered channel, no silent gap)
require argument and analysis, not test counts.

**Verifiability is the product.** It is worth stating plainly why this section carries
the weight it does. A system can satisfy every ZTG requirement and still deliver little
if it cannot show that it does, because the institutional value the framework offers —
to a regulator, an underwriter, a court — is not that the system behaves well but that
its behavior is *demonstrable*. Governance that must be taken on the operator's word is
the retrospective, advisory posture the introduction rejects (§1.2), dressed in
technical language. §22 is where the framework's difference from that posture is
cashed: the guarantees are constructed so that a third party can confirm them, and the
confirmation procedure is itself specified rather than left to the implementer's
discretion.

**Self-certification and its limits.** An implementation can run its own conformance
regime, and Constable does. But self-administered evidence is only as trustworthy as
the substrate it rests on, which is why the framework invests so heavily in records that
are tamper-evident (ZTG-0a) and determinations that are independently reproducible
(ZTG-0b, §3): these are what let a self-administered claim be *re-checked* by an outside
party rather than merely believed. The framework's posture is referee-shaped: it
specifies the conditions under which conformance can be independently confirmed, so that
self-certification and third-party evaluation rest on the same evidence and reach the
same finding.

**Reachability completeness is irreducibly architectural.** The recurring hard problem,
named in ZTG-1 and ZTG-3 and concentrated here, is establishing an absence-of-path claim
over a real system. §22 does not pretend this is mechanical. The completeness of a
reachability argument depends on the implementation's architecture being analyzable —
which is itself a design property an implementation must choose, and a reason the
framework prefers architectures whose effect surface is small, explicit, and
structurally closed rather than large and conventionally monitored. An implementation
that makes its effect reachability hard to analyze has made its conformance hard to
establish, and the framework treats that as the implementation's burden, not a gap in
§22.
