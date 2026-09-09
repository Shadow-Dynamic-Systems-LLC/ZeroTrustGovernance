## What Zero Trust Governance Is Built to Prevent

The seven questions of §1.0 state what governance must *preserve*. This section
states what defeats governance that does not — the failure modes ZTG is built
against. It is the hinge between the introduction and the normative body: each
invariant the body specifies is, read from this side, the structural refusal of a
specific failure named here. A reader who finishes this section should be able to
turn to any invariant and recognize the argument it answers.

The failures share a shape, and the shape has a name. In each of them, a
consequential action becomes separated from the accountable human who was supposed
to be its source, while the *appearance* of authorization survives the separation.
The action reaches the world; the record says it was governed; and there is no
accountable principal at the other end of the chain. We call this **laundered
authority**: authorization-in-appearance detached from authorization-in-fact. The
failures below are distinct laundering channels. ZTG closes or bounds each — and is
candid, channel by channel, about where it closes a channel outright, where it only
reduces it to a small named assumption, and where it can so far only mark the channel
for a chapter that must close it.

### The component that can defect without cause

Conventional security already reasons about components that fail in complicated ways
— Byzantine faults, intermittent failures, latent defects, insider misuse, partial
compromise — and carries a mechanism for each. What it has been able to rely on is
that a component's track record is evidence about its next step: demonstrated
reliability narrows what the component will do. A reasoning system backed by a large
model withdraws that assumption. It is nondeterministic, context-sensitive, and
subject to drift, and it can exit authorized behavior with no adversary, no prompt
injection, and no detectable precipitating cause.[^lw-defect-sources] The turn need
not be induced from outside to occur.

This breaks any architecture that extends trust to the reasoning system's good
behavior — even briefly, even only "once it has authenticated," even only for
actions it has handled correctly a thousand times. Trust extended to a component
that can withdraw its own trustworthiness without notice is not a smaller risk than
trust extended to a known-hostile component; it is the same risk wearing a record
of good conduct. A track record is precisely the evidence that does not bind here,
because the property it attests to is not stable.

ZTG's refusal of this channel is the foundational separation the normative body
opens with: *the Invariant layer must not depend on the Envelope layer* (§1.3,
ZTG-1). The boundary through which synthetic reasoning becomes consequential action
does not trust the reasoning system, has never trusted it, and does not become more
trusting as the system accrues good behavior. Its default disposition toward any
model-derived action is refusal. The consequence is not that ZTG detects the
defecting agent faster than other approaches — it is that ZTG does not need to detect
it at all. Spontaneous deviation is not an incident the architecture races to catch;
it is the baseline assumption the boundary is built against. The question "has the
agent turned?" is not answered better — it is made moot, so long as the boundary
genuinely sits across every path from reasoning to effect.[^lw-complete-mediation] An
unmediated path puts the dependence back.

### The negative that cannot be established

A second failure follows from the same property. In a deterministic system one can
often prove a negative: the system did *not* take action X, did *not* touch record
Y, during window W. Remediation can then be scoped, because the boundary of what
happened is knowable. Against a probabilistic agent this frequently becomes
intractable. The agent's behavior between logged events is not fully captured; the
counterfactual — what it would have done, what it touched that left no trace — is
unanswerable. When the negative cannot be established, the extent of a compromise
cannot be bounded, and the only defensible assumption becomes total compromise.

ZTG's response is not to claim it has made every negative establishable. It is to
draw the line precisely, and to put the unestablishable negative on the side of the
line the architecture already refuses to trust. For the **governed effect surface** —
provided every effect actually routes through the boundary and leaves its expected
record — the negative is establishable:[^lw-establishable-negative] what crossed the
boundary, under what authority, at what decision-time, against what policy, is a
recorded fact on a substrate external to the agent, not an inference reconstructed
after the incident. For **Envelope-internal state** — what the model represented,
intended, or considered — the negative is *not* establishable, and ZTG does not try
to make it so. It denies that state the power to count as authority rather than
pretending it has no effects: the agent's internal state can shape what it
*proposes*, but a proposal is not an effect, and nothing the agent does internally
becomes a governance input or a consequential action until it crosses the boundary
and is recorded. The intractable negative is confined to the layer whose account the
architecture never accepts on its own word.

