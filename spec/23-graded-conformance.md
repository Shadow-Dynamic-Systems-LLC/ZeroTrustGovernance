# §23. Graded Conformance

## Normative

Conformance to ZTG is **graded**, not binary. A conformance claim states a position on a
spectrum whose floor is *execution governance* and whose ceiling is the maximal guarantee the
architecture commits to. The spectrum is graded by **which attack classes a deployment is
designed to survive** — the laundering channels enumerated in the framework's threat model —
so that the delta between two claims is a specific, nameable set of adversaries rather than a
vague "more assurance."

### The Floor

The floor is *execution governance*, defined not by having a boundary but by the attack class
a boundary must survive to earn the name: spontaneous defection / trust-decay-across-regime-shift.
A deployment is execution governance iff (a) the bound on effects that can reach the world does
not depend on the model's good behavior; (b) the bound holds no ambient authority around it, so
the registered surface is the only reachable route by construction (structural closure, ZTG-3);
and (c) it produces enough external, non-self-authored record (ZTG-0a) to demonstrate (a) and
(b) over the enumerated effect surface. The floor is the irreducible core — ZTG-1 + ZTG-3 +
ZTG-0a jointly — and these three do not grade independently. Full development in the design note
(§1); this section carries the floor by reference and does not restate its derivation.

### Survival Is Three-Valued

A grade reports, per attack class, one of three states: **closed** (the class is survived under
complete mediation), **bounded** (survived only to a named, non-zero residual), or **open** (not
survived). A grade that claims "survives X" when it only bounds X to a residual is floor-washing;
the instrument MUST report the residual, not a checkmark. Some classes never reach closed and are
inherently bounded (e.g. hollow ratification — attribution, not attentiveness).

### The Grade Is a Frontier Over a Partial Order

Attack classes form a partial order, not a flat menu: surviving a downstream class requires its
upstream preconditions closed. A grade is therefore a **frontier** over that dependency graph,
and a claim MUST NOT report a downstream class as survived while an upstream precondition it
depends on is open.

### Ceiling and Coverage Are Distinct Deltas

A conformance claim MUST state two things and MUST NOT conflate them:

- the **ceiling delta** — which attack classes, and at what strength, the *architecture* commits
  to at all; and
- the **coverage delta** — how completely a given *deployment* realizes them.

A low ceiling cannot be operated into strength, and a high ceiling is not a realized guarantee.
The reachable-unregistered channel set is a **coverage** matter, borne by the deployer: the
mechanism's no-ambient-authority (floor (b)) relocates and shrinks it but does not close it, and
per §22 the gate cannot self-certify its own enumeration completeness (it produces no evidence
for what bypasses it). Enumeration completeness and the scope of a claim are therefore handled by
§22 (Scope and Partial Conformance), and a grade inherits that scope statement rather than
restating it. Silent scope limitation is a conformance defect there and here.

### The Grade Unit

A grade is reported **per-invariant**. The system of record is a survival frontier per invariant
(closed / bounded / open over the channel partial order). Named tiers are a **derived view** over
those frontiers and MUST NOT be reported as a substitute for them — the same discipline ZTG-0a
applies to metrics-vs-record (§5): a tier is a downstream summary of the frontier, never the record
itself.

A named tier T is a **defined cut** over the partial order: an implementation is at tier T iff, for
every attack class up to T's frontier, survival is at least **bounded**, with **closed** where T
claims closure, and no downstream class is claimed while an upstream precondition it depends on is
open. A tier claim inherits the ceiling/coverage split and the §22 scope statement — it states the
tier the *architecture* reaches and the coverage a *deployment* realizes against it, and MUST NOT
report a tier the deployment's coverage does not support.

### Adopted Attack-Class Registry

