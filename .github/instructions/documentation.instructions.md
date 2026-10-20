---
applyTo: "**/*.md"
---

# Documentation instructions

- Keep the README accurate for workflows, required secrets, and Terraform usage.
- Document new `workflow_dispatch` inputs and repository secrets when adding workflows.
- Prefer clear tables and short procedures over long prose.
- Do not document real secret values or credentials — use placeholders only.
- Link to workflow files under `.github/workflows/` for exact behavior.
- When describing security-sensitive operations (delete, terminate, purge), call out impact and required permissions.
