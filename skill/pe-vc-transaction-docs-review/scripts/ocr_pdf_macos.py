#!/usr/bin/env python3
"""OCR image/scanned PDFs with Poppler pdftoppm and macOS Vision."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def find_pdftoppm() -> str | None:
    env_path = os.environ.get("PDFTOPPM")
    home = Path.home()
    candidates = [
        env_path,
        shutil.which("pdftoppm"),
        str(home / ".cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdftoppm"),
        "/opt/homebrew/bin/pdftoppm",
        "/usr/local/bin/pdftoppm",
    ]
    for c in candidates:
        if c and Path(c).exists():
            return c
    return None


def natural_page_key(path: Path) -> list[object]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", path.name)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--max-pages", type=int, default=0, help="0 means all pages")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--allow-partial", action="store_true", help="Return success even if one or more pages fail OCR.")
    args = ap.parse_args()

    pdf = args.pdf.expanduser()
    if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
        print(f"PDF not found: {pdf}", file=sys.stderr)
        return 2
    if args.max_pages < 0:
        print("--max-pages must be zero or greater.", file=sys.stderr)
        return 2
    if args.dpi < 72 or args.dpi > 600:
        print("--dpi must be between 72 and 600.", file=sys.stderr)
        return 2
    pdftoppm = find_pdftoppm()
    if not pdftoppm:
        print("pdftoppm not found. Install Poppler or use Codex bundled runtime.", file=sys.stderr)
        return 2
    swift = shutil.which("swift")
    if not swift:
        print("swift not found; macOS Vision OCR requires /usr/bin/swift.", file=sys.stderr)
        return 2
    swift_script = Path(__file__).with_name("ocr_vision.swift")

    with tempfile.TemporaryDirectory(prefix="vcpe_pdf_ocr_") as td:
        prefix = Path(td) / "page"
        cmd = [pdftoppm, "-png", "-r", str(args.dpi)]
        if args.max_pages > 0:
            cmd += ["-f", "1", "-l", str(args.max_pages)]
        cmd += [str(pdf), str(prefix)]
        proc = subprocess.run(cmd, text=True, capture_output=True, check=False)
        if proc.returncode != 0:
            print(proc.stderr.strip() or "pdftoppm failed", file=sys.stderr)
            return 1
        images = sorted(Path(td).glob("page-*.png"), key=natural_page_key)
        if not images:
            print("No page images generated for OCR.", file=sys.stderr)
            return 1
        chunks: list[str] = []
        failed_pages: list[int] = []
        for i, image in enumerate(images, start=1):
            ocr = subprocess.run([swift, str(swift_script), str(image)], text=True, capture_output=True, check=False)
            if ocr.returncode != 0:
                failed_pages.append(i)
                chunks.append(f"\n===== PAGE {i} OCR FAILED =====\n{ocr.stderr.strip()}\n")
            else:
                chunks.append(f"\n===== PAGE {i} =====\n{ocr.stdout.strip()}\n")
        text = "\n".join(chunks).strip() + "\n"

    if args.output:
        try:
            args.output.expanduser().write_text(text, encoding="utf-8")
        except OSError as exc:
            print(f"Could not write OCR output: {exc}", file=sys.stderr)
            return 2
    else:
        print(text)
    if failed_pages:
        print(f"OCR failed on page(s): {', '.join(str(page) for page in failed_pages)}", file=sys.stderr)
        return 0 if args.allow_partial else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
