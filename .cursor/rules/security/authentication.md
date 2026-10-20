# Authentication Security Rules

## Principles

- Never hardcode secrets, API keys, tokens, or credentials in source, workflows, or Terraform.
- Load credentials from environment variables, GitHub Actions secrets, or a secrets manager.
- Prefer short-lived credentials (OIDC, temporary STS tokens) over long-lived access keys.
- Scope credentials to the minimum permissions required (least privilege).

## GitHub Actions

- Reference secrets via `${{ secrets.NAME }}`; never echo or print secret values.
- Do not pass credentials through untrusted workflow inputs without validation.
- Prefer `permissions:` blocks with least privilege on workflows and jobs.
- For cloud providers, prefer OIDC federation over static keys when available.

## Authentication checks

- Validate caller identity before performing privileged cloud or Port operations.
- Reject missing, expired, or malformed authentication material early.
- Do not implement custom crypto; use vetted libraries and platform auth.

## Anti-patterns

- Hard-coded passwords, tokens, or AWS keys in YAML, HCL, or scripts
- Committing `.env` files that contain real credentials
- Logging Authorization headers or secret values
