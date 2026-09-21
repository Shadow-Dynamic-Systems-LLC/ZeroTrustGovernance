# Publication provenance

The `0.8-draft-2026-09-21` snapshot was produced on 2026-09-21 from the ZTG
drafting workspace at source commit `18e9c31`.

The transformation is mechanical and reproducible with
[`tools/split-drafting-source.py`](tools/split-drafting-source.py):

- each chapter's `Normative` section is copied verbatim into `spec/`;
- §2 definitions are copied verbatim into `spec/`;
- introductions, operational framing, scope discussion, and further considerations are
  copied verbatim into `guide/`;
- `How We Do It` sections are copied verbatim into `guide/` under a heading marking
  them as the Constable reference implementation's account, non-normative;
- draft flags, working-draft notes, planning documents, and calibration files are
  excluded.

The split changes publication boundaries, not the source wording. Subsequent changes to
normative files are governed by [`GOVERNANCE.md`](GOVERNANCE.md).
