# ZTG governance

This document summarizes the stewardship and amendment procedure ratified on
2026-09-08. It governs the ZTG specification family; it does not adopt ZTG v0.8.

## Current stewardship

Shadow Dynamic Systems LLC is the current caretaker of the ZTG specification. While
SDS holds stewardship, final discretion over official modifications and amendments is
held by the Founder in the capacity of Managing Partner.

Architecture work may draft and maintain specification text, but a draft does not alter
the official ZTG specification. Independently modified copies and forks may exist, but
they are not official ZTG publications and carry no amendment authority.

## Amendment procedure

Every proposed addition, removal, or modification of a normative invariant, definition,
or section is submitted as a sequential, never-reused `ZTG-AMEND-NNN` record. A record
must contain:

- the exact proposed normative text;
- the rationale;
- all affected provisions;
- its current disposition;
- the recorded adoption authority; and
- the version in which an adopted change becomes effective.

Allowed dispositions are `proposed`, `under-review`, `adopted`, `rejected`,
`withdrawn`, and `superseded`. Disposition history is append-only. A materially revised
proposal receives a new identifier rather than reopening a terminal record.

Under current stewardship, an amendment becomes official only after recorded SDS
review and a Founder decision. Receipt, discussion, or merge of a contribution is not
adoption.

## Decision register

Every terminal amendment disposition is recorded in an append-only decision register,
including rejected, withdrawn, and superseded amendments. Corrections are new entries;
existing entries are not edited or deleted. Each entry identifies the amendment, date,
disposition, decision authority, effective version where applicable, and a short
summary.

The register continues across any future stewardship transfer.

## Successor stewardship

The ZTG host organization is intended to move to a legally and factually separate
nonprofit foundation when resources permit the necessary legal and financial work. The
Founder expects to remain Steward with constrained business authority.

A transfer must itself be recorded as a governed event. No successor review board,
quorum rule, or committee structure exists until the successor entity creates one.

## Conformance governance reservation

Specification adoption and conformance certification are separate questions.
Authority to certify implementations, issue conformance marks, or operate an assessment
program has not been assigned to SDS, a future foundation, or any other body.
