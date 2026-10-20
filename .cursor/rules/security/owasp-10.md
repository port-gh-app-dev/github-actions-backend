# OWASP Top 10 Security Rules

Apply OWASP Top 10 thinking to workflows, Terraform, and any application code in this repository.

## A01 Broken Access Control

- Enforce authentication and authorization before privileged cloud or Port actions.
- Prefer least-privilege IAM and GitHub Actions `permissions`.

## A02 Cryptographic Failures

- Never hardcode secrets or credentials; use secret stores.
- Prefer TLS for all external calls; do not disable certificate verification.

## A03 Injection

- Defend against command injection, SQL injection, and template injection.
- Use parameterized queries / prepared statements for data stores.
- Validate and sanitize input before shell or query use.

## A04 Insecure Design

- Threat-model new workflows that mutate infrastructure or delete resources.
- Require confirmation / dry-run patterns for destructive operations when practical.

## A05 Security Misconfiguration

- Lock down default workflow permissions; avoid overly broad secrets access.
- Keep actions and Terraform providers updated (Dependabot / Renovate).

## A06 Vulnerable Components

- Pin action versions to full SHAs when possible; review Dependabot PRs.

## A07 Identification & Authentication Failures

- Use short-lived credentials; rotate and scope secrets.
- Do not hard-code authentication tokens in workflows or HCL.

## A08 Software & Data Integrity Failures

- Prefer verified publishers and checksummed artifacts.
- Protect default branch with required reviews.

## A09 Security Logging & Monitoring Failures

- Log security-relevant events without logging secrets.
- Surface workflow failures clearly for operators.

## A10 Server-Side Request Forgery (SSRF)

- Allowlist outbound hosts when workflows fetch remote URLs from input.
