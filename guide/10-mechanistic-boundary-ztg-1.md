# §10. Mechanistic Boundary (ZTG-1)

The Mechanistic Boundary is the first system invariant (ZTG-1 through ZTG-5). It
specifies the deterministic separation between reasoning and irreversible action —
the structural point through which every model-derived action must pass to become
an effect in the world.

## Operational Questions

ZTG-1 is mapped, with ZTG-3, to **execution-boundary enforcement**: where synthetic
reasoning stops and materially consequential execution begins. ZTG-1 is the gate
every proposed action must pass through; ZTG-3 (Governed Effect Surface) is the
closed set of channels there are to act through. Together they answer the boundary
question in full — ZTG-1 mediates every action, and ZTG-3 guarantees there is no
unmediated way to act. ZTG-1 also conditions **replayability and evidence
coupling**: every boundary decision is recorded (ZTG-0a), reproducible (ZTG-0b),
and, where it authorizes an effect, coupled to that effect's evidence (ZTG-4).

## Further Considerations

**Boundary as architectural primitive.** The Mechanistic Boundary is not a
service the governed system uses when it wants to behave responsibly. It is the
structural separation through which actions must pass. This mirrors
imaginative-to-executive separation in biological cognition: imagination does
not optionally invoke a review function; outputs cannot reach motor execution
without traversing executive function.

**Speculative execution and the boundary.** Speculative execution of
irreversible actions is irreversible execution. Implementations supporting
speculative execution must restrict it to actions whose ZTG-5 harm class is
Restorable and whose computed assessment is below thresholds where
stratification applies. Gradient speculation, partial commits, and optimistic
concurrency with compensating actions are non-conforming for Irreversible-class
actions regardless of performance benefits.

**Defining what counts as external to the model.** The boundary presupposes a
definable distinction between model and external action. Token streaming, tool
use mid-generation, and memory writes can make the distinction subtle.
Implementations should declare their externality boundary explicitly and apply
it consistently. The conservative choice is to treat any output crossing an
architectural component boundary as external.

**Borderline side effects.** Cache changes, internal parameter updates during
inference, logs consumed by other systems, and observable resource-allocation
patterns may be internal operations or boundary-relevant actions depending on
implementation context. Implementations should produce explicit determinations
for each borderline operation type and document them as part of conformance
verification.

**Model architecture interaction.** Mid-generation actions are still actions.
Architectures executing tool calls within inference context, without boundary
involvement, are not ZTG-1 conformant. Tool-call proposals must route through
the boundary before invocation.

**Performance and the temptation to relax.** Boundary evaluation introduces
latency. Caching authorization decisions across requests, bypassing the
boundary for "obviously authorized" actions, or using reduced evaluation paths
are non-conforming. Performance constraints must be addressed by preserving the
discipline: scaling boundary capacity, authorized batching, pre-computation, or
optimization within the evaluation path.

**Adversarial inputs and boundary robustness.** The boundary cannot be more
robust than the inputs it evaluates. Input sanitization is handled by
composition requirements, especially the Input Sanitization Boundary in §18.
ZTG-1 specifies structural boundary properties and depends on composing
requirements for input handling.

**Boundary semantics across action classes.** Boundary discipline does not vary
across action classes, but consequences do. ZTG-5 may impose stricter gate
requirements for Irreversible or over-threshold actions. The boundary's
discipline of complete mediation, deterministic evaluation, and audit emission
remains uniform.

**Boundary and Stasis interaction.** During Stasis (ZTG-2), the boundary becomes
more restrictive, not less: Stasis is the state in which no new authority is
granted, so the boundary grants nothing while held. The boundary refuses
authorization when the system cannot guarantee invariants hold. Operational
pressure to bypass during Stasis is expected; refusal is the architecture
functioning as designed.

## How We Do It (Constable reference implementation — non-normative)

Constable implements the Mechanistic Boundary through architectural separation
between the agent loop and the execution surface. The policy evaluation gate is
structurally placed between these layers, with no path from agent to execution
that does not traverse the gate.

**The execution gate.** Constable's gate is separate from the agent runtime. It
runs in its own process boundary, evaluates policies using OPA/Rego, and
communicates decisions to the action surface through a channel the agent runtime
cannot intercept. The gate's code is separately auditable, deployed, and
versioned from the agent code.

The gate evaluates one action at a time. Each evaluation is atomic with respect
to policy state. The result is a verdict (`authorize`, `refuse`, `escalate`)
bound to the specific action, policy version, and timestamp.

**OPA/Rego as evaluation surface.** Constable uses OPA with Rego policies. OPA
provides deterministic policy evaluation with policy code that is auditable,
version-controlled, and replayable. Rego's evaluation model is decidable and
side-effect-free. Other policy languages with equivalent properties can also be
conforming implementation choices.

**Integration with Airlock.** Constable composes with Airlock for input
sanitization. All policy-evaluation inputs route through Airlock normalization
before reaching the evaluator. The gate accepts only Airlock-processed inputs.

**Memoria promotion gate.** Constable composes with Memoria through Memoria's
promotion gate. Raw memory contents are not visible to policy evaluation.
Memory contents consulted by policy must be promoted through explicit protocol
requiring named human attestation.

**Tool call routing.** Constable routes tool calls produced during inference
through the execution gate before invocation. The model produces tool-call
proposals; the gate evaluates them; only authorized proposals invoke tools.

**Performance optimization within discipline.** Constable preserves boundary
discipline while improving latency through policy pre-compilation, parallel
evaluation of independent policies, input caching at the normalization boundary,
and audit emission batching where durability is preserved. Authorization
decisions are not cached across requests.

**Conformance verification for ZTG-1.** Constable's internal testing includes:

- Path analysis verifying no agent-to-execution bypass.
- Replay testing for identical decisions from identical inputs.
- Adversarial input testing under malformed and ambiguous inputs.
- Tool-call interception testing.
- Memory-bypass testing.
- Stasis interaction testing.
- Performance testing verifying discipline under load.

The testing protocol is documented separately in the conformance verification
specification referenced in §22.