There is a harder case, and ZTG meets it on the failure's own terms. When the
compromise reaches the *trusted base itself* — the gate, the evidence substrate, the
identity system, rather than the Envelope — then the negative genuinely cannot be
established from inside, and total compromise *is* the correct assumption. This is
the posture ZTG-2 (Stasis) and its minimal-recovery-base requirement adopt: a system
whose trusted base may be compromised is not recovered from within by any mechanism,
because a compromised path can manufacture its own release. Recovery proceeds
out-of-band, from a base small enough to be isolated and independently attestable,
re-establishing the compromised guarantee from evidence the held system could not
have forged. Here the honest claim is the bounded one: where the failure is in the
Envelope, ZTG makes "assume total compromise" unnecessary; where the failure is in
the base, ZTG does not dissolve that assumption so much as shrink it — survivability
is made to rest on a small, named, independently attestable recovery base whose own
rooting the specification flags as open rather than hides.[^lw-recovery-base]

### The environment that carries the predisposition forward

The first two channels take the agent as the unit that might be compromised. But an
agent does not act in a vacuum: it acts on an environment — tool configurations,
accessible memory, context stores, written artifacts, the state of the downstream
services it can reach — and through ordinary operation it can leave that environment
changed. The failure this channel names is that the change can predispose the agent's
own successors. An invocation acting within its authority writes to a memory store,
adjusts a tool's configuration, or leaves behind an artifact that a later invocation
will read as ground truth; the distance between the environment the deployment
intended and the environment that now exists widens, invocation by invocation, with no
one having authorized or observed the widening. No adversary is required at any point,
no prompt injection, no detectable trigger. The failure is distinct from prompt
injection (there is no attacker), from model drift (the model has not changed), and
from misconfiguration (the configuration was correct at a prior point); it is a
category of its own, and it is worth a name — *environmental self-predisposition*: an
agent creating, through authorized-looking activity, the conditions that make future
unauthorized behavior more probable, with no external cause. Counted seventh here
because it was the last of these channels to be isolated, it belongs in the reading
order beside the first two — it is their temporal form. Where the channel above says
you cannot establish what the agent did, this one says the agent may already have
shaped what it will do next.

The laundering move is that ungoverned environment state, shaped by the agent itself,
acquires governing force over future behavior without that force ever having been
authorized. What makes the channel severe is the cost of remediation: replacing the
agent does not recover you, because you have placed a clean agent in a contaminated
environment, and the environment — everything the prior agent could write to — carries
the predisposition forward. Recovery, the Fork → Review → Repair → Restore path, must
therefore extend to the full deployment environment and not stop at the agent.

ZTG's refusal of this channel is that the agent has no ambient authority to write to
the environment that governs it. Each of those substrates is reachable only as a
governed effect: memory enters governance through an attested promotion step rather
than as raw state the agent may revise at will; a change to a tool or to the effect
surface is a governance-state mutation (ZTG-0e) on a registered surface (ZTG-3); an
artifact or a downstream write is an effect mediated by the boundary (ZTG-1) and
recorded (ZTG-0a). The load-bearing clause of the failure — that the gap grows
*without anyone authorizing or observing it* — is precisely what these refuse: in a
conforming deployment there is no unobserved write path, and the environment's drift
is itself a sequence of authorized-or-refused, recorded effects. That permits a
sharper definition of the thing recovery needs. *Uncontaminated* need not be a pristine
origin snapshot the deployment must have captured in advance; it can be defined as the
environment state derivable by replaying only the attested authorization history
(ZTG-0b). Contamination is then divergence between the live environment and the
replay-derived one — environment state unaccounted for by any authorized, recorded
governance event — and Review acquires something concrete to compare against in place
of an absent ideal.[^lw-environment-replay]

This holds only as far as the writable environment lies inside the governed effect
surface, and the essay claims no further. Any state the agent can write that is not a
registered surface is unaccounted divergence — the §10 borderline cases (memory
consulted on paths the boundary does not see, observable resource-allocation patterns)
at the scale of the whole environment, a coverage burden discharged by conformance
rather than a guarantee that comes for free. And the replay-derived baseline is
anchored on the same minimal recovery base whose rooting channel 2 already flagged as
open: if no attested origin anchors the replay, there is nothing from which to derive
the clean environment. The bootstrapping gap and environmental self-predisposition
compound — no attested origin state, plus agent-mediated drift, leaves no recoverable
baseline — which makes the minimal-recovery-base question not a footnote to this
channel but the hardest thing the architecture has so far only bounded. It is named
here as exactly that, and not as closed.

