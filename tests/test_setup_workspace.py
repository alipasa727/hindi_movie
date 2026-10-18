import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/setup_workspace.py"
SPEC = importlib.util.spec_from_file_location("setup_workspace", SCRIPT)
setup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(setup)


class SetupWorkspaceTests(unittest.TestCase):
    def test_install_is_repeatable_and_preserves_other_instructions(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            destination = Path(directory) / "AGENTS.md"
            source.write_text("入口の指示\n")
            setup.install(source, destination)
            setup.install(source, destination)
            self.assertEqual(destination.read_text(), source.read_text())
            destination.write_text("既存の別の指示\n")
            with self.assertRaises(SystemExit):
                setup.install(source, destination)
            self.assertEqual(destination.read_text(), "既存の別の指示\n")
