# §11. Stasis (ZTG-2)

## Normative

When the system cannot guarantee that its invariants hold, it MUST enter Stasis: a
held state in which no new authority is granted. Stasis is the authority-granting
function held at zero. It is neither a crash nor a shutdown; it is a defined,
governed, observable state the system holds in until an authorized principal
ratifies its exit.

### Stasis Is the Withholding of New Authority

The defining property of Stasis is that, while held, the system grants no new
authority. This is the precise statement of the hold: Stasis does not enumerate
which effects are forbidden; it suspends the function that would authorize any
effect at all. Composed with ZTG-1 — under which no action derived from model
output may execute without explicit structural authorization — withholding all new
grants forecloses every new governed effect without any effect needing to be
named. There is no special-cased open path during Stasis, because there is no
grant during Stasis.

This framing also fixes what Stasis does *not* hold. Recording an event is not a
grant of authority, so observability (ZTG-0a) continues — indeed it must, including
the recording and surfacing of the held state itself. Reasoning is not a grant of
authority, so the Envelope may continue to generate; nothing it generates reaches
the world, because the boundary grants nothing. Stasis is the maximal, absolute,
and un-overridable form of the boundary's default disposition toward action, which
is refusal.

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
invoke Stasis directly.

Entry is governed by the escalation model. A single instance of a refuse-not-
proceed condition is handled by the boundary refusing that decision; this is the
boundary functioning, not a system failure. Stasis is the escalation that follows
when such conditions are sustained or structural rather than momentary — when the
system is not failing to authorize one action but failing to establish the
preconditions for authorizing any action. The threshold that distinguishes a
momentary refusal from a sustained loss is policy- and deployment-set; that an
escalation must occur once loss is sustained is the invariant. Entry MUST be
recorded (`STASIS_ENTERED`) with the triggering condition.

### Scope of the Hold

While in Stasis the system MUST grant no new authority, MUST continue to record
under ZTG-0a, and MUST remain able to surface its held state to operators. It
remains inspectable and recoverable; Stasis is a state the system holds *in*, not a
state it is destroyed *by*. The distinction from a crash is essential: a crashed
system has lost observability and control; a system in Stasis retains both and has
merely stopped granting authority.

The handling of already-granted, in-flight actions at the moment of entry is a
distinct question from the withholding of new authority and is not fully resolved
in this draft. "No new authority" governs grants; whether and how Stasis quiesces
effects already authorized and in execution — particularly irreversible ones,
where interruption may itself be consequential — is flagged for refinement rather
than settled here.

### Exit

Exit from Stasis MUST be ratified by a human or institutional principal under
ZTG-0d. The system MUST NOT exit Stasis on its own authority, and MUST NOT exit
automatically when the triggering condition appears to clear. Exit requires that
the triggering condition be resolved or explicitly accepted by the ratifying
principal, and the exit MUST be recorded as an authorized governance event
(`STASIS_EXIT_REQUESTED`, then `STASIS_EXIT_RATIFIED`).

Ratified exit is not an additional precaution layered onto Stasis; it follows from
what Stasis is. Because Stasis is the withholding of all new authority, the system
cannot grant itself the authority to exit — the authority to release the hold is
precisely the kind of new authority the hold suspends. Exit authority must
therefore originate outside the held system, with a ratifying principal. The
no-new-authority invariant and the ratified-exit requirement are the same
requirement seen from two sides: a system that could authorize its own exit would
not have been withholding all authority, and a system that withholds all authority
cannot authorize its own exit. A system permitted to self-clear once a condition
"appears resolved" is a system in which the component that failed its guarantees
adjudicates their restoration, which is the self-authorization the architecture
exists to prevent.

### Non-Bypassability

Stasis MUST NOT be bypassable by the governed system or by operational override at
runtime. Operational pressure to bypass Stasis — to keep throughput up during a
governance rollout, to ship past a degraded time source, to avoid the cost of a
held state — is expected, and yielding to it is non-conforming. The pressure is
evidence the mechanism is doing its job: Stasis is costly exactly when proceeding
would be dangerous. A Stasis that can be turned off under load is not a fail-closed
guarantee; it is a fail-closed default with a fail-open exception, which reduces to
fail-open.

### Conformance Criteria

A conforming implementation can: enter Stasis on each enumerated trigger and
demonstrate that escalation occurs once loss is sustained; demonstrate that no new
authority is granted while held, and therefore that no new governed effect
initiates; continue recording and surface the held state while in Stasis; require
ratified exit under ZTG-0d and demonstrate the system cannot self-exit or
auto-exit on apparent clearance; record entry and exit as governance events; and
demonstrate that Stasis cannot be bypassed by the governed system or by runtime
override.
