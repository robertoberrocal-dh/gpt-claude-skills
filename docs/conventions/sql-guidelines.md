# SQL Guidelines

These guidelines apply to analytics-related skills that generate or validate BigQuery SQL.

## General Principles

- Use BigQuery Standard SQL only
- Prefer trusted curated tables over raw tables
- Minimize scanned data
- Avoid unnecessary joins
- Be explicit with assumptions
- Optimize for correctness first, efficiency second

## Query Construction Rules

### Table references
- Always use fully qualified table names
- Use backticks around fully qualified names

Example:

```sql
SELECT *
FROM `project.dataset.table`
```

### Aliases
- Use explicit aliases
- Keep aliases short and readable

### Column usage
- Never invent columns
- Only use columns validated from schema references or `INFORMATION_SCHEMA`
- Avoid `SELECT *` unless doing exploration or schema inspection

### Filtering
- Apply restrictive filters as early as possible
- Use partition or date filters whenever possible
- Use `LIMIT` for exploratory non-aggregated queries

### Aggregations
- Every non-aggregated selected column must appear in `GROUP BY`
- Use the correct aggregation function for the metric
- Use `HAVING` only for post-aggregation logic

### Dates and timestamps
- Be explicit about whether a field is `DATE`, `DATETIME`, or `TIMESTAMP`
- Be careful with local date vs UTC timestamp logic
- Prefer business-relevant date columns when available

### Joins
- Join as few tables as possible
- Verify join keys and types before joining
- Watch for one-to-many duplication risks
- Be careful with nested and repeated fields

## Performance Preferences

- Prefer aggregated tables when suitable
- Avoid large scans for simple KPI checks
- Use pre-aggregated or narrower tables when they answer the question reliably
- Prefer targeted diagnostics over broad exploratory queries on very large tables

## Quality Checks Before Execution

Before executing generated SQL, verify:
- tables are approved
- columns exist
- logic matches the user question
- filters are present
- output grain is correct
- duplication risks are understood
- cost is reasonable for the task

## Response Standards

Whenever a query is generated or executed, the response should make clear:
- what was queried
- which filters were used
- what metric was computed
- what assumptions were made
- any limitations or caveats