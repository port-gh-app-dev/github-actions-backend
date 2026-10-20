# Agent Instructions

This repository provides GitHub Actions workflows for AWS/Azure cloud operations and Terraform for EC2 provisioning. Use these rules when editing workflows, Terraform, or related config.

## Security (required)

- Follow OWASP-oriented practices: authentication, input validation, and injection defenses apply to workflow inputs and any scripts.
- Never hardcode secrets or credentials in YAML, HCL, or docs examples that look like real values.
- Prefer parameterized queries or prepared statements anywhere SQL or query APIs appear; never string-concatenate untrusted input into queries.
- Validate and sanitize all external input (workflow `inputs`, entity context, issue/PR text) before using it in shell commands or cloud CLIs.
- Do not log secrets, tokens, or credentials.

## Coding standards

- Prefer least-privilege IAM and GitHub Actions `permissions` blocks.
- Keep workflow names and inputs clear; document required repository secrets in the README.
- Match existing YAML and Terraform style in the repo.
- Destructive operations (delete, terminate, purge) should be explicit and carefully gated.

## Scope

- Primary languages/configs: GitHub Actions YAML, Terraform HCL, JSON templates under `.github/templates/`.
- Do not invent cloud credentials; reference secrets by name only.
