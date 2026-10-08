# §22. Conformance Verification

## Normative

An implementation is ZTG-conformant to the extent that it satisfies the structural
prerequisites (ZTG-0a–0e) and the system invariants (ZTG-1–5), *and can demonstrate
that it does so by the methods specified in this section.* Satisfaction and
demonstration are distinct requirements: an implementation that meets a requirement but
cannot show it meets the requirement has not established conformance to that
requirement, because the property the framework sells is verifiability, and an
unverifiable guarantee is outside what the framework certifies.

Conformance is not self-certifying by assertion. A claim of conformance MUST be backed
by the evidence and procedures this section requires, such that a party who does not
trust the implementer can reach the same conclusion from the same evidence. The
substrate that makes this possible is the same substrate the prerequisites require:
because decisions are recorded (ZTG-0a), reproducible (ZTG-0b), and attributable
(ZTG-0d), a third party can re-derive conformance findings rather than accept them.

### Property Classes and Their Verification Methods

The requirements across ZTG are not all verified the same way, and a single uniform
method — "run a test suite" — is insufficient for several of them. §22 distinguishes the
classes of property the framework asserts and specifies the method each admits.

**Reachability and structural properties.** Some requirements assert the *absence of a
path*: no agent-to-execution route bypasses the boundary (ZTG-1); no reachable effect
channel is unregistered (ZTG-3); no ambient effect authority exists (ZTG-3). These
cannot be established by testing, because testing exercises paths that exist and cannot
demonstrate that no other path does. They MUST be verified by architecture-level
reachability analysis: a demonstration over the implementation's structure that the only
reachable paths to the world traverse the mediated, registered surface. An
implementation MUST be able to present its effect-reachability argument, not merely a
suite of passing effect tests.

**Reproduction properties.** Some requirements assert that a result *regenerates*:
replay reproduces a verdict (ZTG-0b); banded assessment recomputes identically (ZTG-5);
an admissibility determination is independently reproducible (§3). These are verified by
re-execution over a recorded corpus and comparison: regenerate the determination from
its substrate under the pinned procedure and confirm identity with the recorded result.

