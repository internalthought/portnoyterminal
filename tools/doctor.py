#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

from _utils import find_repo_root, ensure_codex_dir, run, read_file, timestamp


def py_compile_all(root: Path) -> dict:
    py_files = [str(p) for p in (root / "tools").glob("*.py")]
    if not py_files:
        return {"ok": True, "errors": []}
    code, out, err = run([sys.executable, "-m", "py_compile", *py_files], cwd=root)
    ok = code == 0
    return {"ok": ok, "errors": (out + err).strip().splitlines() if not ok else []}


def check_node_env(root: Path) -> dict:
    checks = {}
    for tool in ("node", "npm"):
        code, out, err = run([tool, "-v"], cwd=root)
        checks[tool] = {"ok": code == 0, "output": (out or err).strip()}
    return checks


def check_tests_detect(root: Path) -> dict:
    code, out, err = run([sys.executable, str(root / "tools" / "test.py"), "--detect"], cwd=root)
    return {"ok": code == 0, "stdout": out, "stderr": err}


def build_fix_prompt(root: Path, report: dict) -> str:
    return (
        "You are an expert at repairing the 'tools/' automation for Codex TDD.\n"
        "Analyze the diagnostics below and patch the Python tools to resolve issues.\n"
        "Keep changes minimal and focused; maintain backward compatibility.\n\n"
        f"Repo: {root}\n"
        f"Timestamp: {timestamp()}\n\n"
        "Diagnostics (JSON):\n" + json.dumps(report, indent=2) + "\n\n"
        "Goals:\n"
        "- Ensure test runner detection works for TypeScript Node.js projects.\n"
        "- Ensure tools emit useful JSON results when requested.\n"
        "- Ensure timeouts and verbose logging work across tools.\n"
        "- Add or fix any missing imports or syntax errors.\n"
    )


def maybe_self_fix(root: Path, report: dict, profile: str | None, model: str | None, ask: bool, full_auto: bool) -> int:
    # Check for codex
    code, _, _ = run(["which", "codex"], cwd=root)
    if code != 0:
        print("Codex CLI not found; cannot self-fix automatically.")
        return 127
    prompt = build_fix_prompt(root, report)
    base = ["codex", "exec", "--cd", str(root)]
    if profile:
        base.extend(["--profile", profile])
    if model:
        base.extend(["--model", model])
    if ask:
        base.append("--ask-for-approval")
    if full_auto:
        base.append("--full-auto")
    base.append(prompt)
    rc, out, err = run(base, cwd=root)
    if out:
        print(out, end="")
    if err:
        print(err, end="")
    return rc


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Diagnose and optionally self-fix the Codex tools.")
    parser.add_argument("--self-fix", action="store_true", help="Attempt to repair tools using Codex CLI")
    parser.add_argument("--profile", default="gpt5", help="Codex CLI profile")
    parser.add_argument("-m", "--model", help="Model name for Codex CLI")
    parser.add_argument("-a", "--ask-for-approval", action="store_true", help="Codex CLI approval mode")
    parser.add_argument("--full-auto", action="store_true", help="Codex full-auto mode")
    parser.add_argument("--json", action="store_true", help="Emit JSON diagnostics report")
    args = parser.parse_args(argv)

    root = find_repo_root()

    report = {
        "py_compile": py_compile_all(root),
        "node_env": check_node_env(root),
        "tests_detect": check_tests_detect(root),
    }

    if args.json:
        print(json.dumps(report))
    else:
        print("Diagnostics:")
        print(json.dumps(report, indent=2))

    if args.self_fix:
        return maybe_self_fix(root, report, args.profile, args.model, args.ask_for_approval, args.full_auto)

    # Non-zero if any critical check failed
    ok = (
        report["py_compile"]["ok"]
        and report["node_env"]["node"]["ok"]
        and report["node_env"]["npm"]["ok"]
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

