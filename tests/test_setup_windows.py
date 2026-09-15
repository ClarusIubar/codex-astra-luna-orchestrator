import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("pwsh"), "pwsh is required")
class WindowsSetupTests(unittest.TestCase):
    def test_default_install_accepts_each_component_prompt(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target"
            target.mkdir()
            answers = f"{target}\n1\ny\ny\ny\n"
            result = subprocess.run(
                ["pwsh", "-NoProfile", "-File", str(ROOT / "setup.ps1")],
                input=answers,
                text=True,
                encoding="utf-8",
                capture_output=True,
                check=False,
                timeout=30,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Setup complete. 3 component(s) installed", result.stdout)
            self.assertTrue((target / ".codex" / "config.toml").is_file())
            self.assertTrue((target / ".agents" / "skills" / "astra-orchestrator" / "SKILL.md").is_file())
            self.assertTrue((target / "AGENTS.md").is_file())


if __name__ == "__main__":
    unittest.main()
