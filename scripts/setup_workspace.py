#!/usr/bin/env python3
"""Install the workspace entry instructions without replacing existing rules."""

import argparse
from pathlib import Path


def install(source, destination):
    content = source.read_text(encoding="utf-8")
    try:
        with destination.open("x", encoding="utf-8") as output:
            output.write(content)
    except FileExistsError:
        if destination.read_text(encoding="utf-8") != content:
            raise SystemExit(f"既存の指示は上書きしません: {destination}")
    print(f"作業開始時の案内を確認しました: {destination}")


def check(source, destination):
    """Detect a missing or stale entry point without changing existing files."""
    if not destination.is_file():
        raise SystemExit(f"作業開始時の案内が未配置です: {destination}")
    if destination.read_text(encoding="utf-8") != source.read_text(encoding="utf-8"):
        raise SystemExit(f"作業開始時の案内が原本と一致しません: {destination}")
    print(f"作業開始時の案内の配置と内容を検査しました: {destination}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="配置済みの案内を変更せず検査する")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    if root != Path("/workspace/hindi_movie"):
        raise SystemExit("この配置処理は /workspace/hindi_movie のクラウド環境専用です")
    action = check if args.check else install
    action(root / "scripts/workspace-AGENTS.md", Path("/workspace/AGENTS.md"))
