# Approved Datasets

This document defines the approved initial scope for `data-analyst-expert`.

## Scope Philosophy

This skill works best when datasets are selected by use case rather than by generic project-wide access.

The main dataset families are:
1. pricing performance and macro KPI analysis
2. DPS tracing and experiment diagnostics
3. profitability validation
4. pricing experiment pipeline (action standards)

## Dataset Family A: Pricing Performance and Macro KPI Analysis

### `dh-imd.growth_pricing.pricing_performance`
Purpose:
- granular pricing and performance analysis
- customer-level counting using `analytical_customer_id`
- detailed pricing feature diagnostics
- granular assignment or low-level behavioral analysis

Notes:
- trusted and important for team workflows
- not a curated shared layer
- validate grain carefully before joining or aggregating
- prefer when aggregate data is insufficient

### `dh-imd.growth_pricing.pricing_performance_agg`
Purpose:
- fast macro KPI analysis
- daily entity-level performance
- high-level fee, order, and profitability trends
- lighter and more efficient than the base table

Notes:
- preferred default for macro and daily analysis
- multi-dimensional aggregate table
- do not treat each row as a daily total without understanding segment splits
- use `partition_date_local` filtering

## Dataset Family B: DPS Tracing and Experiment Diagnostics

### `fulfillment-dwh-production.curated_data_shared.dps_test_orders`
Purpose:
- experiment order-level analysis
- control vs variant diagnostics
- test result validation
- safer experiment-level analysis than blindly unnesting repeated structures in other tables

Notes:
- curated and preferred when analyzing DPS experiments
- useful for test metadata and variant logic

### `fulfillment-dwh-production.curated_data_shared.dps_experiment_setups`
Purpose:
- experiment configuration and setup logic
- identifying test setup parameters
- validating test metadata

Notes:
- curated source
- use when the question is about setup, rollout, or experiment structure

### `fulfillment-dwh-production.cl.dps_sessions_mapped_to_orders`
Purpose:
- session-to-order mapping
- DPS diagnostics
- travel time and pricing behavior tied to orders
- operational tracing for dynamic pricing logic

Notes:
- important for lower-level DPS analysis
- validate grain and duplication risk carefully

## Dataset Family C: Profitability Validation

### `fulfillment-dwh-production.curated_data_shared_mkt.bima_order_profitability`
Purpose:
- profitability analysis
- subsidy and funding-source logic
- stricter P&L validation
- finance-leaning profitability views

Notes:
- curated source
- preferred when profitability logic needs a more trusted curated basis

## Dataset Family D: Pricing Experiment Pipeline (Action Standards)

This family covers the pipeline created and maintained by the Global Pricing Team
`pricing_action_standards` scheduled query
It produces daily statistical readouts for all active pricing experiments.

Pipeline flow:
```
test_user_assignment  ──┐
                        ├──► test_pnl ──► daily_order_profitability ──► test_confidence ──► pricing_action_standards
BIMA order data    ─────┘                                                                    (+ DPS experiment metadata)
```

### `dh-imd.growth_pricing.test_user_assignment`
Purpose:
- user-to-variant assignment registry for all pricing experiments
- ground truth for experiment randomization
- used to attribute orders to the correct experiment arm when building P&L views

Notes:
- grain: one row per user per experiment (`entity_id`, `test_id`, `test_user_id`, `variant`)
- partitioned by `last_updated`, clustered by `entity_id`, `test_id`
- very large table (~2.4B rows); always filter by `entity_id` and `test_id`
- use `last_updated` for partitioning — not an event date
- covers 54 entities, 554 distinct tests, from 2023-08-07 to present

### `dh-imd.growth_pricing.test_pnl`
Purpose:
- daily P&L aggregated by experiment variant, vertical, and channel
- detailed revenue and cost breakdown (same schema as `bima_order_profitability`) for each test arm
- used to understand what drove profit changes within an experiment (waterfall analysis per variant)

