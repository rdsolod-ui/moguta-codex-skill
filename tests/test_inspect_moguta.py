from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "moguta-codex-skill" / "scripts" / "inspect_moguta.py"
SPEC = importlib.util.spec_from_file_location("inspect_moguta", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class InspectMogutaTests(unittest.TestCase):
    def test_detects_project_extensions_version_and_findings(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "mg-core").mkdir()
            (root / "mg-core" / "version.php").write_text(
                "<?php define('VER', '10.9.0');", encoding="utf-8"
            )
            plugin = root / "mg-plugins" / "demo-plugin"
            plugin.mkdir(parents=True)
            plugin.joinpath("index.php").write_text(
                """<?php
/*
Plugin Name: Demo
Description: Test plugin
Author: Example
Version: 1.0.0
*/
DB::query("SELECT * FROM ".PREFIX."product WHERE id=".$_GET['id']);
""",
                encoding="utf-8",
            )
            template = root / "mg-templates" / "demo-template"
            (template / "css").mkdir(parents=True)
            (template / "components").mkdir()
            (template / "template.php").write_text("<?php mgMeta('css');", encoding="utf-8")
            (template / "css" / "style.css").write_text("body{}", encoding="utf-8")

            report = MODULE.discover(root, 500)

            self.assertTrue(report["is_moguta"])
            self.assertEqual(report["version_candidates"][0]["value"], "10.9.0")
            self.assertEqual(report["summary"]["plugins"], 1)
            self.assertEqual(report["summary"]["templates"], 1)
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("dynamic-sql-superglobal", codes)
            self.assertIn("component-config-missing", codes)

    def test_clean_standalone_plugin(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            root.joinpath("index.php").write_text(
                """<?php
/*
Plugin Name: Demo
Description: Test plugin
Author: Example
Version: 1.0.0
*/
""",
                encoding="utf-8",
            )
            report = MODULE.discover(root, 100)
            self.assertTrue(report["is_moguta"])
            self.assertEqual(report["summary"]["plugins"], 1)
            self.assertEqual(report["summary"]["errors"], 0)

    def test_bom_and_incomplete_metadata_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            root.joinpath("index.php").write_bytes(
                b"\xef\xbb\xbf<?php /* Plugin Name: Demo */"
            )
            report = MODULE.discover(root, 100)
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("php-bom", codes)
            self.assertIn("plugin-metadata-incomplete", codes)

    def test_json_cli_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "mg-pages").mkdir()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(root), "--json"],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertTrue(payload["is_moguta"])

    def test_version_13_1_warns_about_noncomponent_template(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            core = root / "mg-core"
            core.mkdir()
            core.joinpath("version.php").write_text(
                "<?php define('VER', '13.1.1');", encoding="utf-8"
            )
            template = root / "mg-templates" / "legacy"
            (template / "css").mkdir(parents=True)
            template.joinpath("template.php").write_text("<?php", encoding="utf-8")
            (template / "css" / "style.css").write_text("body{}", encoding="utf-8")

            report = MODULE.discover(root, 100)
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("noncomponent-template-unsupported", codes)

    def test_version_13_warns_about_tcpdf_extension(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            core = root / "mg-core"
            core.mkdir()
            core.joinpath("version.php").write_text(
                "<?php define('VER', '13.0.0');", encoding="utf-8"
            )
            plugin = root / "mg-plugins" / "legacy-pdf"
            plugin.mkdir(parents=True)
            plugin.joinpath("index.php").write_text(
                """<?php
/*
Plugin Name: Legacy PDF
Description: Compatibility fixture
Version: 1.0.0
*/
$pdf = new TCPDF();
""",
                encoding="utf-8",
            )

            report = MODULE.discover(root, 100)
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("legacy-tcpdf-reference", codes)

    def test_version_gates_do_not_warn_before_their_release(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            core = root / "mg-core"
            core.mkdir()
            core.joinpath("version.php").write_text(
                "<?php define('VER', '12.0.0');", encoding="utf-8"
            )
            template = root / "mg-templates" / "legacy"
            (template / "css").mkdir(parents=True)
            template.joinpath("template.php").write_text("<?php", encoding="utf-8")
            (template / "css" / "style.css").write_text("body{}", encoding="utf-8")
            plugin = root / "mg-plugins" / "legacy-pdf"
            plugin.mkdir(parents=True)
            plugin.joinpath("index.php").write_text(
                "<?php /* Plugin Name: PDF */ new TCPDF();", encoding="utf-8"
            )

            report = MODULE.discover(root, 100)
            codes = {item["code"] for item in report["findings"]}
            self.assertNotIn("noncomponent-template-unsupported", codes)
            self.assertNotIn("legacy-tcpdf-reference", codes)


if __name__ == "__main__":
    unittest.main()
