#!/usr/bin/env python3
"""Basic docs guardrails for CI.

This validator is intentionally lightweight:
- verifies docs folder exists
- verifies mkdocs config exists
- verifies docs home page exists
- if Firebase rules files exist, ensures documentation contains references
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
MKDOCS_FILE = ROOT / "mkdocs.yml"
HOME_PAGE = DOCS_DIR / "index.md"


def fail(message: str) -> None:
    print(f"[docs-validate] ERROR: {message}")
    sys.exit(1)


if not DOCS_DIR.is_dir():
    fail("Missing docs directory at ./docs")

if not MKDOCS_FILE.is_file():
    fail("Missing mkdocs.yml at repository root")

if not HOME_PAGE.is_file():
    fail("Missing docs/index.md")

firestore_rules = ROOT / "firebase" / "firestore.rules"
storage_rules = ROOT / "firebase" / "storage.rules"

if firestore_rules.exists() or storage_rules.exists():
    docs_text = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in DOCS_DIR.rglob("*.md")
    ).lower()
    if "firestore" not in docs_text and "storage" not in docs_text and "firebase" not in docs_text:
        fail(
            "Firebase rules files exist, but docs do not reference firebase/firestore/storage"
        )

print("[docs-validate] OK")
