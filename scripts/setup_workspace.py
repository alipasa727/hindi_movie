#!/usr/bin/env python3
"""Install the workspace entry instructions without replacing existing rules."""

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


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    if root != Path("/workspace/hindi_movie"):
        raise SystemExit("この配置処理は /workspace/hindi_movie のクラウド環境専用です")
    install(root / "scripts/workspace-AGENTS.md", Path("/workspace/AGENTS.md"))
