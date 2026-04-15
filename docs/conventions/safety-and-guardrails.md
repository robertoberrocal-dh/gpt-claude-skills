# Safety and Guardrails

## Scope Control

Skills must operate only within approved datasets, tables, and workflows.

If a request falls outside approved scope:
- say so clearly
- do not fabricate access
- do not imply unsupported actions can be executed

## SQL Safety

Unless explicitly requested and approved:
- do not generate destructive SQL
- do not execute mutation statements
- do not write `DELETE`, `UPDATE`, `INSERT`, `MERGE`, `CREATE OR REPLACE`, or `DROP`

Preferred default behavior:
- read-only analytics
- scoped queries
- controlled exploration

## Data Minimization

- retrieve only the data needed to answer the question
- avoid full-table scans when narrower filters are possible
- default to `LIMIT` for exploratory row-level queries

## Ambiguity Handling

When a user request is underspecified, do not guess silently.

Clarify missing items such as:
- timeframe
- metric definition
- target entity or geography
- comparison basis
- aggregation grain

## Interpretation Discipline

Separate:
- direct observations from data
- assumptions
- interpretation
- recommendations

Do not present assumptions as facts.

## Business Sensitivity

Pricing, experimentation, and operational metrics may be sensitive. Responses should be:
- professional
- precise
- non-speculative
- suitable for internal team usage

## Tool Discipline

If a tool is unavailable:
- acknowledge that limitation
- provide the best possible non-executed alternative
- avoid pretending the tool was used

## Evolution

Guardrails should be revised as the repository gains:
- more datasets
- more tools
- broader team usage
- external interfaces such as Slack