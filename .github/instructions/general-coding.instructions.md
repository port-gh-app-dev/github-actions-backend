---
applyTo: "**"
---

# General coding instructions

## Security

- Follow OWASP-oriented secure coding: authentication checks, input validation, and injection prevention.
- Never hardcode secrets or credentials in source, workflows, or Terraform.
- Use parameterized queries or prepared statements for any database access.
- Validate and sanitize external input before use in shell, SQL, or cloud CLIs.
- Do not log tokens, passwords, or secret material.

## Quality

- Prefer small, reviewable changes with clear PR descriptions.
- Match existing style in YAML, HCL, and JSON templates.
- Fail closed on invalid input; surface actionable errors.
- Prefer least privilege for IAM policies and GitHub Actions permissions.
