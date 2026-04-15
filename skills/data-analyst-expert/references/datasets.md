# Approved Datasets

This document defines the approved initial scope for `data-analyst-expert`.

## Scope Philosophy

This skill works best when datasets are selected by use case rather than by generic project-wide access.

The main dataset families are:
1. pricing performance and macro KPI analysis
2. DPS tracing and experiment diagnostics
3. profitability validation

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

## Selection Rules

- Prefer `pricing_performance_agg` for high-level KPI analysis
- Use `pricing_performance` only when granular fields are required
- Prefer `dps_test_orders` and `dps_experiment_setups` for experiment-focused questions
- Prefer `dps_sessions_mapped_to_orders` for lower-level DPS and session/order tracing
- Prefer `bima_order_profitability` when profitability logic or subsidy attribution is central

## Important Caveat

Not all approved tables have the same level of standardization.

Practical hierarchy:
- curated shared sources: generally preferred when they answer the question
- trusted team-managed pricing sources: valid and important, but validate grain and metric interpretation carefully