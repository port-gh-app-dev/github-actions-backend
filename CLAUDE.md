# CLAUDE.md

Guidance for Claude Code and other AI assistants working in this repository.

## Project overview

GitHub Actions backend for cloud operations (AWS, Azure) plus Terraform for provisioning an EC2 instance. Workflows may integrate with Port via `port_context` and Port API credentials.

## Security requirements

- Apply security best practices aligned with OWASP: strong authentication posture, input validation, and protection against command injection.
- Never hardcode secrets, API keys, or credentials; use GitHub Actions secrets and environment variables.
- If touching data stores, use parameterized queries / prepared statements — never concatenate untrusted input into SQL.
- Validate workflow inputs before interpolating them into shell `run:` steps.
- Do not print or commit secret values.

## How to work

- Read existing workflows under `.github/workflows/` before adding or changing automation.
- Preserve `workflow_dispatch` inputs and Port integration patterns unless asked to change them.
- Keep Terraform in the repository root consistent with `main.tf`, `variables.tf`, and `outputs.tf`.
- Update the README when adding required secrets or new workflows.
