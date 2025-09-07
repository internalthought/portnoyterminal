#!/usr/bin/env python3
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from threading import Thread
from queue import Queue, Empty


def timestamp() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def _parse_bool_env(name: str, default: bool = False) -> bool:
    val = os.getenv(name)
    if val is None:
        return default
    val = val.strip().lower()
    return val in ("1", "true", "yes", "on")


def find_repo_root(start: Path | None = None) -> Path:
    """Ascend from start to locate repo root by .git or package.json; fallback to cwd."""
    if start is None:
        start = Path.cwd()
    cur = start.resolve()
    for parent in [cur] + list(cur.parents):
        if (parent / ".git").exists() or (parent / "package.json").exists():
            return parent
    return cur


def ensure_codex_dir(root: Path) -> Path:
    codex = root / ".codex"
    codex.mkdir(exist_ok=True)
    return codex


def _log_dir(root: Path) -> Path:
    base = ensure_codex_dir(root) / "logs"
    base.mkdir(parents=True, exist_ok=True)
    return base


def _jsonl_write(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def _reader_thread(stream, q: Queue, tag: str):
    try:
        for line in iter(stream.readline, ""):
            q.put((tag, line))
    finally:
        try:
            stream.close()
        except Exception:
            pass


def run(
    cmd: list[str],
    cwd: Path | None = None,
    *,
    timeout_sec: float | None = None,
    idle_timeout_sec: float | None = None,
    verbose: bool | None = None,
    env: dict | None = None,
) -> tuple[int, str, str]:
    """Run a subprocess with logging, optional timeouts, and captured output.

    Backward-compatible return: (code, stdout, stderr).
    Environment configuration (defaults if args not provided):
    - CODEX_VERBOSE: enable live echo and command banners.
    - CODEX_CMD_TIMEOUT_SEC: overall timeout (seconds).
    - CODEX_IDLE_TIMEOUT_SEC: no-output idle timeout (seconds).
    - CODEX_LOG_DIR: custom log directory; defaults to .codex/logs.
    """
    root = find_repo_root(cwd)
    log_dir = Path(os.getenv("CODEX_LOG_DIR") or _log_dir(root))
    tools_log = log_dir / "tools.log"
    started = time.time()
    verbose = _parse_bool_env("CODEX_VERBOSE", False) if verbose is None else verbose
    if timeout_sec is None:
        t_env = os.getenv("CODEX_CMD_TIMEOUT_SEC")
        timeout_sec = float(t_env) if t_env else None
    if idle_timeout_sec is None:
        it_env = os.getenv("CODEX_IDLE_TIMEOUT_SEC")
        idle_timeout_sec = float(it_env) if it_env else None

    banner = {
        "event": "proc_start",
        "ts": timestamp(),
        "cmd": cmd,
        "cwd": str(cwd or Path.cwd()),
        "timeout_sec": timeout_sec,
        "idle_timeout_sec": idle_timeout_sec,
    }
    _jsonl_write(tools_log, banner)
    if verbose:
        print(f"[tools.run] $ {' '.join(cmd)} (cwd={banner['cwd']})", file=sys.stderr)

    try:
        proc = subprocess.Popen(
            cmd,
            cwd=str(cwd) if cwd else None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True,
            env={**os.environ, **(env or {})},
        )
    except FileNotFoundError as e:
        err = f"Executable not found: {cmd[0]}\n{e}"
        _jsonl_write(tools_log, {
            "event": "proc_error",
            "ts": timestamp(),
            "cmd": cmd,
            "cwd": str(cwd or Path.cwd()),
            "error": err,
        })
        if verbose:
            print(f"[tools.run] {err}", file=sys.stderr)
        return 127, "", err

    q: Queue = Queue()
    t_out = Thread(target=_reader_thread, args=(proc.stdout, q, "stdout"), daemon=True)
    t_err = Thread(target=_reader_thread, args=(proc.stderr, q, "stderr"), daemon=True)
    t_out.start(); t_err.start()

    out_parts: list[str] = []
    err_parts: list[str] = []
    last_output = time.time()
    timed_out = False
    idle_timed_out = False

    while True:
        if proc.poll() is not None:
            # Drain remaining lines
            try:
                while True:
                    tag, line = q.get_nowait()
                    if tag == "stdout":
                        out_parts.append(line)
                    else:
                        err_parts.append(line)
                    last_output = time.time()
                    if verbose:
                        stream = sys.stdout if tag == "stdout" else sys.stderr
                        print(line, end="", file=stream)
            except Empty:
                pass
            break
        # Read any available lines without blocking too long
        try:
            tag, line = q.get(timeout=0.05)
            if tag == "stdout":
                out_parts.append(line)
            else:
                err_parts.append(line)
            last_output = time.time()
            if verbose:
                stream = sys.stdout if tag == "stdout" else sys.stderr
                print(line, end="", file=stream)
        except Empty:
            pass

        now = time.time()
        if timeout_sec is not None and (now - started) > timeout_sec:
            timed_out = True
            try:
                proc.kill()
            except Exception:
                pass
            break
        if idle_timeout_sec is not None and (now - last_output) > idle_timeout_sec:
            idle_timed_out = True
            try:
                proc.kill()
            except Exception:
                pass
            break

    t_out.join(timeout=1)
    t_err.join(timeout=1)

    code = proc.returncode if not (timed_out or idle_timed_out) else 124
    out = "".join(out_parts)
    err = "".join(err_parts)
    duration = time.time() - started

    hang_info = None
    if timed_out or idle_timed_out:
        hang_info = {
            "type": "timeout" if timed_out else "idle_timeout",
            "duration_sec": duration,
            "last_output_age_sec": time.time() - last_output,
            "stdout_tail": out[-2000:],
            "stderr_tail": err[-2000:],
        }
        hang_path = log_dir / f"hang_{int(started)}.json"
        _jsonl_write(hang_path, {
            "cmd": cmd,
            "cwd": str(cwd or Path.cwd()),
            "started": timestamp(),
            "timeout_sec": timeout_sec,
            "idle_timeout_sec": idle_timeout_sec,
            **hang_info,
        })
        if verbose:
            print(f"[tools.run] timeout: details saved to {hang_path}", file=sys.stderr)

    _jsonl_write(tools_log, {
        "event": "proc_end",
        "ts": timestamp(),
        "cmd": cmd,
        "cwd": str(cwd or Path.cwd()),
        "code": code,
        "duration_sec": duration,
        "timed_out": timed_out,
        "idle_timed_out": idle_timed_out,
    })

    return code, out, err


def run_ex(
    cmd: list[str],
    cwd: Path | None = None,
    *,
    timeout_sec: float | None = None,
    idle_timeout_sec: float | None = None,
    verbose: bool | None = None,
    env: dict | None = None,
) -> dict:
    """Extended runner returning a structured dict for JSON outputs."""
    code, out, err = run(
        cmd,
        cwd=cwd,
        timeout_sec=timeout_sec,
        idle_timeout_sec=idle_timeout_sec,
        verbose=verbose,
        env=env,
    )
    return {
        "cmd": cmd,
        "cwd": str(cwd or Path.cwd()),
        "code": code,
        "stdout": out,
        "stderr": err,
    }


def read_json(path: Path, default):
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        return default


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def detect_package_manager(root: Path) -> str:
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    return "npm"


def read_package_json(root: Path) -> dict:
    return read_json(root / "package.json", {})


def detect_test_runner(root: Path) -> str | None:
    pkg = read_package_json(root)
    scripts = (pkg.get("scripts") or {})
    script_str = " ".join(scripts.values()).lower()
    # Prefer explicit config
    if "jest" in script_str:
        return "jest"
    if "vitest" in script_str:
        return "vitest"
    if "mocha" in script_str:
        return "mocha"
    if re.search(r"node\s+--test", script_str):
        return "node-test-runner"
    # Heuristics based on devDeps
    dev_deps = (pkg.get("devDependencies") or {}) | (pkg.get("dependencies") or {})
    for k in dev_deps.keys():
        kl = k.lower()
        if kl == "jest" or kl.startswith("@jest/"):
            return "jest"
        if kl == "vitest":
            return "vitest"
        if kl == "mocha":
            return "mocha"
    return None


def detect_typescript(root: Path) -> bool:
    if (root / "tsconfig.json").exists():
        return True
    pkg = read_package_json(root)
    deps = (pkg.get("devDependencies") or {}) | (pkg.get("dependencies") or {})
    return "typescript" in {k.lower() for k in deps.keys()}


def package_script_exists(root: Path, name: str) -> bool:
    pkg = read_package_json(root)
    scripts = (pkg.get("scripts") or {})
    return name in scripts


def run_package_script(root: Path, script: str, extra_args: list[str] | None = None) -> tuple[int, str, str]:
    mgr = detect_package_manager(root)
    cmd = []
    if mgr == "pnpm":
        cmd = ["pnpm", "run", script]
    elif mgr == "yarn":
        # yarn v1 supports `yarn <script>`; v2+ uses `yarn run <script>`
        cmd = ["yarn", script]
    else:
        cmd = ["npm", "run", script]
    if extra_args:
        cmd.extend(["--", *extra_args])
    return run(cmd, cwd=root)


def safe_append_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(content)


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def write_file(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8")


def upsert_memories_section(text: str, entry: str) -> str:
    """Insert or append an entry under a '## Memories' section in AGENTS.md content."""
    if not text.strip():
        return f"## Memories\n\n- {entry}\n"
    lines = text.splitlines()
    out = []
    i = 0
    inserted = False
    while i < len(lines):
        out.append(lines[i])
        if lines[i].strip().lower() == "## memories":
            # Append after this header and any immediate blank lines
            i += 1
            while i < len(lines) and lines[i].strip() == "":
                out.append(lines[i])
                i += 1
            out.append(f"- {entry}")
            inserted = True
            # Copy the rest as-is
            while i < len(lines):
                out.append(lines[i])
                i += 1
            break
        i += 1
    if not inserted:
        # Add a new section at the end
        if out and out[-1].strip() != "":
            out.append("")
        out.append("## Memories")
        out.append("")
        out.append(f"- {entry}")
    return "\n".join(out) + "\n"


def extract_memories(text: str) -> list[str]:
    """Extract bullet lines under the first '## Memories' section."""
    lines = text.splitlines()
    in_mem = False
    items: list[str] = []
    for line in lines:
        if line.strip().lower() == "## memories":
            in_mem = True
            continue
        if in_mem:
            if re.match(r"^## ", line):
                break
            m = re.match(r"^\s*[-*]\s+(.*)$", line)
            if m:
                items.append(m.group(1).strip())
    return items