Notes:
- grain: `global_entity_id` × `test_name` × `test_variant` × `vertical` × `channel` × `order_date`
- partitioned by `order_date`, clustered by `global_entity_id`, `test_name`, `test_variant`, `vertical`
- includes `is_in_treatment` flag (TRUE = variant arm, FALSE = control arm)
- all revenue and cost fields match `bima_order_profitability` schema (delivery_fee_net, commission_fee_net, analytical_profit, etc.)
- also includes `od_orders`, `priority_orders`, `saver_orders` for order type breakdown
- covers 66 entities, 4,941 distinct test names, from 2023-01-01 to present (~4.8M rows)

### `dh-imd.growth_pricing.daily_order_profitability`
Purpose:
- daily FLGP-per-order (local currency) aggregated by experiment and variant
- includes statistical correction multipliers (`order_multiplier`, `profit_multiplier`) for CUPED or variance reduction
- intermediate input to the statistical computation that produces `test_confidence`

Notes:
- grain: `data_source` × `entity_id` × `test_id` × `variant` × `order_date`
- partitioned by `order_date`, clustered by `data_source`, `entity_id`, `test_id`, `variant`
- `data_source` takes values `DPS-Central` or `BIMA-Regional` — do not aggregate across sources
- `flgpo_local` is FLGP per order in local currency (not EUR); compare within one entity
- `_before_correction` fields preserve the raw pre-CUPED values for auditability
- covers 70 entities, 575 tests, from 2023-03-01 to present (~1.1M rows)

### `dh-imd.growth_pricing.test_confidence`
Purpose:
- daily statistical test results (p-values, means, confidence intervals) for all pricing experiments
- intermediate table between `daily_order_profitability` and `pricing_action_standards`
- use when you need raw stats without the full experiment metadata enrichment

Notes:
- grain: `entity_id` × `test_id` × `base` × `variation` × `updated_date`
- partitioned by `updated_date`, clustered by `entity_id`, `test_name`, `base`, `variation`
- same statistical field structure as `pricing_action_standards` (opu, cvr, flgpu, flgpo, profit_user, profit_order, volume)
- does NOT include experiment metadata (no hypothesis, objective, launched_by, test flags, etc.)
- covers 69 entities, 547 tests, from 2024-06-12 to present (~26K rows — one snapshot per day per test)

### `dh-imd.growth_pricing.pricing_action_standards`
Purpose:
- final enriched output of the experiment pipeline; primary table for experiment readout and action decisions
- combines statistical results from `test_confidence` with full experiment metadata from DPS setups
- used for: monitoring active experiments, ranking experiments by impact, generating readouts

Notes:
- grain: `entity_id` × `test_id` × `base` × `variation` × `updated_date` × `data_source`
- partitioned by `updated_date`, clustered by `entity_id`, `test_id`, `base`, `variation`
- each test appears multiple rows per snapshot: one per `data_source` (DPS-Central, BIMA-Regional) and one per `base`/`variation` pair
- always filter to the latest `updated_date` snapshot when reading current state
- `profit_order_source` and `profit_user_source` indicate whether the profit signal comes from DPS or BIMA
- BM_KR profit values are in local currency (KRW), not EUR — do not compare directly with other entities
- covers 69 entities, 559 tests, from 2024-06-12 to present (~355K rows)
- preferred over `test_confidence` for any analysis requiring experiment metadata (type, flags, objective, launched_by)

## Selection Rules

- Prefer `pricing_performance_agg` for high-level KPI analysis
- Use `pricing_performance` only when granular fields are required
- Prefer `dps_test_orders` and `dps_experiment_setups` for experiment-focused questions
- Prefer `dps_sessions_mapped_to_orders` for lower-level DPS and session/order tracing
- Prefer `bima_order_profitability` when profitability logic or subsidy attribution is central
- Prefer `pricing_action_standards` for experiment readouts, statistical results, and action decisions
- Use `test_pnl` when a P&L waterfall breakdown by experiment variant is needed
- Use `test_confidence` when only raw statistical results are needed without metadata
- Use `daily_order_profitability` when tracking experiment metric trends day-by-day within a test
- Use `test_user_assignment` when attributing orders or users to a specific experiment arm

## Important Caveat

Not all approved tables have the same level of standardization.

Practical hierarchy:
- curated shared sources: generally preferred when they answer the question
- trusted team-managed pricing sources: valid and important, but validate grain and metric interpretation carefully