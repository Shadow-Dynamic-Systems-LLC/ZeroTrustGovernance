# ZTG-AMEND-NNN: Scoped Stasis (ZTG-2)

| Field | Value |
|---|---|
| Identifier | `ZTG-AMEND-NNN` (number to be assigned by the steward; never reused) |
| Title | Scoped Stasis, legitimate resolution, and escalation by threat to the enclosing scope |
| Disposition | `proposed` |
| Disposition history | 2026-10-08 `proposed` |
| Adoption authority | Founder, as Managing Partner of Shadow Dynamic Systems LLC, under current stewardship (`GOVERNANCE.md`) |
| Effective version | v0.8, if adopted before that release; otherwise the first version after adoption |
| Affected provisions | §11 (ZTG-2) in full; §2.6 (Stasis; new term Legitimate resolution); §5 (ZTG-0a recorded events); §13 (ZTG-4, Indeterminate Effects); §22 (fault-injection properties) |
| Non-normative companion | `guide/11-stasis-ztg-2.md` (Relationship to harm class; Scoped holds; Constable note) |

## Rationale

v0.4 retired the former ZTG-5, Graduated Freeze, and folded its semantics into ZTG-2
(`VERSIONING.md`). The published §11 never absorbed that change. It describes only the
severe form, with the whole authority-granting function held at zero, so a single
indeterminate effect on a Restorable-class surface takes the entire system out of
service. That cost creates pressure to bypass Stasis, which ZTG-2 itself identifies as
the failure to resist.

The amendment restores graduated Stasis without weakening the severe form:

1. **Scopes.** Stasis is held over a scope: at least permit, component, surface, and
   control plane, in an open set. Control-plane Stasis is unchanged and mandatory.
   Narrower scopes are optional, because holding wider than required is always
   permitted.
2. **Scope selection.** The scope must be no narrower than the lost guarantee.
   System-wide guarantee losses, detected tampering, and closure breaches hold the
   control plane. An indeterminate effect's minimum scope follows its ZTG-5 harm class.
   This states the "composition concern between ZTG-2 and ZTG-5" that the guide left
   open.
3. **Escalation.** A hold widens when its condition threatens an invariant of the
   enclosing scope, or degrades it. Time alone neither escalates nor releases a hold.
4. **Exit.** A narrower scope lifts only on a legitimate resolution, never on apparent
   clearance. Control-plane exit stays ratified under ZTG-0d, with no auto-exit.
5. **Exit Path Integrity.** §22 already cites this provision, but §11 did not contain
   it. It is restored: tamper-family exits need independent re-verification, separate
   from ratification.

**Judgment for review.** §13 places every unreconciled indeterminate effect in the
tamper family, and the tamper family otherwise holds the control plane. This amendment
lets an indeterminate effect whose doubt is confined to one effect be held at the scope
its harm class requires. Any sign that the doubt is not confined is detected tampering
or a recording-integrity loss, and holds the control plane. If this exception is not
accepted, scoped Stasis still applies to the other triggers, but every indeterminate
effect holds the control plane.

**Unchanged.** The handling of in-flight actions at entry remains flagged for
refinement. The triggers are unchanged except that each records its scope. Momentary
refusals versus sustained-loss escalation is unchanged.

## Exact proposed normative text

### §11 (replaces the section in full)

# §11. Stasis (ZTG-2)

## Normative

When the system cannot guarantee that its invariants hold, it MUST enter Stasis: a
held state in which no new authority is granted within the affected scope. Stasis is
the authority-granting function held at zero over that scope. It is neither a crash
nor a shutdown; it is a defined, governed, observable state the system holds in until
the condition that caused it is legitimately resolved and, where this section requires
it, an authorized principal ratifies its exit.

### Stasis Is the Withholding of New Authority

The defining property of Stasis is that, while held, the system grants no new
authority within the held scope. This is the precise statement of the hold: Stasis
does not enumerate which effects are forbidden; it suspends the function that would
authorize any effect inside the scope at all. Composed with ZTG-1 — under which no
action derived from model output may execute without explicit structural
authorization — withholding all new grants within a scope forecloses every new governed
effect inside it without any effect needing to be named. There is no special-cased
open path inside a held scope, because there is no grant inside a held scope.

This framing also fixes what Stasis does *not* hold. Recording an event is not a
grant of authority, so observability (ZTG-0a) continues — indeed it must, including
the recording and surfacing of the held state itself. Reasoning is not a grant of
authority, so the Envelope may continue to generate; nothing it generates reaches
the world through a held scope, because the boundary grants nothing there. Stasis is
the maximal, absolute, and un-overridable form of the boundary's default disposition
toward action, which is refusal.

### Scope of the Hold

