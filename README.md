# Zero Trust Governance

**Preserving human agency—continuously and structurally.**

Zero Trust Governance (ZTG) is an open specification for preserving human authority
as AI systems become capable of consequential action.

An AI system can propose an action. It must not become the source of the authority to
execute it. Human agency is not preserved merely because someone approved a
deployment, can inspect a log, or may intervene after the fact. It is preserved when
every consequential action remains bound, at the moment of execution, to authority
supplied by an identifiable human or institution.

ZTG specifies the architecture for maintaining that boundary. Every governed effect
must pass through deterministic enforcement, trace to attributable authority, and
produce evidence structurally bound to execution. When the system cannot establish
that these conditions hold, it must not grant new authority.

ZTG does not try to make probabilistic reasoning trustworthy, aligned, or incapable
of error. It treats model output as a proposal—not permission. The reasoning may be
synthetic. The authority remains human.

## Publication status

This repository publishes the current ZTG working draft. It is not the adopted ZTG
v0.8 release. v0.7 remains the last published version designation; v0.8 is the
conformance-complete adoption target.

The draft is incomplete in places. Publication makes the work reviewable and
implementable; it does not convert unresolved material into an adopted requirement or
create a certification program.

## Repository map

- [`spec/`](spec/) contains normative requirements.
- [`guide/`](guide/) contains the Deployment Guide: explanatory material separated
  from the source chapters, including the introduction, operational framing, and
  further considerations.
- [`GOVERNANCE.md`](GOVERNANCE.md) records the adopted stewardship and amendment
  process.
- [`DECISIONS.md`](DECISIONS.md) records current public decision status where the
  working draft has not yet caught up.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how proposals are received and adopted.
- [`LICENSES.md`](LICENSES.md) defines the repository's effective license boundaries.
- [`PROVENANCE.md`](PROVENANCE.md) identifies the source snapshot and transformation.

Internal drafting flags and planning material are not part of this publication.

## Companion material

This repository holds the normative text (`spec/`) and the Deployment Guide
(`guide/`). Each guide chapter carries the section's operational questions, its
design rationale, and a non-normative account of how the Constable reference
implementation maintains the invariant in operation (`How We Do It`). Material
published outside the repository:

- **[zerotrustgovernance.io](https://zerotrustgovernance.io)** — public home of
  the specification: reading order, current draft status, and the essays the
  normative chapters cite (§1.0 Preserving Human Agency, continuous
  ratification, the Invariant/Envelope separation).
- **[shadowdynamicsystems.com](https://shadowdynamicsystems.com)** — the
  anti-pattern guide and the diagnosis (DX) and prescription (RX) series: the
  failure modes each invariant is written to exclude, and the design
  requirements that exclude them.
- **[constable.id](https://constable.id)** — the reference implementation.
  Nothing on that site is normative; conformance language is governed by
  the *Conformance claims* section below.

## Conformance claims

No ZTG conformance-certification authority or conformance-mark program currently
exists. Publication of this draft does not authorize a claim that an implementation is
officially certified, endorsed, or “ZTG Conformant.” Descriptive statements such as
“implements concepts derived from ZTG” remain distinct from reserved official-status
claims. Trademarks and names are not licensed, and no grant authorizes passing off a
nonconforming or uncertified system as conforming or certified.

## Licenses
Normative specification: OWFa 1.0
Deployment Guide and explanatory documentation: ZTG Documentation License 1.0
Schemas and tooling: Apache License 2.0
Constable: Copyright 2026 Shadow Dynamic Systems LLC.
Zero Trust Governance: 
See [`LICENSES.md`](LICENSES.md) for additional detail