**Negative-space and absence properties.** Some requirements assert that *missing
things are detected*: an expected record absent on an action path is a violation
(ZTG-0a); an effect lacking committed evidence is an orphan to be caught (ZTG-4). These
are verified by injection — deliberately producing the absent condition and confirming
the implementation raises it as a violation rather than passing it as ordinary missing
data. For the ZTG-4 no-orphan direction specifically, the demonstration is that
completion records are emitted only after dispatch on the isolated coupling path, so the
absence of a corresponding effect for a completion record cannot arise silently (per
§13's authorizing-vs-completion division).

**Fault-injection properties.** Some requirements assert a *response to loss of
guarantee*: Stasis fires on each trigger (ZTG-2); a partitioned gate fails closed
(ZTG-0e); the write-ahead crash window yields a recorded indeterminate effect, never a
silent gap (ZTG-4). These are verified by injecting the fault and confirming the
fail-closed response — including that a held scope lifts only on a legitimate
resolution, that recovery from control-plane Stasis requires ratified authority, and,
for tamper-family triggers, independent re-verification (ZTG-2 Exit Path Integrity).

**Integrity properties.** Some requirements assert *tamper-evidence*: governance records
cannot be silently altered (ZTG-0a); the coupling path cannot be severed by the
reasoning system (ZTG-4). These are verified by adversarial attempt — altering,
deleting, or inserting records, and attempting to dispatch an effect while suppressing
its evidence — and confirming detection.

An implementation's conformance evidence MUST address each requirement by the method its
property class admits. A reachability property demonstrated only by passing tests, or an
integrity property demonstrated only by analysis, is not adequately demonstrated.

### Closure Verification

The hardest structural demonstration is ZTG-3 closure: that no reachable effect channel
is unregistered. §22 specifies it as a reachability obligation. The implementation MUST
exhibit its complete set of effect channels and an argument that every reachable path
from the governed system to an externally observable effect terminates in a registered
surface — equivalently, that the capacity to produce an unregistered effect does not
exist as an ambient capability (ZTG-3). The argument is over the architecture, and its
completeness is the conformance burden: ZTG-3 reframes "have we listed every effect" as
"is there any reachable path outside a registered surface," and §22 is where that
reachability question is discharged for a given implementation. Discovery, by analysis
or at runtime, of a reachable unregistered channel is a closure breach and a Stasis
trigger (ZTG-3), not a finding to be quietly registered away.

### The Convergence Test

The convergence test is the method by which an admissibility determination (§3) — and
the harm classification within it (ZTG-5) — is shown to be checkable rather than
asserted. The test requires that an independent assessment of a request, performed over
the recorded substrate and not sharing state with the original evaluation, converge on
the same determination. Convergence is the conformance evidence for §3's claim that
admissibility is reproducible; divergence between independent assessments of the same
recorded request is a conformance failure, surfaced for investigation.

The independent assessment MUST draw only on the recorded substrate — recorded inputs,
pinned policy and engine, pinned snapshot — and MUST NOT consult the live system or
re-run the reasoning model, for the same reasons replay does not (ZTG-0b): an assessment
that re-derived its inputs from the live system would be checking the system against
itself. The precise criteria for convergence — exact-match on verdict and harm class,
and the tolerance, if any, permitted on banded composite assessment — are specified
below as an open calibration item; the requirement that independent assessment converge,
and that non-convergence be a conformance failure, is settled.

### Conformance of Non-Reference Implementations

The specification is open: Constable is the reference implementation, and any
implementation satisfying the prerequisites and invariants is ZTG-conformant (Scope).
§22 is what makes that claim operational for a non-reference implementation. A
non-reference implementation demonstrates conformance by exhibiting, for each
requirement, the evidence its property class requires — its reachability arguments, its
reproduction corpus and harness, its injection and adversarial results — over its own
architecture. Conformance is to the specified invariants and prerequisites, not to
Constable's mechanisms: an implementation that achieves complete mediation, closure,
evidence coupling, and the rest by different means than Constable is conformant if its
evidence establishes the properties, and Constable's particular choices (OPA/Rego,
the Monotonic Logger, HumanSeal) are not themselves conformance requirements.

### Scope and Partial Conformance

An implementation's conformance claim MUST state the scope over which it holds — which
effect surfaces, which action classes, which deployment. A demonstration that covers a
subset of an implementation's effectful actions establishes conformance for that subset
only; the unscoped remainder is not conformant by extension. Consistent with the
framework's posture elsewhere, §22 does not soften a requirement to fit an implementation
not yet able to demonstrate it: an implementation that cannot yet exhibit closure over
its full effect surface is partially conformant over the surface it can, not fully
conformant over all of it. Silent scope limitation — claiming conformance while bounding
coverage without saying so — is itself a conformance defect.

### Reconciliation with the minimum-conformance matrix

The ten prerequisite and invariant chapters (§5–§14) each state their own conformance
criteria; the ZTG v0.8 Minimum-Conformance Matrix
(`ZTG-V0.8-MINIMUM-CONFORMANCE-MATRIX-001`, sds-architecture, advisory — not yet adopted)
is the cross-cutting instrument that restates those ten criteria in one shape: protected
condition, minimum guarantee, required evidence, test oracle, three-valued result (HOLDS /
VIOLATED / INDETERMINATE), Stasis consequence, and permitted scope limitation. The matrix
adds no new requirement and no new verification method: every one of its ten
`test_oracle` fields is tagged by which property class defined above it instantiates, so
every prerequisite and invariant criterion this section verifies maps to exactly one
matrix row.

| Requirement | §22 property class | Matrix row |
|---|---|---|
| ZTG-0a Observability | negative-space / integrity | Prerequisite Matrix, ZTG-0a |
| ZTG-0b Replayability | reproduction | Prerequisite Matrix, ZTG-0b |
| ZTG-0c Temporal Integrity | fault-injection / integrity | Prerequisite Matrix, ZTG-0c |
| ZTG-0d Identity Integrity | adversarial attempt / reproduction | Prerequisite Matrix, ZTG-0d |
| ZTG-0e Governance Consistency | fault-injection | Prerequisite Matrix, ZTG-0e |
| ZTG-1 Mechanistic Boundary | reachability | Invariant Matrix, ZTG-1 |
| ZTG-2 Stasis | fault-injection | Invariant Matrix, ZTG-2 |
| ZTG-3 Governed Effect Surface | reachability | Invariant Matrix, ZTG-3 |
| ZTG-4 Evidence-Coupled Execution | negative-space / fault-injection | Invariant Matrix, ZTG-4 |
| ZTG-5 Irreversibility of Harm | reproduction / convergence | Invariant Matrix, ZTG-5 |

