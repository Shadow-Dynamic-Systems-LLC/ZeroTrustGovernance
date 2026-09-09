# §3. The Authorization Model

## Normative

An authorization is the explicit, recorded determination that a specific proposed
action is admissible: permitted, under valid human-governed conditions, at a definite
instant, by an attributable authority, within bounded consequence. The architecture's
default disposition toward any proposed action is refusal; an authorization is the
positive grant that converts that default into permission for one action. Authority is
never assumed, inherited, or inferred from the absence of denial.

### The Authorization Request

The unit of decision is the authorization request: the object the boundary evaluates.
A request comprises the proposed action and its validated parameters (ZTG-1 / §18), the
authorizing identity asserted for it (ZTG-0d), the registered surface it would route
through (ZTG-3), and the decision-time temporal context against which it is evaluated
(ZTG-0c). A request is evaluated as a whole and against a single coherent snapshot of
governance state (ZTG-0e); an architecture that decides parts of one request against
different states or different instants has not produced one authorization.

The reasoning system originates the *proposal* — the candidate action and its
parameters — and nothing else in the request. It does not supply the authorizing
identity, the harm classification, the time, or the policy. The governed subject
proposes; it does not author the inputs against which its proposal is judged.

### The Verdict Space

Every evaluation of a request produces exactly one of three verdicts:

- `authorize` — the request is admissible; the action is granted permission to become
  a governed effect through its routed surface.
- `refuse` — the request is not admissible; no effect follows. Refusal is the default
  and the most common verdict, and it is recorded with the same fidelity as a grant
  (ZTG-0a).
- `escalate` — admissibility cannot be determined by the architecture alone, or policy
  designates the decision for human judgment; the request is routed to the authority
  policy specifies, and the escalation, its trigger, and its routing are recorded.

`escalate` is a first-class verdict, not a deferred `refuse`. It is how the model
routes the decisions a policy reserves for human authority — high-consequence actions,
edge cases, situations requiring institutional judgment — without either granting them
mechanically or refusing them as if they were inadmissible.

### Admissibility

A request is admissible only if every one of the following holds at decision-time.
Each condition is owned by the section named; §3 is where they compose into a single
determination. Admissibility is a conjunction: the failure of any one condition makes
the request inadmissible, and the absence of a positive determination on any condition
is a failure, not a pass.

1. **Attributable authority.** A valid authorizing identity, traced through its
   delegation chain to a ratifying principal, bound by non-repudiable, revocable
   credentials, and valid as of decision-time (ZTG-0d).
2. **Coherent temporal context.** A single decision-time from a trusted source and a
   coherent point-in-time snapshot of governance state; no stale, future, or
   temporally inconsistent inputs (ZTG-0c).
3. **Consistent governance.** A single governance view, agreed across enforcement
   points and applied atomically (ZTG-0e).
4. **Policy permission.** The proposed action is permitted by the policy in effect in
   the governance bundle for that snapshot.
5. **Closed-surface routing.** The action routes to a registered surface or
   sub-surface (ZTG-3), selected by governed routing over validated features, carrying
   that channel's declared harm class.
6. **Bounded consequence.** The action is within its policy-assigned liability ceiling
   and is routed to the harm-class-appropriate gate (ZTG-5).
7. **Recordable and coupled.** The decision is recorded with integrity (ZTG-0a) and is
   replayable (ZTG-0b); where it authorizes an effect, that effect will be coupled to
   its evidence (ZTG-4).

When all conditions hold, the verdict is `authorize`. When a condition fails, the
verdict is `refuse`. When a condition cannot be determined, or policy reserves the
decision, the verdict is `escalate`. There is no admissible action outside this
conjunction, and there is no path to a grant that does not establish every condition
in it.

### Authorization Provenance

Every authorization MUST trace to human-attested authority. The authority under which a
grant is made is either direct human attestation — a ratifying principal authorizing
the action — or derivation from human-attested policy — a policy, itself ratified by a
principal under ZTG-0e, that permits the action. No authorization derives from any
other source. The model admits no self-bootstrapped authority: the system does not
originate the authority under which it acts, and there is no representable grant whose
authority terminates at the system rather than at a human or institutional principal.

This is the property on which the framework's liability argument rests. Because every
authorized effect traces to either a principal's direct attestation or a principal's
ratified policy, every authorized effect has an accountable human author — the party
whose attested acceptance of responsibility the authorization carries (§1.0). An
architecture in which some authorizations could not be traced to attested human
authority would be one in which some consequential actions had no responsible author,
which is the condition the model exists to make unrepresentable.

### The Convergence Test

An admissibility determination is admissible evidence only if it is checkable. The
convergence test is the discipline that holds it to that standard: an independent
re-evaluation of a request, over the recorded substrate, MUST converge on the same
determination, and a determination that cannot be independently reproduced is not yet
admissible. This is why the model's inputs are recorded (ZTG-0a), its evaluation is
deterministic and replayable (ZTG-0b), and its consequence assessment is banded
(ZTG-5): each is what lets a second party regenerate the determination rather than take
it on trust. The full method of the convergence test — the independent-assessment
procedure and the criteria for convergence — is larger than this section and is
specified in §22.

### Composition

The authorization model is not a separate mechanism from the boundary; it is the
decision the boundary runs. ZTG-1 guarantees that every proposed action reaches the
model and that no action becomes an effect except through its verdict; §3 specifies
what that verdict is and how it is reached. ZTG-3 guarantees the verdict has a closed
set of channels to authorize into; ZTG-5 grades the verdict by consequence; the
prerequisites guarantee the substrate the verdict is computed over and recorded into.
The binding force §1.0 asks for — authority exercised at the point of execution rather
than advisorily — is realized here: the model is the point at which an accountable
human's authority is exercised against a specific action, mediated by ZTG-1 and
attributed by ZTG-0d.

### Conformance Criteria

A conforming implementation can: represent every authorization decision as a request
evaluated as a whole against one coherent snapshot; produce exactly one of the three
verdicts for every request and record refusals and escalations with grant-level
fidelity; demonstrate that a grant is issued only when every admissibility condition is
established, and that absence of a condition produces refusal or escalation rather than
a grant; trace every authorization to direct human attestation or to human-attested
policy, and demonstrate that no grant terminates its authority at the system;
demonstrate that escalation routes to the authority policy specifies; and demonstrate
that its authorization determinations are independently reproducible from the recorded
substrate (convergence test, §22).
