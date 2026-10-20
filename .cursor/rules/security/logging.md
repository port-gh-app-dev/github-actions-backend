# Logging Security Rules

## Principles

- Log enough to debug and audit; never log secrets, credentials, tokens, or passwords.
- Redact Authorization headers, connection strings, and API keys from logs and workflow outputs.
- Prefer structured logs with stable fields (action, resource id, outcome) over free-form dumps of full payloads.

## GitHub Actions

- Do not `echo` secret values or write them to `$GITHUB_STEP_SUMMARY`.
- Mask sensitive values with `::add-mask::` when they must appear transiently.
- Avoid printing full Terraform plans that may contain sensitive attributes in public logs when possible.

## Application & scripts

- Set log levels appropriately per environment; verbose debug must not expose credentials.
- When logging errors, omit request bodies that may contain authentication material or PII.

## Anti-patterns

- Logging `${{ secrets.* }}` values
- Dumping environment variables wholesale in CI
- Hardcoding a debug flag that prints secret material