Stasis is held over a scope: the extent within which no new authority is granted. The
scopes of Stasis are at least the following, in increasing breadth:

- **Permit** — a single grant and anything that would extend or derive from it.
- **Component** — an enforcement point, an effector, or another architectural
  component through which authority is exercised.
- **Surface** — a ZTG-3 surface or sub-surface.
- **Control plane** — the whole authority-granting function of the system.

Control-plane Stasis is the severe form: authority held at zero for the whole system.
Every conforming implementation MUST implement it. An implementation MAY implement the
narrower scopes; one that does not holds at the narrowest scope it implements that
encloses the required one, which is always conforming because holding wider than
required is permitted. The set of scopes is open; an implementation MAY define
additional scopes, and each MUST declare the scope that encloses it. Holding a scope
holds everything inside it. Authority outside every held scope continues to be granted
under the ordinary rules of this specification.

While any scope is held the system MUST grant no new authority within it, MUST continue
to record under ZTG-0a, and MUST remain able to surface every held scope and its
trigger to operators. It remains inspectable and recoverable; Stasis is a state the
system holds *in*, not a state it is destroyed *by*. The distinction from a crash is
essential: a crashed system has lost observability and control; a system in Stasis
retains both and has merely stopped granting authority where its guarantees are in
doubt.

The handling of already-granted, in-flight actions at the moment of entry is a
distinct question from the withholding of new authority and is not fully resolved
in this draft. "No new authority" governs grants; whether and how Stasis quiesces
effects already authorized and in execution — particularly irreversible ones,
where interruption may itself be consequential — is flagged for refinement rather
than settled here.

### Triggers

The system MUST enter Stasis when it cannot guarantee its invariants hold. Trigger
conditions include, at minimum: sustained loss of temporal integrity (ZTG-0c);
persistent inability to establish a consistent governance view (ZTG-0e); inability
to record governance-relevant events with integrity (ZTG-0a); inability to
attribute authority to a ratifying principal (ZTG-0d); inability to evaluate the
boundary deterministically (ZTG-1); detection of a reachable effect channel that is
not registered, breaching effect-surface closure (ZTG-3); an effect whose evidence
coupling cannot be confirmed — an unreconciled indeterminate effect (ZTG-4); and
detection of evidence or integrity tampering. An authorized principal MAY also
invoke Stasis directly, at any scope.

Entry is governed by the escalation model. A single instance of a refuse-not-
proceed condition is handled by the boundary refusing that decision; this is the
boundary functioning, not a system failure. Stasis is the escalation that follows
when such conditions are sustained or structural rather than momentary — when the
system is not failing to authorize one action but failing to establish the
preconditions for authorizing within some scope. The threshold that distinguishes a
momentary refusal from a sustained loss is policy- and deployment-set; that an
escalation must occur once loss is sustained is the invariant. Entry MUST be
recorded (`STASIS_ENTERED`) with the scope and the triggering condition.

### Scope Selection

The system MUST enter Stasis at a scope no narrower than the guarantee that has been
lost. A condition confined to one grant, one component, or one surface MAY be held at
that scope. A condition that compromises a guarantee the whole system depends on —
loss of temporal integrity, of a consistent governance view, of recording integrity,
of authority attribution, or of deterministic boundary evaluation, detected evidence or
integrity tampering, and a ZTG-3 closure breach — MUST be held at the control plane.

An unreconciled indeterminate effect (ZTG-4) is in the tamper family, but its doubt is
confined to the coupling of one effect to its evidence, so its minimum scope follows
its harm class rather than defaulting to the control plane. Any sign that the doubt is
not confined — more than one indeterminate effect without an innocent common cause,
evidence that does not reconcile with the effector's record, or an indeterminate effect
that cannot be attributed to the write-ahead failure window — is detected tampering or
a recording-integrity loss and is held at the control plane.

The cost of being wrong about scope is asymmetric and tracks ZTG-5 harm class:
wrongly holding a Restorable-class scope is recoverable, while wrongly granting beside
an Irreversible-class indeterminate effect may not be. The minimum scope for an
indeterminate effect (ZTG-4) MUST therefore widen with the harm class of the surface
it was routed through: no narrower than the permit for a Restorable-class surface whose
liability ceiling is enforced, no narrower than the surface for a Mitigable-class
surface or a ceiling that is not enforced, and the control plane for an
Irreversible-class surface. Policy MAY widen any scope. Policy MUST NOT narrow a
scope below the minimum this section requires.

### Escalation