The attack-class partial order referenced above ("The Grade Is a Frontier Over a Partial
Order", "Ceiling and Coverage Are Distinct Deltas") is populated by the adopted attack class
registry prepared by sds-adversarial under ADV-ZTGC-01
(`ZTG-V0.8-ADOPTED-ATTACK-CLASS-REGISTRY-CANDIDATE.md`, version 0.8-candidate-1). Twelve
classes, each stating a testable protected condition, its invariant/prerequisite mapping, its
dependencies on other classes, and a named residual limitation:

- **ZTGC-AC-01** Applicability Prerequisite Forgery — prerequisites 1–4; ZTG-0d, ZTG-0e;
  foundational, no dependencies.
- **ZTGC-AC-02** Identity/Attribution Substitution — ZTG-0d; depends on AC-01.
- **ZTGC-AC-03** Governance State Drift — ZTG-0e; compounds with AC-05.
- **ZTGC-AC-04** Intent-as-Authorization Substitution — ZTG-1; no dependencies, the core ZTG-1
  attack surface.
- **ZTGC-AC-05** Uncertainty-State Authority Grant — ZTG-2; interacts with AC-03.
- **ZTGC-AC-06** Ambient/Composed Effect Path — ZTG-3; no direct dependencies, the usual
  cash-out point once AC-01/AC-02/AC-04 succeed.
- **ZTGC-AC-07** Post-hoc Evidence Substitution — ZTG-4; depends on AC-08.
- **ZTGC-AC-08** Observability Hollowing — ZTG-0a; upstream of AC-07 and AC-09.
- **ZTGC-AC-09** Replay Denial — ZTG-0b; depends on AC-08.
- **ZTGC-AC-10** Temporal Scope Carryover — ZTG-0c; depends on AC-03.
- **ZTGC-AC-11** Reversibility Misclassification — ZTG-5; consumes the output of AC-04 and
  AC-06.
- **ZTGC-AC-12** Human-Layer Authority Capture — §3 authority genealogy, ZTG-0d (human side);
  depends on AC-01 and AC-02.

Every applicability prerequisite and every ZTG-0a–0e / ZTG-1–5 invariant maps to at least one
class; the full quick-lookup matrix is carried in the source registry and not reproduced here.
Sections 22–23 are themselves out of registry scope by construction: they govern how
conformance is checked and tiered, not what is attacked.

The registry carries candidate status only. It was prepared under a one-time sds-adversarial
authorization (bce7021d-b37e-464b-a4f8-989e6fc33d32, 2026-09-07) to produce a candidate;
sds-adversarial does not adopt it and does not approve ZTG. Adoption, if any, follows the
ordinary policy chain (Strategy → Meta → Founder). §23's grading machinery is written to
operate against whatever registry version is adopted; this candidate is the first version
populating it, not a ratified input.

### Versioned and Non-Exhaustive Scope

A conformance claim graded under "The Grade Unit" MUST cite the registry version it was graded
against. The registry is explicitly non-exhaustive: later versions may add attack classes as
corpus evidence accumulates, and a grade computed against an earlier version does not
retroactively cover classes a later version adds. Non-exhaustiveness is not a license to leave
a declared in-scope effect path unregistered — ZTGC-AC-06 (Ambient/Composed Effect Path) is
precisely the class such an omission would defeat, and the registry's own residual notes flag
it as the highest-stakes class for exactly this reason. A grade silent about its registry
version, or one that claims coverage of a class the cited version does not contain, is
floor-washing under "Survival Is Three-Valued."

### Conformance Application

Each class's protected condition is verified by the method its property class admits under
§22: reachability arguments for structural classes (e.g. AC-04, AC-06), reproduction and
convergence for AC-08/AC-09, injection for AC-05, adversarial attempt for AC-01/AC-02/AC-07.
The registry's stated dependencies between classes (AC-02 on AC-01; AC-07 and AC-09 on AC-08;
AC-10 on AC-03; AC-12 on AC-01 and AC-02) instantiate the partial order "The Grade Is a
Frontier Over a Partial Order" requires: a class MUST NOT be reported closed or bounded while
a class it depends on is open. Per-class residuals named in the source registry (e.g. AC-01's
untested multi-hop delegation laundering, AC-06's backlog tool/MCP moveset, AC-12's
provisional Family IX evidence) are not registry gaps to be silently absorbed into a grade;
they are the named, non-zero residuals that "Survival Is Three-Valued" requires a bounded
verdict to disclose.
