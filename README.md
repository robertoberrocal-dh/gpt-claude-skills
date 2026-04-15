# gpt-claude-skills

Internal Claude skills repository for the Global Pricing Team.

This repository contains reusable Claude skills designed to support:
- analytics workflows in BigQuery
- pricing and experimentation questions
- business-oriented explanations for stakeholders
- future orchestration across Slack, Jira, Confluence, Gemini, and Google Workspace tools

## Current Skills

### 1. data-analyst-expert
A BigQuery-focused analytics skill that translates natural language questions into safe SQL, validates schema, executes queries when appropriate, and explains findings clearly.

### 2. dh-pricing-expert
A Delivery Hero pricing knowledge skill for business-oriented questions related to pricing concepts, KPIs, experimentation, and operational interpretation.

### 3. pricing-orchestrator
A routing skill that helps determine whether a user request should be handled as:
- business explanation
- analytical query
- a combined workflow

## Repository Structure

```text
docs/
  architecture/
  conventions/
  onboarding/

skills/
  data-analyst-expert/
  dh-pricing-expert/
  pricing-orchestrator/

tests/
  prompts/
  expected-behavior/
```

## Goals

- Standardize how Claude is used across the team
- Improve consistency in SQL generation and analytical reasoning
- Provide business-friendly and stakeholder-friendly explanations
- Build a foundation for future integrations with Slack, BigQuery, Jira, Confluence, Drive, Docs, and Gemini

## Working Principles

- Keep each skill focused and composable
- Prefer references for detailed documentation instead of bloating `SKILL.md`
- Use approved datasets and guardrails
- Test triggers and non-triggers explicitly
- Iterate based on real usage

## Status

This repository is currently in active development.

The first implementation priority is `data-analyst-expert`.