A held condition MUST escalate to the enclosing scope when it threatens an invariant of
that scope, or degrades it. Escalation tracks the reach of the threat, not elapsed
time: a condition that spreads to further grants on the same component threatens the
component; indeterminate effects whose composite assessment (ZTG-5) crosses a
surface's threshold threaten the surface; a condition that touches any guarantee the
whole system depends on threatens the control plane. A sustained condition is evidence
of degradation and MAY be the reason a threat is established, but the passage of time
alone neither escalates a scope nor releases one. Escalation MUST be recorded as
`STASIS_ENTERED` for the wider scope, with the narrower hold as its trigger.

### Exit

A scope narrower than the control plane MAY exit when every trigger inside it has been
legitimately resolved and no enclosing scope is held. A **legitimate resolution** is
one that itself carries evidence and authority: the true disposition of an
indeterminate effect established and recorded, or its acceptance explicitly ratified
by an authorized principal (ZTG-4); a lost guarantee verifiably restored; or a
condition otherwise handled by a recorded act of an authorized principal. A trigger
that merely appears to clear — time passing, a component becoming reachable again
without accounting for what happened, an error that stopped recurring — is not a
legitimate resolution and MUST NOT lift any scope. Exit from a narrower scope MUST be
recorded (`STASIS_EXIT`) with references to the resolving records. Policy MAY require
ratification for exit from any scope.

Exit from control-plane Stasis MUST be ratified by a human or institutional principal
under ZTG-0d. The system MUST NOT exit control-plane Stasis on its own authority, and
MUST NOT exit automatically when the triggering condition appears to clear. Exit
requires that the triggering condition be resolved or explicitly accepted by the
ratifying principal, and the exit MUST be recorded as an authorized governance event
(`STASIS_EXIT_REQUESTED`, then `STASIS_EXIT_RATIFIED`).

Ratified exit from the control plane is not an additional precaution layered onto
Stasis; it follows from what Stasis is. Because control-plane Stasis is the withholding
of all new authority, the system cannot grant itself the authority to exit — the
authority to release the hold is precisely the kind of new authority the hold
suspends. Exit authority must therefore originate outside the held system, with a
ratifying principal. A narrower scope is different only in where the authority to
resolve it comes from: the system outside the held scope still grants under its
guarantees, so a narrower scope may lift on a resolution that carries its own
authority, but never on the system's judgment that the condition "appears resolved".
A system permitted to self-clear once a condition appears resolved is a system in
which the component that failed its guarantees adjudicates their restoration, which is
the self-authorization the architecture exists to prevent.

### Exit Path Integrity

Where the trigger belongs to the tamper family, exit at any scope MUST additionally
require independent re-verification of the integrity that was in doubt — the evidence
chain, the effect-surface registry, or the coupling of effects to evidence — by a path
the component under suspicion cannot influence. For an indeterminate effect held below
the control plane, establishing its true disposition from the effector's own record,
validated against the authorization it was dispatched under, is that re-verification;
its ratified acceptance replaces re-verification only because it is itself a ratified
act. Detected tampering and closure breaches are held at the control plane, so their
exit is also ratified under ZTG-0d. Re-verification and ratification are separate
requirements: a principal cannot ratify away a doubt that has not been re-verified, and
a passing re-verification does not exit a ratified hold without ratification.

### Non-Bypassability

Stasis MUST NOT be bypassable by the governed system or by operational override at
runtime, at any scope. Operational pressure to bypass Stasis — to keep throughput up
during a governance rollout, to ship past a degraded time source, to avoid the cost of
a held state — is expected, and yielding to it is non-conforming. The pressure is
evidence the mechanism is doing its job: Stasis is costly exactly when proceeding
would be dangerous. A Stasis that can be turned off under load is not a fail-closed
guarantee; it is a fail-closed default with a fail-open exception, which reduces to
fail-open. Narrowing a held scope is a form of release and is subject to the same
prohibition.

### Conformance Criteria

A conforming implementation can: enter Stasis on each enumerated trigger and
demonstrate that escalation occurs once loss is sustained; implement control-plane
Stasis and declare which narrower scopes it implements, and demonstrate that no new
authority is granted inside a held scope while authority outside every held scope
continues under the ordinary rules; select a scope no narrower than the lost
guarantee, holding detected tampering, closure breaches, system-wide guarantee
losses, and Irreversible-class indeterminate effects at the control plane, and
holding other indeterminate effects no narrower than their harm class requires;
escalate a held condition to its enclosing scope when it threatens or degrades that
scope, and demonstrate that time alone neither escalates nor releases; continue
recording and surface every held scope while in Stasis; lift a narrower scope only
on a legitimate resolution and demonstrate that apparent clearance does not lift it;
require ratified exit under ZTG-0d for control-plane Stasis and demonstrate the
system cannot self-exit or auto-exit on apparent clearance; require independent re-
verification before exit from tamper-family triggers; record entry, escalation, and
exit as governance events; and demonstrate that Stasis, and the breadth of a held
scope, cannot be bypassed or narrowed by the governed system or by runtime override.

