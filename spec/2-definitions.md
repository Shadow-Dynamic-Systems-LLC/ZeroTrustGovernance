# §2. Definitions

## 2.1 Layers

**Envelope** — the non-deterministic, statistical layer: model reasoning,
generation, and any probabilistic-improvement mechanism (alignment training,
moderation, instruction-tuning). The Envelope produces *proposals*, never effects.

**Invariant** — the deterministic, structural layer that delivers hard guarantees:
authorization gates, evidence chains, harm-class registration, ceiling enforcement,
Stasis. **The Invariant layer MUST NOT depend on any property of the Envelope**
(§1, Foundational Commitments). An Invariant guarantee that reduces to a statistical property of the Envelope
is not a guarantee.

## 2.2 The Execution Pipeline

**Governed action** — a model-proposed operation submitted to the boundary for
authorization. An action lives on the reasoning side until it is granted; it may be
granted, refused, or escalated.

**Governed effect** — an authorized action dispatched through a registered surface to
produce an externally observable change in the world. Every governed effect
originates in a governed action the boundary authorized; not every governed action
becomes a governed effect. *Action* is proposed and gated; *effect* touches the world
and is routed and coupled. The distinction is normative, not stylistic.

**The boundary (execution gate)** — the deterministic component, separate from the
reasoning system, through which every governed action must pass to become a governed
effect. Full treatment: §10 (ZTG-1).

**Authorization (grant)** — the explicit structural decision that converts the
boundary's default refusal into permission for a specific action, under a specific
policy version, at a specific decision-time, traced to a specific authorizing
identity. *Refusal* and *escalation* are the other two verdicts; all three are
governance-relevant events.

**Surface / sub-surface** — a registered, enumerated channel through which a governed
effect may reach the world, carrying declared governance properties (harm-class
default, compositional multiplier, reversal_strategy). A sub-surface may *tighten* its
surface's declarations but MUST NOT relax them. Full treatment: §12 (ZTG-3).

**Effect channel** — any path by which the system can produce an externally observable
effect. ZTG-3 requires the set of effect channels to be closed: every channel is a
registered surface, and no unregistered channel is reachable.

## 2.3 Authority and Identity

**Ratifying principal** — the human or institutional party who ratified the authority
under which a decision is made, and who is accountable for it. The terminus of every
delegation chain; the system is never the terminus. (Canonical term per the
cohesiveness pass; "ratifying officer" in §1.2 is the institutional-role synonym.)

**Authorizing identity** — the identity under whose authority a governance decision is
made, cryptographically bound, non-repudiable, revocable, and valid as of
decision-time. The reasoning system holds no authorizing identity. Full treatment: §8
(ZTG-0d).

**Delegation chain** — the recorded path from an operating identity back to its
terminal ratifying principal. Service and automated identities may be intermediate
links, never terminal.

## 2.4 Record, Time, and State

**Governance-relevant event** — any state transition, decision, or check bearing on
what the governed system was permitted to do, under what conditions, with what
accountability. The class is defined by relevance, not volume. Enumerated in §5
(ZTG-0a).

**Decision-time** — the single instant at which the boundary evaluates a proposed
action against policy; the reference instant for every time-dependent input to that
decision. Established by the architecture from a trusted source, never supplied by the
reasoning system. Full treatment: §7 (ZTG-0c).

**Governance state** — the complete set of governing inputs a decision is evaluated
against: policy versions, identity/credential registry, surface registry, harm-class
and ceiling declarations, and the configuration of the governance substrate itself.
Full treatment: §9 (ZTG-0e).

**Governance bundle** — the implementation object that carries a single coherent
version of governance state; the unit of atomic transition. (Canonical term; "policy
bundle" is not used.)

**Replay** — deterministic reconstruction of a past decision's verdict from its
recorded inputs, pinned policy version, and pinned engine semantics. Replay
reconstructs verdicts and MUST NOT re-emit effects. Full treatment: §6 (ZTG-0b).

**Evidence record (ZTG-4 evidence record)** — the record into which every invariant's
and prerequisite's output converges for a single effect. The canonical name for this
object; "convergence record" is retired (cohesiveness pass). Full treatment: §13
(ZTG-4).

## 2.5 Consequence

**Harm class** — a classification of a governed action by the *restorability* of the
harm it produces: `Restorable`, `Mitigable`, or `Irreversible`. Classification is over
the harm, not the action; the availability of forward remediation does not lower it.
Full treatment: §14 (ZTG-5).

**Liability ceiling** — the policy-assigned bound on the exposure an action is
permitted to carry. The system never originates ceiling authority.

**Compositional multiplier / composite assessment** — the per-surface multiplier, and
the recursive product of component assessments and multipliers across an action
sequence; expressed in discrete, deterministic bands so it replays identically.

**reversal_strategy** — a surface's declared, descriptive account of what the system
can undo or compensate. Orthogonal to harm class; recorded in provenance; MUST NOT
relax the gate or the harm class.

## 2.6 States and Fault Families

**Stasis** — the held state in which the system grants no new authority within a
scope, entered on loss of a positive guarantee. Scopes include at least a permit, a
component, a surface, and the control plane; control-plane Stasis, the severe form,
holds authority at zero for the whole system and is exited only by ratified authority.
A narrower scope is exited only on a legitimate resolution of its trigger. Full
treatment: §11 (ZTG-2).

**Legitimate resolution** — a resolution of a Stasis trigger that itself carries
evidence and authority: an indeterminate effect's disposition established and recorded
or its acceptance ratified, a lost guarantee verifiably restored, or a recorded act of
an authorized principal. Apparent clearance is not a legitimate resolution. Full
treatment: §11 (ZTG-2).

**Indeterminate effect** — an effect whose evidence coupling cannot be confirmed (the
write-ahead failure window, or a detected effect lacking committed evidence). A loss
of the ZTG-4 guarantee; a Stasis trigger. Full treatment: §13 (ZTG-4).

**Tamper family** — the class of integrity violations (detected tampering, ZTG-3
closure breach, ZTG-4 unreconciled indeterminate effect) that escalate to Stasis.
Consolidated trigger list in §11 (ZTG-2).
