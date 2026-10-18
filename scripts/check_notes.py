#!/usr/bin/env python3
"""Check learning-note paths and structure; this does not assess translation accuracy."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = ["本文", "直訳", "語彙説明", "文法説明", "補足"]
VOCAB_HEADER = "| 本文の形 | 基本形 | 品詞 | 意味 | 活用・語尾の働き |"
PROJECT_DOCS = {"AGENTS.md", "README.md", "SOURCES.md", "GRAMMAR_LEGEND.md",
                "scripts/workspace-AGENTS.md"}
REFERENCE_FILES = {
    "movies/Muthu-1995/dialogues/dialogue.md",
    "movies/Muthu-1995/songs/Kokku-Saiva-Kokku.md",
    "movies/Muthu-1995/songs/Kuluvalile.md",
    "movies/Muthu-1995/songs/Thillana-Thillana.md",
}


def check_note(path):
    """Return errors for a path, resolving symlinks before checking its location."""
    path = Path(path).resolve()
    try:
        relative = path.relative_to(ROOT).as_posix()
    except ValueError:
        return [f"{path}: 保存先がリポジトリ外です"]
    if relative in PROJECT_DOCS:
        return []
    pattern = r"movies/(?:[^/\s]+-\d{4}|_template)/(dialogues|songs)/([^/]+)\.md"
    match = re.fullmatch(pattern, relative)
    if not match:
        return [f"{relative}: 映画名-公開年/dialogues または songs の命名規則に違反しています"]
    category, filename = match.groups()
    if category == "dialogues" and filename != "dialogue":
        return [f"{relative}: 台詞は dialogues/dialogue.md にまとめてください"]
    if category == "songs" and re.search(r"\s", filename):
        return [f"{relative}: 曲名の空白はハイフンにしてください"]
    if not path.is_file():
        return [f"{relative}: ファイルがありません"]
    if relative in REFERENCE_FILES:
        return []

    text = path.read_text(encoding="utf-8")
    errors = []

    def fail(message):
        errors.append(f"{relative}: {message}")

    if len(re.findall(r"^# .+$", text, re.M)) != 1:
        fail("先頭見出しは1つ必要です")
    summary = "<summary>出典と確認範囲</summary>"
    if text.count(summary) != 1 or not text.rstrip().endswith("</details>"):
        fail("末尾に出典と確認範囲をまとめてください")
    body = text.split("<details>", 1)[0]
    # Anchors may precede each numbered dialogue; they are not an introduction.
    body = re.sub(r'<a id="dialogue-\d{3,}"></a>\s*', "", body)
    pieces = re.split(r"^## (.+)\n", body, flags=re.M)
    if len(pieces) < 3:
        fail("台詞・歌詞の節がありません")
    preamble = re.sub(r"\A# [^\n]+\n", "", pieces[0]).strip()
    if preamble:
        fail("先頭見出しと本文の間に前置きを置かないでください")

    sections = list(zip(pieces[1::2], pieces[2::2]))
    if category == "dialogues" and sections and sections[0][0] == "目次":
        _, toc = sections.pop(0)
        expected = []
        for title, _ in sections:
            number = re.match(r"(\d{3,})：", title)
            if number:
                expected.append(f"- [{title}](#dialogue-{number.group(1)})")
        if [line.strip() for line in toc.splitlines() if line.strip()] != expected:
            fail("目次の項目・順序・リンクを台詞の見出しに合わせてください")
        if not sections:
            fail("目次に対応する台詞の節がありません")

    numbers = []
    for title, section in sections:
        divisions = re.split(r"^### (.+)\n", section, flags=re.M)
        if divisions[1::2] != HEADINGS:
            fail(f"{title}: 本文→直訳→語彙説明→文法説明→補足の順にしてください")
            continue
        contents = dict(zip(divisions[1::2], divisions[2::2]))
        for heading in HEADINGS[:-1]:
            if not contents[heading].strip():
                fail(f"{title}: {heading} が空です")
        if not re.search(r"^> \S", contents["本文"], re.M):
            fail(f"{title}: 本文の引用がありません")
        if VOCAB_HEADER not in contents["語彙説明"]:
            fail(f"{title}: 語彙表の5列が規定と異なります")
        if category == "dialogues":
            number = re.match(r"(\d{3,})：", title)
            if not number:
                fail(f"{title}: 番号付き見出しが必要です")
            else:
                numbers.append(number.group(1))

    if category == "dialogues":
        anchors = re.findall(r'<a id="dialogue-(\d{3,})"></a>', text)
        if numbers != anchors or len(set(anchors)) != len(anchors):
            fail("見出し番号とアンカーが一致しないか、重複しています")
    return errors


def main():
    paths = [Path(p) for p in sys.argv[1:]] if len(sys.argv) > 1 else sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.relative_to(ROOT).parts
    )
    errors = [error for path in paths for error in check_note(path)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"保存先・書式を確認しました（{len(paths)}個のMarkdownファイル、管理文書は本文形式の検査対象外）。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
