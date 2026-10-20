# Input Validation Security Rules

## Principles

- Validate and sanitize all external input at trust boundaries (workflow inputs, API payloads, CLI args, Port entity properties).
- Prefer allowlists over denylists for formats, enums, and resource identifiers.
- Fail closed: reject invalid input early with clear errors; do not process partially validated data.

## What to validate

- Types, lengths, ranges, and required fields
- Resource names, ARNs, regions, and IDs against known patterns
- URLs and webhook targets against allowlisted hosts when applicable
- Boolean and enum workflow inputs before branching on them

## Injection & authentication context

- Input validation complements (does not replace) authentication, parameterized queries, and command-injection defenses.
- Never use unvalidated input in shell commands, SQL, or Terraform variable interpolation that affects privileged operations.

## Secrets

- Do not log raw input that may contain secrets or credentials.
- Never hardcode default "test" credentials that could be used in production paths.

## Anti-patterns

- Passing workflow inputs straight into cloud CLIs without pattern checks
- Relying only on frontend or caller-side validation
