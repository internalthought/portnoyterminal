#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

from _utils import find_repo_root, run, run_ex


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Execute a subprocess with timeouts, verbose logs, and JSON output.")
    parser.add_argument("cmd", nargs=argparse.REMAINDER, help="Command to run after '--'. Example: tools/exec.py -- npx tsc -v")
    parser.add_argument("--timeout", type=float, help="Overall timeout (seconds)")
    parser.add_argument("--idle-timeout", type=float, help="Idle (no output) timeout (seconds)")
    parser.add_argument("--json", action="store_true", help="Emit JSON result")
    parser.add_argument("--dir", type=Path, help="Working directory")
    parser.add_argument("--verbose", action="store_true", help="Echo live subprocess output")
    args = parser.parse_args(argv)

    # Allow calling without '--'
    cmd = args.cmd
    if cmd and cmd[0] == "--":
        cmd = cmd[1:]
    if not cmd:
        print("Usage: tools/exec.py -- <command> [args...]", file=sys.stderr)
        return 2

    root = find_repo_root()
    code, out, err = run(
        cmd,
        cwd=args.dir or root,
        timeout_sec=args.timeout,
        idle_timeout_sec=args.idle_timeout,
        verbose=args.verbose,
    )

    if args.json:
        print(json.dumps({
            "ok": code == 0,
            "code": code,
            "stdout": out,
            "stderr": err,
            "cmd": cmd,
            "cwd": str(args.dir or root),
            "timeout_sec": args.timeout,
            "idle_timeout_sec": args.idle_timeout,
        }))
        return code

    if out:
        print(out, end="")
    if err:
        print(err, end="")
    return code


if __name__ == "__main__":
    sys.exit(main())

