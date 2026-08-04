"""Validate the C1-2 evidence manifest."""

from __future__ import annotations

import argparse
from pathlib import Path
import tomllib


def validate(root: Path) -> list[str]:
    """Return manifest consistency findings."""

    manifest_path = root / "evidence" / "manifest.toml"
    if not manifest_path.is_file():
        return ["evidence/manifest.toml is missing"]
    with manifest_path.open("rb") as manifest_file:
        manifest = tomllib.load(manifest_file)
    findings: list[str] = []
    seen: set[str] = set()
    for item in manifest.get("requirements", []):
        requirement_id = item.get("id", "")
        status = item.get("status", "")
        files = item.get("files", [])
        if not requirement_id or requirement_id in seen:
            findings.append(f"invalid or duplicate id: {requirement_id}")
        seen.add(requirement_id)
        if status not in {"complete", "pending"}:
            findings.append(f"{requirement_id}: invalid status")
        if status == "complete" and not files:
            findings.append(f"{requirement_id}: complete item has no evidence")
        for relative_path in files:
            if not (root / relative_path).is_file():
                findings.append(f"{requirement_id}: missing {relative_path}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("validate",))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    findings = validate(args.root.resolve())
    if findings:
        print("\n".join(f"[FAIL] {finding}" for finding in findings))
        return 1
    print("[OK] evidence manifest is consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
