"""Regression tests for real child-thread orchestration defaults."""

from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class OrchestrationConfigTests(unittest.TestCase):
    def test_pro_and_plus_presets_enable_v2_child_creation(self) -> None:
        pro = (ROOT / ".codex" / "config.toml").read_text(encoding="utf-8")
        plus = (ROOT / ".codex" / "config.plus.toml").read_text(encoding="utf-8")

        self.assertIn('model_reasoning_effort = "ultra"', pro)
        self.assertIn("[features]", pro)
        self.assertIn("multi_agent_v2 = true", pro)
        self.assertIn("[features]", plus)
        self.assertIn("multi_agent_v2 = true", plus)


if __name__ == "__main__":
    unittest.main()
