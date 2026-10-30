#!/usr/bin/env python3
"""Find enrolled repositories with code changes since their last documented commit,
and dispatch the wiki backend in update mode for each one.

Environment:
  GH_TOKEN      token that can read the enrolled repositories and run workflows
                in BACKEND_REPO (the sync token)
  BACKEND_REPO  owner/name of this repository
  DRY_RUN       "true" to report what would be dispatched without dispatching
"""
import base64
import json
import os
import subprocess
import sys

import yaml

BACKEND_REPO = os.environ["BACKEND_REPO"]
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
BACKEND_WORKFLOW = "wiki-backend.yaml"
MARKER_PATH = "docs/wiki/.last-synced"


def gh(*args, check=True):
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout).strip())
    return result


def api_text(path, jq):
    return gh("api", path, "--jq", jq).stdout.strip()


def active_backend_titles():
    """Run titles of backend runs that are queued or in progress."""
    titles = set()
    for status in ("queued", "in_progress"):
        out = gh(
            "run", "list", "--repo", BACKEND_REPO, "--workflow", BACKEND_WORKFLOW,
            "--status", status, "--limit", "100", "--json", "displayTitle",
        ).stdout
        titles.update(run["displayTitle"] for run in json.loads(out))
    return titles


def decide(name, active_titles):
    branch = api_text(f"repos/{name}", ".default_branch")
    head = api_text(f"repos/{name}/commits/{branch}", ".sha")

    marker = gh(
        "api", f"repos/{name}/contents/{MARKER_PATH}?ref={branch}",
        "--jq", ".content", check=False,
    )
    if marker.returncode != 0:
        if "Not Found" in marker.stderr:
            return "skip: no wiki yet. Run Generate wiki (full) in Port first."
        raise RuntimeError(marker.stderr.strip())
    last = base64.b64decode(marker.stdout).decode().strip()

    if last == head:
        return "skip: up to date"

    open_prs = json.loads(gh(
        "pr", "list", "--repo", name, "--label", "docs:wiki",
        "--state", "open", "--json", "number",
    ).stdout)
    if open_prs:
        return f"skip: wiki PR #{open_prs[0]['number']} is still open"

    if f"Wiki update: {name}" in active_titles:
        return "skip: a refresh for this repository is already running"

    files = json.loads(api_text(
        f"repos/{name}/compare/{last}...{head}", "[.files[]?.filename]",
    ) or "[]")
    code_files = [f for f in files if not f.startswith("docs/wiki/") and not f.endswith(".md")]
    span = f"{last[:7]}..{head[:7]}"

    if not code_files:
        return f"skip: docs-only changes ({span})"
    if DRY_RUN:
        return f"would dispatch {span} ({len(code_files)} code files)"

    gh(
        "workflow", "run", BACKEND_WORKFLOW, "--repo", BACKEND_REPO,
        "-f", f"repository={name}",
        "-f", "mode=update",
        "-f", f"commit_range={last}..{head}",
    )
    return f"dispatched {span} ({len(code_files)} code files)"


def main():
    with open("repos.yaml") as f:
        repos = yaml.safe_load(f)["repos"]

    active = active_backend_titles()
    rows, failures = [], 0
    for entry in repos:
        name = entry["name"]
        try:
            outcome = decide(name, active)
        except Exception as exc:  # keep going, report at the end
            outcome = f"error: {exc}"
            failures += 1
        print(f"{name}: {outcome}")
        rows.append(f"| {name} | {outcome} |")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write("| Repository | Outcome |\n|---|---|\n" + "\n".join(rows) + "\n")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