### Conforming changes to §2, §5, §13 and §22

```diff
diff --git a/spec/13-evidence-coupled-execution-ztg-4.md b/spec/13-evidence-coupled-execution-ztg-4.md
index 3aa7dcc..3e62919 100644
--- a/spec/13-evidence-coupled-execution-ztg-4.md
+++ b/spec/13-evidence-coupled-execution-ztg-4.md
@@ -52,8 +52,9 @@ An effect whose coupling cannot be confirmed — the write-ahead failure window
 dispatch status is unknown, or any detected effect lacking committed evidence — is a
 loss of the ZTG-4 guarantee and MUST be treated as an integrity violation in the
 tamper family. Consistent with fail-closed semantics, an unreconciled indeterminate
-effect is a Stasis (ZTG-2) trigger: the system holds rather than continuing to act
-while the coupling between its effects and its evidence is in doubt. The
+effect is a Stasis (ZTG-2) trigger: the system holds, at the scope ZTG-2 requires for
+the effect's harm class, rather than continuing to act while the coupling between its
+effects and its evidence is in doubt. The
 indeterminate effect MUST be reconciled — its true disposition established and
 recorded — or its acceptance explicitly ratified by an authorized principal, before
 normal operation resumes. The system does not silently absorb a coupling gap, and it
diff --git a/spec/2-definitions.md b/spec/2-definitions.md
index 4b82d5c..0209207 100644
--- a/spec/2-definitions.md
+++ b/spec/2-definitions.md
@@ -109,9 +109,18 @@ relax the gate or the harm class.
 
 ## 2.6 States and Fault Families
 
-**Stasis** — the held state in which the system grants no new authority, entered on
-loss of a positive guarantee and exited only by ratified authority. Full treatment:
-§11 (ZTG-2).
+**Stasis** — the held state in which the system grants no new authority within a
+scope, entered on loss of a positive guarantee. Scopes include at least a permit, a
+component, a surface, and the control plane; control-plane Stasis, the severe form,
+holds authority at zero for the whole system and is exited only by ratified authority.
+A narrower scope is exited only on a legitimate resolution of its trigger. Full
+treatment: §11 (ZTG-2).
+
+**Legitimate resolution** — a resolution of a Stasis trigger that itself carries
+evidence and authority: an indeterminate effect's disposition established and recorded
+or its acceptance ratified, a lost guarantee verifiably restored, or a recorded act of
+an authorized principal. Apparent clearance is not a legitimate resolution. Full
+treatment: §11 (ZTG-2).
 
 **Indeterminate effect** — an effect whose evidence coupling cannot be confirmed (the
 write-ahead failure window, or a detected effect lacking committed evidence). A loss
diff --git a/spec/22-conformance-verification.md b/spec/22-conformance-verification.md
index ad3955f..10d4537 100644
--- a/spec/22-conformance-verification.md
+++ b/spec/22-conformance-verification.md
@@ -53,9 +53,9 @@ absence of a corresponding effect for a completion record cannot arise silently
 guarantee*: Stasis fires on each trigger (ZTG-2); a partitioned gate fails closed
 (ZTG-0e); the write-ahead crash window yields a recorded indeterminate effect, never a
 silent gap (ZTG-4). These are verified by injecting the fault and confirming the
-fail-closed response — including that recovery from Stasis requires ratified authority
-and, for tamper-family triggers, independent re-verification (ZTG-2 Exit Path
-Integrity).
+fail-closed response — including that a held scope lifts only on a legitimate
+resolution, that recovery from control-plane Stasis requires ratified authority, and,
+for tamper-family triggers, independent re-verification (ZTG-2 Exit Path Integrity).
 
 **Integrity properties.** Some requirements assert *tamper-evidence*: governance records
 cannot be silently altered (ZTG-0a); the coupling path cannot be severed by the
diff --git a/spec/5-observability-ztg-0a.md b/spec/5-observability-ztg-0a.md
index 7371e97..0d13a12 100644
--- a/spec/5-observability-ztg-0a.md
+++ b/spec/5-observability-ztg-0a.md
@@ -27,7 +27,8 @@ enumerate the governance-relevant event types its architecture can produce and
 demonstrate that each produces a record. At minimum the class includes:
 authorization requests; boundary evaluations and their verdicts; policy-version
 selection; identity validation; time-source checks; surface- and sub-surface
-routing decisions; Stasis entry, exit request, and exit ratification; harm-class
+routing decisions; Stasis entry, escalation, exit, exit request, and exit
+ratification, each with its scope; harm-class
 and liability-ceiling assignment; evidence-record emission; input normalization;
 and any promotion of memory content into policy-relevant input.
 
```
