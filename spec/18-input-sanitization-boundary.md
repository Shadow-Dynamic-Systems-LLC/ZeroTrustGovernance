# §18. Input Sanitization Boundary

## Normative

Every input that reaches governance evaluation MUST first pass the Input Sanitization
Boundary, and the gate MUST accept only sanitized inputs. There is no input path into
evaluation that bypasses sanitization. Sanitization brings an input to a canonical
validated form, rejects input that cannot be brought to such a form, and records what it
did.

### Normalization to Canonical Form

Inputs MUST be normalized to a canonical representation before evaluation, such that
semantically-equivalent inputs normalize to the same form and evaluate identically. The
purpose is to remove the representational ambiguity adversarial inputs exploit: encoding
tricks, equivalent-but-different spellings of a target, hidden or duplicated fields, and
the many ways one effective request can be made to look like another. A policy evaluated
against a non-canonical input is evaluating against one reading of an input that has
several, and the reading the gate takes need not be the reading that produces the effect.
Canonicalization collapses those readings to one before the gate decides.

### Validation and Rejection

Input that cannot be normalized to a valid canonical form MUST be refused, not evaluated
on a best-effort basis. Sanitization is fail-closed: an input the boundary cannot bring to
a well-formed, validated representation is rejected as malformed, and the rejection is
recorded. The architecture does not guess at the intended meaning of a malformed input and
proceed on the guess, because a guess is exactly the ambiguity an adversary supplies the
input to create.

### Model Output Is Untrusted Input

The reasoning system's output is input, and it is the central case. Under §4 the reasoning
system composes as a proposer outside the trust boundary, so its outputs — tool-call
proposals, action parameters, target specifications — are untrusted input and MUST pass
sanitization before they enter an authorization request (§3). This is where the structural
attack surface of prompt injection and manipulated model output is addressed: §18 does not
make the model trustworthy, and it does not certify that the model's proposal reflects the
user's intent; it ensures the proposal reaches the gate in canonical, validated,
bounded form, so that whatever the model was induced to emit is evaluated as the
well-formed action it actually is, against policy, at its true harm class. The model's
output earns no exemption from sanitization by virtue of originating inside the deployment.

### Sanitization Is Not Authorization

§18 validates form; it does not decide admissibility. A perfectly sanitized input can be,
and often is, refused by policy (§3): canonical form is a precondition for the gate to
decide correctly, not a determination that the input should be granted. The two MUST NOT
be conflated. Sanitization that began making policy decisions would be a second,
undocumented authorization surface; admissibility belongs to the authorization model, and
§18 delivers it inputs it can decide on, nothing more.

### Determinism and Provenance

The normalization transform MUST be deterministic, and either its output (the
post-normalization input) MUST be recorded as the replay input or the transform version
MUST be pinned alongside policy and engine (ZTG-0b, §6). A nondeterministic or
silently-drifting normalizer would make verdicts non-reproducible for reasons unrelated to
any governance decision. Each sanitization MUST emit input-normalization evidence
(`INPUT_NORMALIZED`, ZTG-0a) carrying the provenance of the sanitized input: what raw
input it derived from and what normalization was applied, sufficient to reconstruct the
gate's input under replay.

### Scope

Sanitization applies to every input class that reaches evaluation: end-user input,
reasoning-system output, promoted memory content (ZTG-1), and external data drawn into the
decision. The boundary-scope subtleties ZTG-1 names — reads whose access pattern signals a
target, mid-generation tool calls, memory writes consulted elsewhere — are input surfaces
as much as effect surfaces, and an input crossing into evaluation through any of them is
subject to §18.

### Conformance Criteria

A conforming implementation can: demonstrate that no input reaches evaluation without
passing sanitization; demonstrate canonicalization, such that semantically-equivalent
inputs normalize identically; refuse malformed and un-normalizable input fail-closed and
record the refusal; sanitize reasoning-system output as untrusted input before it enters a
request; demonstrate that sanitization makes no admissibility decision; demonstrate that
its normalizer is deterministic and that the replay input is the canonical form or the
normalizer is pinned; and emit `INPUT_NORMALIZED` provenance sufficient for replay.
