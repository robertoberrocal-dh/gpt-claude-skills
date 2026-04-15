# How to Install Skills

This document explains how to install and use the skills contained in this repository.

## Local Development

Clone the repository:

```bash
git clone <repo-url>
cd gpt-claude-skills
```

## Skill Structure

Each skill lives in its own folder under `skills/`.

Example:
- `skills/data-analyst-expert`
- `skills/dh-pricing-expert`
- `skills/pricing-orchestrator`

Each skill must contain:
- `SKILL.md`

It may also contain:
- `references/`
- `scripts/`

## Installing in Claude

Depending on the Claude surface being used, skills can typically be:
- uploaded as a skill folder or zip
- placed in the relevant Claude Code skills directory
- managed through internal workflows

## Recommended Development Flow

1. Update the skill files locally
2. Test prompts manually
3. Refine triggering and scope
4. Commit changes to Git
5. Share changes with the team
6. Promote stable versions for wider use

## Initial Testing Checklist

Before sharing a skill:
- verify `SKILL.md` exists
- verify frontmatter is valid
- confirm folder name matches skill name
- test obvious trigger prompts
- test paraphrased trigger prompts
- test non-trigger prompts
- review instructions for clarity and over-trigger risk

## Repository Priority

Initial implementation priority:
1. `data-analyst-expert`
2. `dh-pricing-expert`
3. `pricing-orchestrator`