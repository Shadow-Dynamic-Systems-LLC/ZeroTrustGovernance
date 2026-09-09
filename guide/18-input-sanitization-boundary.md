# §18. Input Sanitization Boundary

The Input Sanitization Boundary is the input-side composition requirement (§4) detailed
in full. ZTG-1 states the limit it answers: the boundary cannot be more robust than the
inputs it evaluates. A deterministic gate evaluating malformed, ambiguous, or
adversarially-shaped input can produce a correct verdict on a misread of what was
actually proposed. §18 is the requirement that inputs are brought to a canonical,
validated form before evaluation, so that the gate evaluates well-formed inputs whose
meaning is unambiguous, and so that the form a later replay reconstructs is the form the
gate actually saw.

## Operational Questions

§18 is not one of the seven operational questions; it is a precondition for two of them.
It serves **execution-boundary enforcement** (with ZTG-1 and ZTG-3) by ensuring the
boundary mediates inputs whose meaning is determinate rather than inputs an adversary can
shape to be read two ways. And it serves **replayability** (ZTG-0b): the canonical,
post-sanitization input is the input the gate evaluated and the input replay
reconstructs, which is why §6 records the post-normalization input or pins the
normalization that produced it. An un-sanitized input path is both an enforcement gap and
a replay gap.

## Further Considerations

**The language-theoretic-security grounding.** A line of security research traced a large
class of vulnerabilities to a single habit: processing input before, or while, deciding
whether it is well-formed — the "shotgun parser" that interleaves recognition and action,
so that malformed or ambiguous input is partway processed before anyone has established
what it is. The discipline that answers it treats input as a formal language, places a
recognizer at the boundary that accepts only well-formed input and rejects everything
else *before* any processing, and refuses the equivalence-ambiguities that let one input
masquerade as another. §18 is this discipline at the governance boundary. Canonicalization
is the recognizer bringing input to one well-formed representation; fail-closed rejection
is the refusal to process what the recognizer cannot accept; the insistence that
sanitization precede evaluation is the refusal of the shotgun parser. The tradition's
core finding is the one §18 depends on: robustness against adversarial input is a property
of validating form fully at the boundary, not of handling malformed input gracefully
downstream.

**What sanitization can and cannot do.** §18 removes a structural attack surface; it does
not resolve a semantic one, and the chapter is precise about the line. Canonicalization and
validation ensure the gate evaluates the well-formed action an input actually encodes — they
defeat the *ambiguity* and *malformation* vectors. They do not, and cannot, certify that a
well-formed model proposal reflects what a user intended or that a manipulated model has not
been induced to make a well-formed but unwanted request. That residual is addressed
elsewhere in the architecture: by policy refusing the action (§3), by harm-class gating
routing it to human authority (ZTG-5), and by alignment work in the Envelope. §18's
contribution is bounded and stated as bounded — it makes the input determinate; it does not
make the proposer well-intentioned.

**Why the model's output is where the work is.** Among input classes, reasoning-system
output is the highest-volume and the most adversarially-influenced, because it is shaped by
whatever entered the model's context, including hostile content. Treating it as untrusted
input rather than as a privileged internal signal is the single most consequential stance in
§18. An architecture that sanitized external user input but trusted model output would have
sanitized the smaller surface and exempted the larger one.

**Relationship to replay.** The canonical form §18 produces is the anchor §6 relies on: by
recording the post-normalization input (or pinning the normalizer), the architecture makes
the gate's input reconstructable, so a replayed decision evaluates the input the gate saw
rather than a re-derivation of it. §18 and ZTG-0b meet exactly here, and the #8 reconciliation
in §6 is the other half of this requirement.