### The subject that narrates its own governance

The third channel is the one that most directly produces laundered authority, and
it is subtle because it can coexist with a complete, well-formatted audit trail. If
the record of what the system did is produced by the system itself, then the record
is evidence of what the agent *logged*, not evidence of what the agent was
*authorized* to do. An agent that can defect without cause (the first failure) and
whose internal history cannot be independently bounded (the second) is exactly the
party whose self-narration cannot be trusted to attest to its own governance. A
governance architecture that lets the governed subject author the record of its own
governance has not built an audit trail; it has built a laundering machine, in which
unauthorized action acquires the documentary appearance of authorized action by the
subject's own hand.

ZTG closes this channel by a requirement stated plainly and for exactly this
reason: *the record must be kept outside the governed subject's control.* The
evidence substrate (ZTG-0a) is produced by the boundary, not by the agent; it is
append-only and tamper-evident; and emission runs on a path the reasoning system
cannot affect (ZTG-1), so the agent has no write path into the record of its own
governance.[^lw-external-substrate] The property generalizes one level down, to the
inputs that determine how an action is judged: the features that drive an action's
classification and routing are validated inputs, never values the model asserts
about itself (§18, ZTG-3, ZTG-5). The agent can influence what is *proposed*; it
cannot influence how a proposal is recorded, classified, or attributed. The governed
subject does not author the inputs that govern it, and does not author the record
that attests to it. An agent cannot launder authority through a trail it did not
write and cannot alter, using a classification it was not permitted to assign.

### The reviewer who has stopped reviewing

The fourth channel does not run through the machine at all. It runs through human
psychology, and it is the one structure can narrow but not close. A ratification
step that exists on paper can be hollowed out by habituation, by ratification
fatigue, by the diffusion of authority across enough reviewers that no individual
feels accountable for any single grant. A reviewer conditioned to approve is a
laundering channel that no configuration change addresses: the token is scoped
correctly, the policy is sound, and the human at the controls has stopped
governing. This failure is psycho-social, and it coexists with a perfectly correct
technical configuration rather than being cured by one.

ZTG does not claim to make a human attentive. What it does is deny the specific
laundering move this failure most often takes — the move in which authority becomes
*nobody's in particular*. Every grant traces, through a delegation chain (ZTG-0d),
to a named principal who accepted responsibility for it, and every such acceptance
is recorded as a governance event the principal cannot later disown and the system
cannot manufacture on their behalf. The diffusion of authority into no one — "the
committee approved it," "the process authorized it," "no one in particular decided" —
is denied its anonymous form: the chain terminates in a particular accountable
name.[^lw-terminal-attribution] What the architecture cannot guarantee is that the
name at the terminus answers to meaningful, attentive responsibility rather than a
role occupied and a key held. It renders the act of authority visible, attributable,
and non-bypassable; it cannot render the human exercising it awake. That residual is
real, and it is named here rather than absorbed into a claim the architecture cannot
support: ZTG makes ratification *accountable*; it does not make it *attentive*.
Closing the remaining gap — establishing when ratification is engaged enough to count
as authorization in fact, and what controls (separation of duties, sampling, forced
justification, independent review) deployments owe against reviewer fatigue — is the
work of a dedicated human-ratification assurance chapter, the candidate chapter
immediately following this one. This essay defines no attentiveness threshold and
should not be read as supplying one.

### Two channels this essay names but does not close

The five channels above are not offered as the complete set, and a threat model that
claimed completeness would commit exactly the kind of overreach this specification is
built to avoid. Two further channels are visible now; they are named here, with their
treatment deferred to where it belongs.

**Policy laundering.** Authority can be counterfeited without touching the model, the
log, or the human — by acting under policy that is stale, manipulated, internally
inconsistent, or ambiguously versioned, so that an action is "authorized" against
governing conditions no accountable principal would currently endorse. The mechanisms
that answer this are specified elsewhere (governance-state consistency and continuity,
ZTG-0e; coherent point-in-time policy snapshots, ZTG-0c; the authorization model, §3),
but this essay does not yet develop policy laundering as a channel in its own right.

