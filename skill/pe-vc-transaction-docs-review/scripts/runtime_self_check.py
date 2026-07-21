#!/usr/bin/env python3
"""Check local runtime readiness without network access or user documents."""

from __future__ import annotations

import argparse
import importlib.util
import json
import platform
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIN_PYTHON = (3, 9)
CORE_JSON = (
    ROOT / "references" / "benchmark-data.json",
    ROOT / "references" / "legal-authorities.json",
)


def module_available(name: str) -> bool:
    try:
        return importlib.util.find_spec(name) is not None
    except (ImportError, AttributeError, ValueError):
        return False


def load_json(path: Path) -> tuple[bool, str]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return False, f"{type(exc).__name__}: {exc}"
    if not isinstance(payload, dict):
        return False, "top-level JSON value must be an object"
    return True, "ok"


def build_report() -> dict[str, object]:
    python_ready = sys.version_info >= MIN_PYTHON
    data_checks = {}
    for path in CORE_JSON:
        ok, detail = load_json(path)
        data_checks[str(path.relative_to(ROOT))] = {"ready": ok, "detail": detail}

    optional = {
        "word_comments": {
            "ready": module_available("lxml"),
            "requires": ["lxml"],
            "fallback": "produce a comment plan instead of native Word comments",
        },
        "blind_evaluation": {
            "ready": all(module_available(name) for name in ("docx", "lxml", "PIL")),
            "requires": ["python-docx", "lxml", "Pillow"],
            "fallback": "skip synthetic document rendering; core review remains available",
        },
        "macos_ocr": {
            "ready": platform.system() == "Darwin" and shutil.which("xcrun") is not None,
            "requires": ["macOS", "xcrun", "Vision framework"],
            "fallback": "request a searchable PDF, original Word file, or clearer scans",
        },
        "cross_platform_ocr": {
            "ready": bool(
                (shutil.which("ocrmypdf") and shutil.which("pdftotext"))
                or (shutil.which("tesseract") and shutil.which("pdftoppm"))
            ),
            "requires": ["OCRmyPDF + pdftotext, or Tesseract + pdftoppm"],
            "fallback": "use macOS Vision when available, or request a searchable PDF/Word source",
        },
        "pdf_text": {
            "ready": bool(shutil.which("pdftotext") or module_available("pypdf") or module_available("fitz")),
            "requires": ["pdftotext, pypdf, or PyMuPDF"],
            "fallback": "provide a searchable PDF/Word source or mark the PDF as unreadable",
        },
    }
    core_ready = python_ready and all(item["ready"] for item in data_checks.values())
    errors = []
    if not python_ready:
        errors.append("RUNTIME-001: Python 3.9 or newer is required")
    errors.extend(
        f"RUNTIME-001: {name} is not ready ({item['detail']})"
        for name, item in data_checks.items()
        if not item["ready"]
    )
    warnings = [
        f"Optional capability unavailable: {name}; {item['fallback']}"
        for name, item in optional.items()
        if not item["ready"]
    ]
    return {
        "check": "runtime_self_check",
        "network_used": False,
        "user_documents_read": False,
        "python": {
            "ready": python_ready,
            "version": platform.python_version(),
            "minimum": ".".join(map(str, MIN_PYTHON)),
        },
        "core_data": data_checks,
        "optional_capabilities": optional,
        "core_ready": core_ready,
        "errors": errors,
        "warnings": warnings,
    }


def print_text(report: dict[str, object]) -> None:
    print(f"Core review ready: {'yes' if report['core_ready'] else 'no'}")
    for error in report["errors"]:
        print(f"ERROR: {error}", file=sys.stderr)
    for warning in report["warnings"]:
        print(f"WARNING: {warning}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args()
    try:
        report = build_report()
    except Exception as exc:  # defensive CLI boundary
        report = {
            "check": "runtime_self_check",
            "network_used": False,
            "user_documents_read": False,
            "core_ready": False,
            "errors": [f"RUNTIME-001: unexpected self-check failure: {exc}"],
            "warnings": [],
        }
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text(report)
    return 0 if report["core_ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
