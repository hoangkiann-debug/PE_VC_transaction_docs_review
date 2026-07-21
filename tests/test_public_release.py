from __future__ import annotations

import csv
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "pe-vc-transaction-docs-review"
SCRIPTS = SKILL / "scripts"
sys.path.insert(0, str(SCRIPTS))


def load_module(name: str):
    path = SCRIPTS / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class PublicReleaseTests(unittest.TestCase):
    def test_identity_and_required_files(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: pe-vc-transaction-docs-review\n"))
        self.assertIn("# PE/VC私募交易文件审阅", text)
        self.assertIn("## 典型使用案例", text)
        self.assertIn("## 常见问题", text)
        self.assertIn("## 常见错误用法与正确处理", text)
        self.assertIn("### 默认低门槛模式", text)
        self.assertIn("### 普通用户直接照抄", text)
        self.assertIn("### 与通用合同审阅的区别", text)
        self.assertIn("### 触发优先级", text)
        self.assertIn("### 参考资料三层导航", text)
        self.assertIn("references/complete-output-example.md", text)
        self.assertIn("references/faq-and-troubleshooting.md", text)
        self.assertIn("license: Apache-2.0", text)
        self.assertTrue((SKILL / "agents" / "openai.yaml").is_file())
        self.assertTrue((SKILL / "assets" / "review-preferences-template.md").is_file())
        self.assertTrue((SCRIPTS / "review_checkpoint.py").is_file())
        self.assertTrue((SCRIPTS / "ocr_pdf.py").is_file())
        self.assertIn(
            "用户实际看到的白话提示",
            (SKILL / "references" / "faq-and-troubleshooting.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Data Completeness Gate",
            (SKILL / "references" / "market-benchmarks-2024-2025.md").read_text(encoding="utf-8"),
        )

    def test_outward_documentation_copy(self):
        forbidden = [
            "公开版" + "不包含",
            "公开版本" + "采用明确的文件白名单",
            "It intentionally" + " does not include",
            "It excludes" + " client",
            "public package" + " intentionally omits",
        ]
        for path in [ROOT / "README.md", ROOT / "PRIVACY.md", SKILL / "SKILL.md", SKILL / "references" / "article-digest.md"]:
            content = path.read_text(encoding="utf-8")
            for phrase in forbidden:
                self.assertNotIn(phrase, content, f"removed outward wording returned in {path}")

    def test_every_routed_resource_exists(self):
        pattern = re.compile(r"(?<![A-Za-z0-9_.-])((?:references|scripts|assets)/[A-Za-z0-9_./&:-]+(?:\.md|\.json|\.py|\.swift|\.csv))")
        for markdown in [SKILL / "SKILL.md", *(SKILL / "references").glob("*.md")]:
            for relative in pattern.findall(markdown.read_text(encoding="utf-8")):
                self.assertTrue((SKILL / relative).is_file(), f"broken route: {relative}")

    def test_public_benchmark_is_redacted_and_searchable(self):
        data = json.loads((SKILL / "references" / "benchmark-data.json").read_text(encoding="utf-8"))
        self.assertEqual(data["distribution_profile"], "public")
        self.assertNotIn("source_registry", data)
        self.assertTrue(data["benchmarks"])
        for item in data["benchmarks"]:
            self.assertNotIn("citations", item)
        completed = subprocess.run(
            [sys.executable, str(SCRIPTS / "benchmark_lookup.py"), "redemption", "--json"],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertGreater(len(payload["matches"]), 0)
        self.assertNotIn("source_registry", payload)
        rendered = " ".join(item["benchmark"] for item in payload["matches"])
        self.assertNotRegex(rendered, r"\d+\.\d+%")
        self.assertIn("about", rendered)

    def test_core_routing_and_ontology(self):
        document_map = load_module("build_document_map")
        ontology = load_module("contract_ontology")
        self.assertEqual(document_map.classify(Path("A轮增资协议.docx")), "investment/subscription agreement")
        self.assertEqual(document_map.classify(Path("Series A SHA.docx")), "shareholders agreement")
        self.assertTrue(ontology.CLAUSE_FAMILIES)

    def test_legal_registry_and_consistency_validator(self):
        completed = subprocess.run(
            [sys.executable, str(SCRIPTS / "validate_skill_consistency.py")],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("23 complete benchmark topics", completed.stdout)
        completed = subprocess.run(
            [sys.executable, str(SCRIPTS / "legal_authority_lookup.py"), "公司法", "--json", "--check-freshness"],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertGreater(len(json.loads(completed.stdout)["matches"]), 0)

    def test_checkpoint_and_ocr_router(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "agreement.txt"
            state = root / "review-state.json"
            source.write_text("version one", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "review_checkpoint.py"), "init", str(state),
                 "--matter-id", "synthetic", "--source", str(source)],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertNotIn("version one", state.read_text(encoding="utf-8"))
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "review_checkpoint.py"), "autosave", str(state),
                 "document_map", "--unit", "file-001"],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            payload = json.loads(completed.stdout)
            self.assertEqual(payload["stages"]["document_map"]["status"], "in_progress")
            self.assertEqual(payload["stages"]["document_map"]["completed_units"], ["file-001"])
        completed = subprocess.run(
            [sys.executable, str(SCRIPTS / "ocr_pdf.py"), "--list-engines"],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIsInstance(json.loads(completed.stdout)["available_engines"], list)

    def test_package_conflicts_and_clean_version_delta(self):
        package_matrix = load_module("build_package_matrix")
        version_compare = load_module("compare_contract_versions")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "investment.txt").write_text(
                '第一条 定义\n\n“交割日”系指2026年8月1日。\n\n'
                '第二条 股权结构\n\n交割后创始股东持有公司60%，投资人持有公司40%。\n\n'
                '公司注册资本为人民币1,000,000元。',
                encoding="utf-8",
            )
            (root / "articles.txt").write_text(
                '第五条 定义\n\n“交割日”系指2026年9月1日。\n\n'
                '第六条 股权结构\n\n交割后创始股东持有公司55%，投资人持有公司45%。\n\n'
                '公司注册资本为人民币1,200,000元。',
                encoding="utf-8",
            )
            matrix = package_matrix.build_matrix([root])
            self.assertTrue(matrix["definition_conflicts"])
            self.assertTrue(matrix["numeric_fact_conflicts"])

            prior = root / "prior.txt"
            current = root / "current.txt"
            prior.write_text("1. Redemption\nThe annual simple interest rate is 8%.", encoding="utf-8")
            current.write_text("1. Redemption\nThe annual simple interest rate is 10%.", encoding="utf-8")
            delta = version_compare.compare_documents(prior, current)
            self.assertGreater(delta["change_block_count"], 0)
            self.assertGreater(delta["clause_change_count"], 0)

    @unittest.skipUnless(importlib.util.find_spec("lxml"), "lxml optional dependency not installed")
    def test_native_word_comment_apply_and_rollback(self):
        comments = load_module("apply_comment_plan")
        schema = load_module("review_schema")
        anchor = "Any expenditure requires prior investor consent."
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "agreement.docx"
            reviewed = root / "reviewed.docx"
            restored = root / "restored.docx"
            plan = root / "comments.csv"
            report_path = root / "apply-report.json"
            document = (
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                f'<w:body><w:p><w:r><w:t>{anchor}</w:t></w:r></w:p></w:body></w:document>'
            )
            content_types = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                '<Default Extension="xml" ContentType="application/xml"/>'
                '<Override PartName="/word/document.xml" '
                'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
                '</Types>'
            )
            relationships = (
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'
            )
            with zipfile.ZipFile(source, "w") as archive:
                archive.writestr("[Content_Types].xml", content_types)
                archive.writestr("word/document.xml", document)
                archive.writestr("word/_rels/document.xml.rels", relationships)
            with plan.open("w", newline="", encoding="utf-8-sig") as handle:
                writer = csv.DictWriter(handle, fieldnames=schema.COMMENT_HEADERS["en"])
                writer.writeheader()
                writer.writerow(
                    {
                        "file": source.name,
                        "location": "paragraph 1",
                        "anchor_text": anchor,
                        "risk": "High",
                        "issue_type": "Governance",
                        "comment_text": "Issue: consent is too broad. Proposed revision: add a materiality threshold.",
                        "proposed_revised_wording": "Add a materiality threshold.",
                        "fallback": "Limit consent to reserved matters.",
                        "needs_client_input": "Confirm threshold.",
                    }
                )
            report = comments.apply_comments(source, plan, reviewed)
            report_path.write_text(json.dumps(report), encoding="utf-8")
            rollback = comments.rollback_comments(reviewed, report_path, restored)
            self.assertTrue(report["ok"], report)
            self.assertTrue(report["visible_text_unchanged"])
            self.assertTrue(report["source_file_unchanged"])
            self.assertTrue(rollback["ok"], rollback)
            self.assertTrue(rollback["visible_text_matches_source"])


if __name__ == "__main__":
    unittest.main()
