#!/usr/bin/env python3
# Copyright 2026 Shadow Dynamic Systems LLC
# Licensed under the Apache License, Version 2.0.
"""Split ZTG drafting sources into normative and explanatory publications.

Usage: python3 tools/split-drafting-source.py /path/to/ztg-v1-drafting

Normative and explanatory wording is copied verbatim. SDS implementation sections
and internal drafting notes are excluded.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_CHAPTER = "section-14-irreversibility-of-harm-ztg-5-calibration.md"
INTRO_FILES = (
    "section-1-0-preserving-human-agency.md",
    "introduction-reference.md",
    "bridge-what-ztg-is-built-to-prevent.md",
)


def section_blocks(text: str) -> tuple[list[str], list[tuple[str, list[str]]]]:
    lines = text.rstrip().splitlines()
    preamble: list[str] = []
    blocks: list[tuple[str, list[str]]] = []
    heading = ""
    current: list[str] = []
    for line in lines:
        if line.startswith("## "):
            if heading:
                blocks.append((heading, current))
            elif current:
                preamble = current
            heading = line
            current = [line]
        else:
            current.append(line)
    if heading:
        blocks.append((heading, current))
    elif current:
        preamble = current
    return preamble, blocks


def clean_join(parts: list[list[str]]) -> str:
    return "\n\n".join("\n".join(part).strip() for part in parts if part).rstrip() + "\n"


def without_drafting_metadata(lines: list[str]) -> list[str]:
    """Drop the source-capture paragraph while retaining explanatory prose verbatim."""
    paragraphs = "\n".join(lines).strip().split("\n\n")
    if len(paragraphs) > 1:
        candidate = paragraphs[1].lower()
        if "this file" in candidate and ("draft" in candidate or "captures" in candidate):
            del paragraphs[1]
    return "\n\n".join(paragraphs).splitlines()


def chapter_key(path: Path) -> tuple[int, str]:
    match = re.match(r"section-(\d+)-", path.name)
    return (int(match.group(1)) if match else 999, path.name)


def publish_chapter(source: Path) -> None:
    text = source.read_text(encoding="utf-8")
    preamble, blocks = section_blocks(text)
    title = [text.splitlines()[0]]
    section_number = chapter_key(source)[0]
    if section_number == 2:
        normative = [title]
        normative.extend(lines for heading, lines in blocks if heading != "## Draft Flags")
        guide = [without_drafting_metadata(preamble)] if len(preamble) > 1 else []
    else:
        normative = [title]
        normative.extend(lines for heading, lines in blocks if heading == "## Normative")
        guide = [without_drafting_metadata(preamble)]
        guide.extend(
            lines
            for heading, lines in blocks
            if heading not in {"## Normative", "## How We Do It", "## Draft Flags"}
        )
    name = re.sub(r"^section-", "", source.name)
    (ROOT / "spec" / name).write_text(clean_join(normative), encoding="utf-8")
    if any(line.strip() for part in guide for line in part):
        (ROOT / "guide" / name).write_text(clean_join(guide), encoding="utf-8")


def publish_intro(source: Path) -> None:
    lines = source.read_text(encoding="utf-8").rstrip().splitlines()
    lines = without_drafting_metadata(lines)
    if source.name == "bridge-what-ztg-is-built-to-prevent.md":
        for index, line in enumerate(lines):
            if line == "### Working-Draft Notes":
                lines = lines[:index]
                break
    (ROOT / "guide" / source.name).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: split-drafting-source.py SOURCE_ROOT")
    source_root = Path(sys.argv[1]).resolve()
    for path in sorted((source_root / "chapters").glob("section-*.md"), key=chapter_key):
        if path.name != EXCLUDED_CHAPTER:
            publish_chapter(path)
    for name in INTRO_FILES:
        publish_intro(source_root / "01-introduction" / name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
