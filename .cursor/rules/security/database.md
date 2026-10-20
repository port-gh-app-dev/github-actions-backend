# Database Security Rules

## Principles

- Always use parameterized queries or prepared statements — never concatenate user input into SQL.
- Prefer ORMs or query builders that bind parameters by default.
- Apply least-privilege database credentials; never hardcode connection strings or passwords.
- Encrypt connections in transit (TLS) and encrypt sensitive data at rest when required.

## Query safety

- Use parameterized / prepared statement APIs for every dynamic value.
- Reject or escape identifiers only via allowlisted maps — never raw string concat for table/column names from input.
- Limit result sets; avoid unbounded queries driven by caller input.

## Credentials & secrets

- Store DB credentials in a secrets manager or environment variables — never hard-code secrets in code or config committed to git.
- Rotate credentials regularly; use short-lived tokens when available.

## Anti-patterns

- `query = "SELECT * FROM users WHERE id = " + userId`
- Committing connection strings with embedded passwords
- Shared admin credentials across environments