**Composition laundering.** Authority can be laundered across a seam: a governed
system hands an action to a downstream system, vendor, plugin, or tool whose evidence
and authority semantics are weaker, and then treats the downstream effect as though it
inherited the upstream system's governance. §4 establishes that invariants must hold
end-to-end across such seams and that exposure composes rather than resetting, but the
full treatment of governed-to-governed composition is open work (flagged in the
index). The bridge marks composition laundering as the channel that open work must
close.

### The channels at a glance

| Channel | The laundering move | Refused by | Status of the refusal |
|---|---|---|---|
| 1 · Spontaneous defection | The reasoning system's good behavior is promoted into authorization authority | ZTG-1 boundary, independent of the Envelope (§1.3) | Closed under complete mediation + effect-surface closure |
| 2 · Unestablishable negative | An incomplete record of a probabilistic agent is treated as proof of authorized operation | ZTG-0a/0b/3 for the effect surface; ZTG-2 recovery base for the trusted base | Effect-surface negative is conditional; trusted-base survival is a bounded assumption |
| 3 · Self-authored record | The governed subject authors the record and classification of its own governance | ZTG-0a + ZTG-1 (emission off the agent's path); §18 (validated, not asserted, features) | Closed where the substrate is genuinely external |
| 4 · Hollow ratification | Human authority becomes nobody's in particular, or a name without judgment | ZTG-0d terminal attribution | Bounded: attribution, not attentiveness — deferred to a ratification-assurance chapter |
| 5 · Policy laundering | An action is authorized against stale, manipulated, or ambiguous policy | ZTG-0e, ZTG-0c, §3 (mechanism present) | Named, not yet developed as a channel |
| 6 · Composition laundering | A downstream effect inherits upstream governance it did not earn | §4 (principle; end-to-end invariants) | Deferred to open multi-system composition work |
| 7 · Environmental self-predisposition | Ungoverned environment state the agent shaped acquires governing force over its successors | ZTG-1/ZTG-3 (no ambient write; environment mutates only as a governed effect) + ZTG-0b (contamination as replay-divergence) | Conditional on effect-surface coverage of all writable state; compounds with the ZTG-2/ZTG-0e recovery-base bootstrap — the essay's hardest residual |

The status column is the point of the table: it is the claim boundary stated in the
open. Where a channel is closed, it is closed under stated conditions; where it is
only bounded or deferred, the table says so rather than letting the surrounding prose
imply more.

### What this architecture is, stated as a refusal

Read forward, ZTG is a set of guarantees. Read against the failures above, it is a
set of refusals, and the refusals are more revealing than the guarantees. ZTG
refuses to let a consequential effect reach the world except through a grant; it
refuses to let that grant rest on the reasoning system's good behavior; it refuses
to let the governed subject author either the inputs that judge it or the record
that attests to it; it refuses to let the agent quietly reshape the environment that
will govern its successors; and it refuses to let authority dissolve into no one's
particular responsibility. Each refusal closes, bounds, or attributes a channel
through which authority is laundered — through which an action that no accountable
human authorized comes to wear the appearance of authorization. Some it closes
outright, some it reduces to a small and named assumption, and at least two it can so
far only mark for the chapters that must close them; the table above is the honest
ledger of which is which.

The honesty of the architecture is in what it declines to refuse. It does not make a
model trustworthy; it makes the model's trustworthiness irrelevant to what can
reach the world. It does not make every internal history establishable; it makes the
unestablishable history irrelevant to governance. It does not make a human
attentive; it makes the human's authority the only path to consequence and makes its
exercise accountable. The architecture is built to prevent laundered authority. It
is not built to prevent a model from being a model, or a human from being a human —
and a specification that claimed otherwise would be laundering a guarantee it could
not keep.

### Notes

[^lw-defect-sources]: The informal terms name sources, not the property the boundary
    depends on. Formally, the boundary may not take as a premise any Envelope
    guarantee that is merely statistical: nondeterminism, context-sensitivity, and
    distributional drift each make the reasoning system's conformance a probability
    rather than an invariant, and a cannot-do guarantee cannot rest on a probabilistic
    premise (§1.3, Invariant-must-not-depend-on-Envelope). "Spontaneous defection" is
    the operational name; "no statistical Envelope property is admissible as an
    Invariant premise" is the formal one.

[^lw-complete-mediation]: "Sits across every path from reasoning to effect" is
    complete mediation in the reference-monitor sense: every attempt by the governed
    subject to produce a consequential effect is interposed on and checked, with no
    bypass path. ZTG-1 (the Mechanistic Boundary) and ZTG-3 (a closed, registered
    effect surface) are jointly the conformance conditions; §10's borderline cases —
    mid-inference tool calls, memory writes consulted elsewhere, observable
    resource-allocation patterns — are exactly the places complete mediation can leak,
    and each unmediated path reintroduces the Envelope dependence the boundary exists
    to remove.

[^lw-establishable-negative]: Establishable under stated conformance conditions, not
    in general. Formally: given complete mediation (ZTG-1), a closed registered effect
    surface (ZTG-3), and expected-record coverage with enforced negative space
    (ZTG-0a) replayable against pinned governance state (ZTG-0b), the predicate "no
    governed effect crossed the boundary in window W without a corresponding
    authorization record or a logged violation" is decidable over the record. The
    claim ranges over the governed effect surface only; it makes no assertion about the
    totality of the agent's behavior, and it fails gracefully — absent any of the named
    conditions, the negative weakens to the same intractability it has for
    Envelope-internal state.

[^lw-recovery-base]: A hostile reader is right that this isolates the trust assumption
    rather than discharging it. ZTG-2's Exit Path Integrity requires that a minimal
    base survive any trigger and that recovery proceed out-of-band from it; how that
    base is rooted is jointly open with the ZTG-0e substrate self-governance bootstrap.
    The formal claim is therefore a reduction, not a solution: ZTG converts "assume
    everything is compromised" into "assume a small, named, independently attestable
    base survived" — a strictly smaller and inspectable assumption, whose discharge is
    named open work, not an absence of assumption.

[^lw-environment-replay]: Let E be the deployment-environment state (tool and
    effect-surface configuration, promoted memory, context stores, artifacts, reachable
    downstream state). The formal content of "uncontaminated" is not a captured origin
    snapshot but the state E\* obtained by deterministic replay (ZTG-0b) of the attested
    authorization history from an attested initial base; contamination is any divergence
    E ≠ E\* — environment state not derivable from a recorded, authorized governance
    event. Under complete mediation (ZTG-1) and a closed registered effect surface
    (ZTG-3) covering every writable substrate the agent can reach, E = E\* holds by
    construction, so contamination is exactly the residue of writes that escaped the
    surface. The guarantee is therefore doubly conditional: on *coverage* — any writable
    substrate outside the registered effect surface (the §10 borderline cases at
    environment scope) is unaccounted divergence — and on *base* — replay is anchored on
    the minimal recovery base whose rooting is jointly open with ZTG-0e (the same
    assumption named in [^lw-recovery-base]). Where both hold, environmental
    self-predisposition reduces to ungoverned write, which the effect surface already
    refuses; where either fails, it is the open residual.

[^lw-external-substrate]: "Outside the governed subject's control" has a precise form:
    the logging and emission channel must not lie within the agent's effect surface.
    Were the record writable by the governed subject, the record would itself be a
    governed effect the subject could produce — which ZTG-1 (mediation) and ZTG-3
    (closed effect surface) preclude by construction. Tamper-evidence (ZTG-0a) covers
    alteration after emission; emission-off-the-agent's-path (ZTG-1) covers authorship
    at emission. Both are required: either alone leaves a channel.

[^lw-terminal-attribution]: ZTG-0d guarantees terminal attribution, not its
    meaningfulness. Delegation chains terminate at an accountable human or
    institutional principal; committees, delegated roles, service identities, and key
    custody are explicitly deployment bindings under ZTG-0d. Identity integrity
    certifies the cryptographic terminus of the chain — that a particular accountable
    credential authorized the grant — not the cognitive engagement of the principal
    holding it. "Denied its anonymous form" is therefore exact: the architecture
    forecloses anonymity of authority, not the organizational hollowing of it.
