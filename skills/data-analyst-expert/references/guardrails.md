# Guardrails

These guardrails apply specifically to the `data-analyst-expert` skill.

## Scope Guardrails

- Stay within approved datasets documented in `datasets.md`
- Prefer curated sources when they answer the question
- Use trusted team-managed pricing tables when they are the right source for the use case
- Do not imply unrestricted access beyond documented scope

## Table Choice Guardrails

- Use `pricing_performance_agg` by default for high-level daily or entity-level analysis
- Use `pricing_performance` only when granular detail is required
- Use `dps_test_orders` and `dps_experiment_setups` for experiment-focused questions when possible
- Use `dps_sessions_mapped_to_orders` for session/order traceability and lower-level DPS diagnostics
- Use `bima_order_profitability` when profitability logic is central

## Date and Freshness Guardrails

When using pricing performance tables:
- always filter with `partition_date_local`
- if the user does not specify a range, default to a recent sensible window
- remember that the table is typically reliable up to D-2
- be careful when the user asks for "yesterday" before the daily refresh is complete

## SQL Generation Guardrails

- Do not invent tables or columns
- Validate schema before final SQL generation
- Prefer fully qualified table names
- Avoid `SELECT *` unless exploring schema or sample data
- Use `LIMIT` for exploratory row-level queries
- Avoid unnecessary joins
- Be careful with `UNNEST` and repeated fields

## Aggregation Guardrails

- Never use `AVG()` directly to compute a daily average on `pricing_performance_agg`
- Use `SUM(metric) / COUNT(DISTINCT partition_date_local)` for daily averages over a period
- For rate-like metrics across segments or days, use weighted averages:
  - `SUM(numerator) / SUM(denominator)`

## Currency Guardrails

- Never aggregate `_local` monetary fields across multiple entities without currency grouping
- For cross-country analysis, prefer `_eur` fields
- Use `_local` only when the analysis clearly requires it

## User Counting Guardrails

- Use `COUNT(DISTINCT analytical_customer_id)` when counting users on `pricing_performance`
- Do not default to `customer_account_id`

## Baseline Pricing Analysis Guardrails

For baseline comparable pricing analysis, unless explicitly asked otherwise, consider excluding:
- campaign-assigned orders
- subscriber orders
- meal-for-one orders
- HVA orders

Do not apply these exclusions blindly when the user is analyzing those very features.

## Geography and Legal Guardrails

For Woowa Korea (`BM_KR`):
- do not use `vendor_longitude`
- do not use `vendor_latitude`
- do not use `delivery_longitude`
- do not use `delivery_latitude`

Use H3 indices instead when geospatial grouping is needed.

## Timeline Guardrails

Be careful with `dps_standard_fee_eur`:
- before 2024-09-08, it reflected only the standard travel-time fee component
- after 2024-09-08, it reflects the full standard fee

## Communication Guardrails

- Distinguish facts from interpretation
- Explain caveats rather than hiding them
- Say when a dataset is trusted but not curated
- Say when a metric definition may vary
- When confidence is low, say why