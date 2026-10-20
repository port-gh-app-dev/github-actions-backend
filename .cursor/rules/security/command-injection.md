# Command Injection Security Rules

## Principles

- Treat all external input as untrusted: workflow inputs, PR titles, issue bodies, entity properties, and environment variables from callers.
- Prefer structured APIs and libraries over shelling out to the OS.
- If a shell command is required, pass arguments as an array/list — never interpolate untrusted strings into a shell command line.

## GitHub Actions & scripts

- Avoid `eval`, `bash -c` with concatenated user input, and unquoted expansions.
- Sanitize and validate workflow `inputs.*` before using them in `run:` steps.
- Prefer GitHub Actions expressions and official actions over ad-hoc shell when possible.
- Escape or reject characters that alter shell semantics (`;`, `|`, `$()`, backticks, newlines).

## Terraform & cloud CLIs

- Do not build CLI invocations by concatenating untrusted names or tags.
- Validate resource names against a strict allowlist pattern (alphanumeric, hyphen, underscore).

## Anti-patterns

- `run: echo ${{ github.event.issue.title }} | bash`
- Embedding unvalidated Port/entity fields into `aws`, `az`, or `terraform` command strings
