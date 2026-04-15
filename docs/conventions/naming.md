# Naming Conventions

## Repository

Repository name:
- `gpt-claude-skills`

Where `gpt` stands for Global Pricing Team.

## Skills

Skill folders must use kebab-case.

Examples:
- `data-analyst-expert`
- `dh-pricing-expert`
- `pricing-orchestrator`

Rules:
- lowercase only
- no spaces
- no underscores
- folder name should match the skill `name` in frontmatter

## Files

Required:
- `SKILL.md`

Optional support folders:
- `references/`
- `scripts/`
- `assets/`

Reference files should use descriptive snake_case or kebab-case consistently.  
For this repository, prefer `snake_case` for markdown reference files.

Examples:
- `business_metrics.md`
- `pricing_glossary.md`
- `stakeholder_templates.md`

## Branches

Recommended branch naming:
- `feature/<short-description>`
- `fix/<short-description>`
- `docs/<short-description>`

Examples:
- `feature/data-analyst-skill-v1`
- `docs/readme-update`
- `fix/sql-guardrails`

## Commit Messages

Recommended format:
- imperative mood
- concise but specific

Examples:
- `Initialize repository structure`
- `Add data-analyst-expert skill v1`
- `Refine BigQuery query guardrails`
- `Add pricing glossary references`