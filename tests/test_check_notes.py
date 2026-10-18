import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_notes.py"
SPEC = importlib.util.spec_from_file_location("check_notes", SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class CheckNotesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.original_root = checker.ROOT
        self.addCleanup(setattr, checker, "ROOT", self.original_root)
        checker.ROOT = Path(self.temp.name).resolve()
        self.path = checker.ROOT / "movies/Film-2012/dialogues/dialogue.md"
        self.path.parent.mkdir(parents=True)
        self.template = (
            self.original_root / "movies/_template/dialogues/dialogue.md"
        ).read_text()

    def write(self, text):
        self.path.write_text(text)
        return checker.check_note(self.path)

    def test_template_is_accepted(self):
        self.assertEqual(self.write(self.template), [])

    def test_dialogue_toc_is_accepted(self):
        toc = "## 目次\n\n- [001：［台詞の短い見出し］](#dialogue-001)\n\n"
        text = self.template.replace('<a id="dialogue-001">', toc + '<a id="dialogue-001">', 1)
        self.assertEqual(self.write(text), [])

    def test_broken_toc_link_is_rejected(self):
        toc = "## 目次\n\n- [001：［台詞の短い見出し］](#dialogue-002)\n\n"
        text = self.template.replace('<a id="dialogue-001">', toc + '<a id="dialogue-001">', 1)
        self.assertTrue(any("目次の項目" in e for e in self.write(text)))

    def test_original_wrong_path_is_rejected(self):
        path = checker.ROOT.parent / "Gangs of Wasseypur/セリフと日本語訳.md"
        self.assertTrue(any("リポジトリ外" in e for e in checker.check_note(path)))

    def test_original_translation_only_format_is_rejected(self):
        errors = self.write("# 台詞集\n\n## 1\n\n原文\n\n**日本語訳：** 訳\n")
        self.assertTrue(any("本文→直訳" in e for e in errors))

    def test_wrong_folder_inside_repository_is_rejected(self):
        path = checker.ROOT / "Gangs of Wasseypur/セリフと日本語訳.md"
        self.assertTrue(any("命名規則" in e for e in checker.check_note(path)))

    def test_song_template_is_accepted(self):
        path = checker.ROOT / "movies/Film-2012/songs/Song-Title.md"
        path.parent.mkdir(parents=True)
        path.write_text((self.original_root / "movies/_template/songs/Song-Title.md").read_text())
        self.assertEqual(checker.check_note(path), [])

    def test_empty_grammar_is_rejected(self):
        start = self.template.index("### 文法説明\n")
        end = self.template.index("### 補足\n")
        errors = self.write(self.template[:start] + "### 文法説明\n\n" + self.template[end:])
        self.assertTrue(any("文法説明 が空" in e for e in errors))

    def test_wrong_vocabulary_columns_are_rejected(self):
        errors = self.write(self.template.replace("本文の形 | 基本形", "語 | 訳"))
        self.assertTrue(any("語彙表の5列" in e for e in errors))

    def test_wrong_anchor_is_rejected(self):
        errors = self.write(self.template.replace('id="dialogue-001"', 'id="dialogue-002"'))
        self.assertTrue(any("アンカー" in e for e in errors))

    def test_intro_is_rejected(self):
        errors = self.write(self.template.replace("\n\n", "\n\n作成手順の説明。\n\n", 1))
        self.assertTrue(any("前置き" in e for e in errors))

    def test_symlink_outside_repository_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "dialogue.md"
            target.write_text(self.template)
            self.path.symlink_to(target)
            self.assertTrue(any("リポジトリ外" in e for e in checker.check_note(self.path)))


if __name__ == "__main__":
    unittest.main()
