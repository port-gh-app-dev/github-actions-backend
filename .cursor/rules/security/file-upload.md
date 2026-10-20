# File Upload Security Rules

## Principles

- Validate file type, size, and content — do not trust client-supplied MIME types or extensions alone.
- Store uploads outside the web root or in object storage with non-executable permissions.
- Generate server-side filenames; never use raw user-supplied paths.
- Scan for malware when handling untrusted uploads in production paths.

## Validation

- Enforce allowlists for extensions and content types relevant to the feature.
- Cap maximum file size and reject empty or oversized payloads.
- Strip path traversal sequences (`../`, absolute paths) from any user-provided name.

## Secrets & credentials

- Do not accept uploads that embed secrets or credentials into the repository without review.
- Never hardcode cloud storage keys; use IAM roles or short-lived credentials.

## Anti-patterns

- Serving uploaded files from an executable directory
- Trusting `Content-Type` without content sniffing / magic-byte checks
- Writing user-controlled paths directly to the filesystem
