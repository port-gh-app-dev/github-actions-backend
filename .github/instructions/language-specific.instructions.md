---
applyTo: "**/*.{yml,yaml,tf,hcl,json,js,ts,py,go}"
---

# Language-specific instructions

## GitHub Actions (YAML)

- Pin third-party actions to full commit SHAs when practical.
- Declare explicit `permissions:` with least privilege.
- Validate `inputs` (authentication-related and otherwise) before interpolation into `run:` steps to prevent command injection.
- Never echo secrets or credentials; reference `${{ secrets.* }}` only.

## Terraform (HCL)

- Do not hardcode secrets; use variables and environment/`TF_VAR_*` injection.
- Prefer data sources and remote state backends appropriate for the environment.
- Tag resources consistently; avoid overly permissive security groups by default.

## JavaScript / TypeScript

- Validate and sanitize input at API boundaries.
- Prefer parameterized queries / prepared statements for SQL; never concatenate user input.
- Avoid `child_process` with shell string concatenation.

## Python

- Use parameterized queries (e.g. DB-API placeholders) or prepared statements — never f-string SQL.
- Avoid `shell=True` with untrusted input.
- Load credentials from environment variables, not hard-coded literals.

## Go

- Use database/sql with placeholders (parameterized queries); never fmt.Sprintf for SQL values.
- Validate authentication tokens with vetted libraries.
- Context-cancel long-running cloud API calls.
