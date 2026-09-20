# §8. Identity Integrity (ZTG-0d)

## Normative

Every authorization recognized at the boundary MUST trace to an identity that is
cryptographically bound, attributable to a real principal, and valid as of
decision-time. Authority that cannot be attributed to a principal is not
authority, and the boundary MUST NOT act on it.

### Authorizing Identity

An authorizing identity is the identity under whose authority a governance
decision is made. The reasoning system MUST NOT hold an authorizing identity. A
model cannot be a principal whose authority the boundary recognizes, for the same
structural reason the boundary refuses memory-resident content as policy (ZTG-1)
and refuses model-supplied time (ZTG-0c): an input the governed subject can issue
to itself cannot be a check on the governed subject. A system that can mint its
own authorizing identity can author its own authorization, which collapses the
separation the boundary exists to maintain.

### Delegation and Terminal Attribution

Authority in a governed system is delegated, not spontaneous. Every authorization
MUST trace, through a delegation chain, to a human or institutional principal who
ratified the authority under which the decision is made. Service identities,
automated components, and the enforcement architecture itself may appear as
intermediate links in that chain, but they MUST NOT be its terminus. The chain
terminates at an accountable party, never at the system.

This is the identity-layer statement of a principle the framework asserts
elsewhere: the system never originates authority (ZTG-5), and the ratifying
officer's authority is exercised continuously through the architecture (§1, Foundational Commitments).
ZTG-0d makes that principle checkable by requiring the chain back to the ratifying
principal to be present and attributable for any authorization, so that "the
system did it on its own authority" is not a representable state. An action taken
under authority that was never delegated is unauthorized regardless of its
content — authority the principal did not grant is not authority the system holds.

### Credential Binding

Authorizing identity MUST be bound by cryptographic credentials that are
non-repudiable and revocable. Non-repudiable means attributable to the principal,
unforgeable by anyone else, and undeniable by the principal after the fact:
authorization carries a signature only the principal could produce and the
principal cannot later disavow. Revocable means the binding can be withdrawn, and
the withdrawal takes effect on governance decisions made after it.

Bearer tokens, session credentials, and shared secrets do not satisfy ZTG-0d as
the binding for authorizing identity. They authenticate a holder without
attributing to a principal: they are replayable by whoever obtains them and
disavowable by the principal who issued them, so they cannot carry attribution
strong enough to bind a governance authority. They may serve transport
authentication; they may not serve as the authorizing binding. The binding ZTG-0d
requires is the same structure the framework's override visibility depends on —
signed, attributable, and traceable — which is why the credential strength is
specified rather than left to deployment.

### Validity and Revocation in Time

An authorizing identity's validity is time-bounded and MUST be evaluated against
trusted decision-time. Whether a credential is currently valid, expired, or
revoked is determined from the ZTG-0c point-in-time snapshot, using the trusted
time source, not from a live view the reasoning system could influence. Revocation
is a governance event: it is recorded under ZTG-0a, and an authorization made
after a revocation takes effect MUST NOT recognize the revoked identity. Because
identity state is part of the decision-time snapshot, a replayed decision (ZTG-0b)
reconstructs the validity and revocation state exactly as it stood when the
decision was made — a credential valid at decision-time replays as valid even if
later revoked, and a credential revoked before decision-time replays as revoked.

### Attribution Completeness

Every governance decision's record MUST identify the authorizing identity and
preserve enough of the delegation chain to attribute the decision to its terminal
principal. An authorization whose principal cannot be reconstructed from the
record is an attribution gap, and an attribution gap is a violation under ZTG-0a's
negative-space rule, not a missing optional field. A governed system that cannot
say under whose authority an action was taken has not governed the action.

### Conformance Criteria

A conforming implementation can: demonstrate that no authorizing identity is held
by the reasoning system; trace every recognized authorization through its
delegation chain to a human or institutional principal; demonstrate that
authorizing credentials are non-repudiable and revocable, and that bearer or
shared secrets are not accepted as the authorizing binding; evaluate identity
validity and revocation against trusted decision-time from the ZTG-0c snapshot;
honor revocation on decisions made after it takes effect; and reconstruct the
terminal principal of any decision from its record.
