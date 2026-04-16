# SQL Patterns

This document captures common SQL approaches for `data-analyst-expert`.

## 1. Macro KPI Trend Using `pricing_performance_agg`

Use when the user asks for:
- daily trend
- entity-level macro KPI
- country or market summary
- high-level fee, order, or profit movement

Pattern:
- use `pricing_performance_agg`
- filter with `partition_date_local`
- aggregate to the actual desired grain
- do not use row-level `AVG()` as a substitute for daily averages

Example logic:

```sql
SELECT
  global_entity_id,
  SUM(orders) AS orders,
  SUM(delivery_fee_eur) / SUM(orders) AS avg_delivery_fee_eur
FROM `dh-imd.growth_pricing.pricing_performance_agg` AS agg
WHERE partition_date_local BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 8 DAY)
  AND DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
  AND global_entity_id = 'PY_AR'
GROUP BY 1
```

## 2. Daily Average Over a Period

Use when the user asks for:
- average daily orders
- average daily GMV
- average daily fee collections

Correct pattern:
- `SUM(metric) / COUNT(DISTINCT partition_date_local)`

Do not use:
- `AVG(metric)` over aggregated segment rows

Example logic:

```sql
SELECT
  SUM(orders) / COUNT(DISTINCT partition_date_local) AS avg_daily_orders
FROM `dh-imd.growth_pricing.pricing_performance_agg` AS agg
WHERE partition_date_local BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 14 DAY)
  AND DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
  AND global_entity_id = 'FP_TH'
```

## 3. Weighted Average Fee or Rate

Use when the user asks for:
- average delivery fee
- profit per order
- average customer fee
- any rate across segments or dates

Correct pattern:
- `SUM(numerator) / SUM(denominator)`

Example logic:

```sql
SELECT
  SUM(delivery_fee_eur) / SUM(orders) AS weighted_avg_delivery_fee_eur
FROM `dh-imd.growth_pricing.pricing_performance_agg` AS agg
WHERE partition_date_local BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 8 DAY)
  AND DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
  AND global_entity_id = 'PY_AR'
```

## 4. User Counting With Granular Table

Use when the user asks for:
- MTUs
- WAUs
- unique users
- customer reach

Pattern:
- use `pricing_performance`
- count `DISTINCT analytical_customer_id`

Example logic:

```sql
SELECT
  COUNT(DISTINCT analytical_customer_id) AS users
FROM `dh-imd.growth_pricing.pricing_performance` AS pp
WHERE partition_date_local BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  AND DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
  AND global_entity_id = 'PY_AR'
```

## 5. Baseline Pricing Analysis

Use when the goal is to evaluate core pricing behavior without non-pricing features distorting the result.

Typical baseline exclusions:
- `has_dps_campaign_assignment`
- `is_subscriber`
- `is_meal_for_one`
- `is_hva`

Apply only when appropriate.

Example logic:

```sql
SELECT
  SUM(orders) AS orders,
  SUM(delivery_fee_eur) / SUM(orders) AS avg_delivery_fee_eur
FROM `dh-imd.growth_pricing.pricing_performance_agg` AS agg
WHERE partition_date_local BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 8 DAY)
  AND DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
  AND global_entity_id = 'PY_AR'
  AND IFNULL(has_dps_campaign_assignment, FALSE) = FALSE
  AND IFNULL(is_subscriber, FALSE) = FALSE
  AND IFNULL(is_meal_for_one, FALSE) = FALSE
  AND IFNULL(is_hva, FALSE) = FALSE
```

## 6. Experiment Analysis With Curated Test Orders

Use when the user asks for:
- control vs variant analysis
- DPS test result validation
- experiment-level order outcomes

Preferred approach:
- use `dps_test_orders`
- validate variant names and test metadata
- be careful with metric definitions and exposure logic

## 7. DPS Setup Validation

Use when the user asks for:
- experiment setup
- configuration logic
- test metadata
- rollout structure

Preferred approach:
- inspect `dps_experiment_setups`
- confirm relevant identifiers and setup fields first

## 8. Session-to-Order Diagnostics

Use when the user asks for:
- mapping pricing sessions to resulting orders
- travel-time-related pricing behavior
- lower-level DPS operational tracing

Preferred approach:
- use `dps_sessions_mapped_to_orders`
- validate grain
- check duplication and join assumptions carefully

## 9. Profitability Validation

Use when the user asks for:
- funding source
- subsidy splits
- stricter profitability
- finance-aligned P&L views

Preferred approach:
- use `bima_order_profitability`
- prefer net fields for strict economics

## 10. Metadata Inspection Pattern

Use when schema details are unclear.

Useful metadata queries include:

```sql
SELECT
  column_name,
  data_type,
  is_nullable
FROM `project.dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'target_table'
ORDER BY ordinal_position
```

```sql
SELECT
  table_name,
  option_name,
  option_value
FROM `project.dataset.INFORMATION_SCHEMA.TABLE_OPTIONS`
WHERE table_name = 'target_table'
```

```sql
SELECT
  column_name,
  description
FROM `project.dataset.INFORMATION_SCHEMA.COLUMN_FIELD_PATHS`
WHERE table_name = 'target_table'
```

Use metadata inspection before making assumptions about:
- available fields
- grain
- partitioning
- nested paths
- descriptions