A matrix row's three-valued result is produced by applying this section's method for that
row's property class to the matrix's `required_evidence` field; the matrix does not
license a different verification method than the one this section specifies for that
class. The matrix's INDETERMINATE state is this section's own discipline, generalized: a
reachability argument, reproduction corpus, or injection result that is absent or cannot
be run to completion does not default to a pass, whether reported here or in the matrix.

The matrix also names, for the ZTG-1/boundary-adjacent rows, the boundary determinism
amendment as a further constraint: `ZTG-V0.8-UPSTREAM-RESTRICTION-BOUNDARY-DETERMINISM-001`
(ARCH-ZTGC-04, sds-architecture, advisory — resolves A-S3) distinguishes upstream
restriction (heuristic, probabilistic, or banded triage that may suppress a proposal
before it reaches the boundary) from the boundary's own deterministic evaluation. A
proposal an upstream stage suppresses generates no boundary verdict and no boundary
evidence result; its exclusion MUST NOT be cited as evidence of boundary conformance. This
section's reachability method for ZTG-1 and the amendment's Determinism Requirement
compose directly: the reachability argument establishes that no path bypasses the
boundary, and the amendment's determinism replay test — re-running boundary evaluation on
fixed pinned inputs and adopted policy state and confirming byte- or hash-identical
verdicts and evidence results — is this section's reproduction-class method, applied to
the boundary specifically rather than to the recorded corpus generally. The amendment
fixes exact-match as the criterion for that replay test; it does not fix the separate,
still-open banded-composite tolerance question for ZTG-5/§3 convergence (Draft Flags,
below).

Both the matrix and the amendment are architecture-advisory drafts, not adopted ZTG text.
This section cites them as the reconciliation target, not as ratified requirements,
consistent with this section's own discipline of not inventing resolutions the source
chapters have not adopted.

### Reciprocal cross-reference to Section 23

§23 (Graded Conformance) states its dependency on this section: "§23 depends on §22 for
*how* each survival claim is demonstrated; it adds only *how the demonstrated claims
compose into a grade*." This section's own Draft Flags previously carried the reciprocal
question as open ("Binary vs. graded conformance is unresolved here ... reconcile §22's
framing with that work when it lands"). §23 has since landed as a normative stub with its
grade unit fixed (a per-invariant frontier over the adopted attack-class registry, rolling
up into named tiers), so the reconciliation is stated here:

This section's methods are indifferent to how their results are scored. A reachability
argument, a reproduction corpus, an injection result, or an adversarial-attempt finding
establishes HOLDS/VIOLATED/INDETERMINATE for one requirement regardless of whether that
requirement's result is reported as a binary pass/fail or composed, per §23, into a
per-attack-class closed/bounded/open frontier. §23 grades the same evidence this section
specifies how to produce; it does not require a different evidence shape, and this section
does not need to adopt a grading posture itself to be complete. The question is resolved
by composition, not by either section absorbing the other: §22 verifies, §23 grades,
neither substitutes for the other — the same three-instrument split the minimum-conformance
matrix states explicitly in its own "Relationship to §22 and §23" (see Reconciliation with
the minimum-conformance matrix, above).

### Conformance Criteria

A conforming verification regime can: classify each ZTG requirement by property class
and apply the admitting method; present effect-reachability arguments for the structural
properties (no-bypass, closure, no-ambient-authority); regenerate recorded
determinations under pinned procedure and confirm reproduction; inject negative-space
and fault conditions and confirm violation-handling and fail-closed response; attempt
tamper and confirm detection; demonstrate independent convergence on recorded
admissibility determinations; and state the scope over which the conformance claim
holds, without silent limitation.
