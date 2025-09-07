#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from _utils import (
    find_repo_root,
    detect_package_manager,
    detect_test_runner,
    detect_typescript,
    package_script_exists,
    run,
    run_package_script,
)


def run_all_tests(root: Path, watch: bool, timeout: float | None, idle_timeout: float | None) -> tuple[int, str, str]:
    # Try scripts first
    if package_script_exists(root, "test"):
        extra = ["--watch"] if watch else []
        code, out, err = run_package_script(root, "test", extra_args=extra if extra else None)
        return code, out, err

    # Try common runners
    runner = detect_test_runner(root) or "jest"
    if runner == "jest":
        args = ["npx", "jest"]
        if watch:
            args.append("--watch")
        return run(args, cwd=root, timeout_sec=timeout, idle_timeout_sec=idle_timeout)
    if runner == "vitest":
        args = ["npx", "vitest", "run"]
        if watch:
            args = ["npx", "vitest"]  # watch mode
        return run(args, cwd=root, timeout_sec=timeout, idle_timeout_sec=idle_timeout)
    if runner == "mocha":
        args = ["npx", "mocha"]
        # If TypeScript detected, try ts-node/register automatically
        if detect_typescript(root):
            args = ["npx", "mocha", "-r", "ts-node/register"]
        return run(args, cwd=root, timeout_sec=timeout, idle_timeout_sec=idle_timeout)
    if runner == "node-test-runner":
        args = ["node", "--test"]
        return run(args, cwd=root, timeout_sec=timeout, idle_timeout_sec=idle_timeout)
    return 127, "", f"No test script/runner detected. Please add an npm test script."


def run_category(root: Path, category: str, pattern: str | None, watch: bool, timeout: float | None, idle_timeout: float | None) -> tuple[int, str, str]:
    # Map to npm scripts like test:unit, test:integration, test:e2e
    script = f"test:{category}"
    extra = []
    if watch:
        extra.append("--watch")
    if pattern:
        extra.append(pattern)
    if package_script_exists(root, script):
        return run_package_script(root, script, extra_args=extra if extra else None)
    # Fallback to runner flags
    runner = detect_test_runner(root) or "jest"
    if runner == "jest":
        args = ["npx", "jest"]
        if watch:
            args.append("--watch")
        if pattern:
            args.extend(["-t", pattern])
        return run(args, cwd=root, timeout_sec=timeout, idle_timeout_sec=idle_timeout)
    if runner == "vitest":
        args = ["npx", "vitest", "run"]
        if watch:
            args = ["npx", "vitest"]
        if pattern:
            args.extend(["-t", pattern])
        return run(args, cwd=root, timeout_sec=timeout, idle_timeout_sec=idle_timeout)
    if runner == "mocha":
        args = ["npx", "mocha"]
        if pattern:
            args.extend(["--grep", pattern])
        return run(args, cwd=root, timeout_sec=timeout, idle_timeout_sec=idle_timeout)
    if runner == "node-test-runner":
        args = ["node", "--test"]
        return run(args, cwd=root, timeout_sec=timeout, idle_timeout_sec=idle_timeout)
    return 127, "", f"No suitable test command for category '{category}'."


def run_typecheck(root: Path, timeout: float | None) -> tuple[int, str, str]:
    if not detect_typescript(root):
        return 0, "", ""
    # Prefer package script if present
    if package_script_exists(root, "typecheck"):
        return run_package_script(root, "typecheck")
    # Fallback to tsc --noEmit
    args = ["npx", "tsc", "--noEmit"]
    return run(args, cwd=root, timeout_sec=timeout)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Run tests for the Node.js project (TypeScript-aware, with timeouts and JSON output).")
    parser.add_argument("--category", choices=["unit", "integration", "e2e"], help="Run a specific test category.")
    parser.add_argument("--pattern", help="Focus tests by name/pattern (mapped to runner flags).")
    parser.add_argument("--watch", action="store_true", help="Run in watch mode if supported.")
    parser.add_argument("--detect", action="store_true", help="Only detect and print runner and package manager.")
    parser.add_argument("--typecheck", dest="typecheck", action="store_true", help="Run TypeScript typecheck before tests if TS is detected.")
    parser.add_argument("--no-typecheck", dest="typecheck", action="store_false", help="Skip TypeScript typecheck even if TS is detected.")
    parser.set_defaults(typecheck=None)  # auto by default
    parser.add_argument("--timeout", type=float, help="Overall timeout (seconds) for the test process.")
    parser.add_argument("--idle-timeout", type=float, help="Idle (no output) timeout in seconds.")
    parser.add_argument("--json", action="store_true", help="Emit a single-line JSON object with results.")
    args = parser.parse_args(argv)

    root = find_repo_root()

    if args.detect:
        pm = detect_package_manager(root)
        runner = detect_test_runner(root) or "unknown"
        print(f"package_manager: {pm}")
        print(f"test_runner: {runner}")
        return 0

    # Auto decide typecheck: default True if TS detected and not explicitly disabled
    do_typecheck = detect_typescript(root) if args.typecheck is None else args.typecheck
    t_code = 0
    t_out = ""
    t_err = ""
    if do_typecheck:
        t_code, t_out, t_err = run_typecheck(root, args.timeout)
        if t_out:
            print(t_out, end="")
        if t_err:
            print(t_err, end="")
        if t_code != 0 and not args.json:
            # Return early on type errors if not JSON (JSON will include both)
            return t_code

    if args.category:
        code, out, err = run_category(root, args.category, args.pattern, args.watch, args.timeout, args.idle_timeout)
    else:
        code, out, err = run_all_tests(root, args.watch, args.timeout, args.idle_timeout)

    if args.json:
        payload = {
            "ok": code == 0,
            "code": code,
            "stdout": out,
            "stderr": err,
            "typecheck": {
                "ran": do_typecheck,
                "code": t_code,
                "stdout": t_out,
                "stderr": t_err,
            },
            "runner": detect_test_runner(root) or None,
            "package_manager": detect_package_manager(root),
            "timeout_sec": args.timeout,
            "idle_timeout_sec": args.idle_timeout,
        }
        print(json.dumps(payload))
        return code

    if out:
        print(out, end="")
    if err:
        print(err, end="")
    return code


if __name__ == "__main__":
    sys.exit(main())
