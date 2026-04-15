# Schema Reference

This file is the working schema reference for `data-analyst-expert`.

## Purpose

This reference helps the skill choose the right table family and avoid incorrect assumptions about:
- column names
- table grain
- date fields
- join keys
- metric definitions
- duplication risks

This is a living document.  
It should be refined over time using:
- table metadata from BigQuery
- column descriptions
- verified queries
- team knowledge and usage patterns

## How To Use This Reference

For each table, the skill should use this file for:
1. business purpose
2. likely grain
3. preferred use cases
4. known caveats
5. fields that must be confirmed via metadata before querying

The skill must still validate schema when needed using:
- `INFORMATION_SCHEMA.COLUMNS`
- `INFORMATION_SCHEMA.TABLES`
- `INFORMATION_SCHEMA.TABLE_OPTIONS`
- `INFORMATION_SCHEMA.COLUMN_FIELD_PATHS`

## Metadata Inspection Queries

Use these queries when schema details must be confirmed.

### 1. Get columns and data types

```sql
SELECT
  column_name,
  data_type,
  is_nullable,
  ordinal_position
FROM `project.dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'target_table'
ORDER BY ordinal_position
```

### 2. Get table options and description

```sql
SELECT
  table_name,
  option_name,
  option_value
FROM `project.dataset.INFORMATION_SCHEMA.TABLE_OPTIONS`
WHERE table_name = 'target_table'
ORDER BY option_name
```

### 3. Get nested field paths and descriptions

```sql
SELECT
  column_name,
  field_path,
  data_type,
  description
FROM `project.dataset.INFORMATION_SCHEMA.COLUMN_FIELD_PATHS`
WHERE table_name = 'target_table'
ORDER BY field_path
```

### 4. Check partitioning and clustering from table metadata

```sql
SELECT
  table_name,
  ddl
FROM `project.dataset.INFORMATION_SCHEMA.TABLES`
WHERE table_name = 'target_table'
```

### 5. Inspect latest available dates

```sql
SELECT
  MIN(partition_date_local) AS min_partition_date_local,
  MAX(partition_date_local) AS max_partition_date_local
FROM `project.dataset.target_table`
```

Replace `partition_date_local` with the relevant date field if needed.

### 6. Lightweight grain inspection

```sql
SELECT
  COUNT(*) AS row_count,
  COUNT(DISTINCT partition_date_local) AS distinct_days,
  COUNT(DISTINCT global_entity_id) AS distinct_entities
FROM `project.dataset.target_table`
WHERE partition_date_local BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 8 DAY)
  AND DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
```

Adjust field names based on actual schema.

## Table Family A: Pricing Performance and Macro KPI Analysis

---

## `dh-imd.growth_pricing.pricing_performance`

**Purpose**  
Granular pricing and performance table used for low-level analysis of pricing behavior, users, assignments, and detailed operational diagnostics.

**Preferred use cases**
- unique user counting
- low-level pricing diagnostics
- detailed fee behavior
- assignment-level or order-level pricing analysis
- cases where aggregate tables do not contain the required field

**Likely grain**
- likely more granular than `pricing_performance_agg`
- validate whether the grain is order-level, assignment-level, or another analytical event grain before use

**Known / expected important fields**
These are strongly suggested by current team knowledge and should still be confirmed through metadata:
- `partition_date_local`
- `global_entity_id`
- `brand_name`
- `analytical_customer_id`
- `is_successful`
- `vertical_parent`
- `basket_value_paid_eur`
- `basket_value_nominal_eur`
- `delivery_fee_eur`
- `dps_standard_fee_eur`
- `minimum_order_value_eur`
- `small_basket_fee_eur`
- `analytical_profit`
- `currency_iso_code`
- `has_dps_campaign_assignment`
- `is_subscriber`
- `is_meal_for_one`
- `is_hva`

**Date fields to confirm**
- `partition_date_local`
- any event timestamp or local datetime fields used for lower-level analysis

**Likely join keys or filtering keys**
- `global_entity_id`
- `analytical_customer_id`
- possibly order-level identifiers if present
- possibly experiment or assignment identifiers if present

**Important caveats**
- always validate grain before aggregation
- use `is_successful = TRUE` for order / GMV / revenue aggregation unless the analysis explicitly requires failed or cancelled orders
- use `COUNT(DISTINCT analytical_customer_id)` for user counting
- avoid blindly averaging pre-aggregated-looking values
- watch currency context: use `_eur` fields for cross-country analysis
- treat `_local` fields carefully and only within proper currency scope
- confirm whether the table includes multiple rows per order due to dimension splits or assignment logic

**Validation priority**
Before using this table, confirm:
1. grain
2. date field
3. success flag behavior
4. available user identifier
5. whether assignment-related fields create duplication risk

---

## `dh-imd.growth_pricing.pricing_performance_agg`

**Purpose**  
Primary aggregate table for fast, high-level pricing and performance analysis.

**Preferred use cases**
- daily KPI trends
- entity-level or market-level summaries
- fee and basket trends
- macro profitability views
- fast exploratory summaries

**Likely grain**
- multi-dimensional aggregate grain
- not a pure daily-total table
- each day may contain multiple rows split across analytical dimensions

**Known / expected important fields**
These are strongly suggested by current team knowledge and should still be confirmed through metadata:
- `partition_date_local`
- `global_entity_id`
- `brand_name`
- `vertical_parent`
- `orders`
- `basket_value_paid_eur`
- `basket_value_nominal_eur`
- `delivery_fee_eur`
- `dps_standard_fee_eur`
- `minimum_order_value_eur`
- `small_basket_fee_eur`
- `analytical_profit`
- `currency_iso_code`
- `has_dps_campaign_assignment`
- `is_subscriber`
- `is_meal_for_one`
- `is_hva`

**Date fields to confirm**
- `partition_date_local`

**Likely grouping dimensions**
Confirm via metadata and profiling, but current team knowledge suggests dimensions may include:
- `global_entity_id`
- `vertical_parent`
- `is_subscriber`
- channel or comparable segmentation fields

**Important caveats**
- preferred default table for high-level KPI analysis
- always filter using `partition_date_local`
- `orders` already represents successful orders
- do not use `AVG()` directly to compute average daily metrics over a period
- use `SUM(metric) / COUNT(DISTINCT partition_date_local)` for daily averages
- use weighted averages such as `SUM(delivery_fee_eur) / SUM(orders)` for rate-like metrics
- never assume one row equals one daily total
- validate segment splits before interpreting totals

**Validation priority**
Before using this table, confirm:
1. actual dimensional grain
2. available KPI columns
3. which segmentation flags exist
4. whether fee fields are gross or net
5. whether metric definitions match the question

---

## `fulfillment-dwh-production.curated_data_shared_mkt.bima_order_profitability`

**Purpose**  
Curated profitability table used for finance-leaning profitability analysis, subsidy logic, and stricter net-of-tax revenue and cost views.

**Preferred use cases**
- profitability validation
- subsidy and funding-source analysis
- strict P&L cuts
- marketing / finance-aligned profitability views

**Likely grain**
- likely order-level or order-derived profitability grain
- confirm before aggregating

**Known / expected important concepts**
Fields should be confirmed through metadata, but likely themes include:
- order identifiers
- `global_entity_id`
- profitability and cost lines
- funding-source splits
- revenue and subsidy components
- tax-stripped net metrics

**Date fields to confirm**
- order date
- accounting date
- partition field if applicable

**Likely join keys or filters**
- order-level identifier
- `global_entity_id`
- date field

**Important caveats**
- prefer this table when the question is explicitly about profitability truth, funding source, or strict P&L logic
- do not assume field names from `pricing_performance`
- confirm whether values are already net-of-tax
- confirm whether cancelled / failed orders are included and how that affects interpretation

**Validation priority**
Before using this table, confirm:
1. grain
2. date field
3. order identifier
4. profitability field definitions
5. funding-source fields and their logic

## Table Family B: DPS Tracing and Experiment Diagnostics

---

## `fulfillment-dwh-production.curated_data_shared.dps_test_orders`

**Purpose**  
Curated table for DPS experiment order-level analysis, including test metadata and variant logic.

**Preferred use cases**
- control vs variant analysis
- test result validation
- experiment-level order outcomes
- safer experiment analysis than blindly unnesting experiment arrays elsewhere

**Likely grain**
- likely order-level with experiment metadata
- confirm whether one order can appear multiple times for multiple tests

**Known / expected important concepts**
Based on team usage, likely relevant fields include:
- order identifiers
- created date / local date
- `entity_id`
- test identifiers
- `test_name`
- `test_variant`
- sent / successful flags
- profitability fields such as `marketing_fully_loaded_gross_profit_eur`

Confirm exact names via metadata.

**Date fields to confirm**
- created date
- local order date
- partition field if present

**Likely join keys**
- order identifier
- `entity_id`
- test identifier

**Important caveats**
- validate whether each row is unique per order or per order-test combination
- do not assume profitability fields align perfectly with other profitability sources
- confirm whether the table already solves experiment duplication that would otherwise happen with repeated experiment fields in other tables

**Validation priority**
Before using this table, confirm:
1. grain
2. date field
3. order identifier
4. variant field
5. test identifier fields

---

## `fulfillment-dwh-production.curated_data_shared.dps_experiment_setups`

**Purpose**  
Curated table for DPS experiment setup logic and configuration.

**Preferred use cases**
- experiment setup inspection
- test metadata lookup
- setup validation
- rollout structure and configuration debugging

**Likely grain**
- likely test-setup-level grain
- may include multiple rows per setup depending on configuration structure

**Known / expected important concepts**
Likely relevant:
- setup identifiers
- entity or market identifiers
- test name or experiment name
- setup status or rollout metadata
- configuration details related to fee logic or targeting

Confirm exact names via metadata.

**Date fields to confirm**
- setup creation date
- active start / end date
- partition field if present

**Likely join keys**
- experiment or setup identifier
- `entity_id` or comparable market field

**Important caveats**
- configuration tables often contain nested or structured fields
- confirm which fields are human-readable versus configuration payloads
- use this table for setup understanding, not necessarily for final business KPI measurement

**Validation priority**
Before using this table, confirm:
1. grain
2. setup identifiers
3. market/entity fields
4. active date fields
5. nested configuration structure

---

## `fulfillment-dwh-production.cl.dps_sessions_mapped_to_orders`

**Purpose**  
Operational table linking DPS sessions to resulting orders for lower-level pricing diagnostics and dynamic pricing tracing.

**Preferred use cases**
- session-to-order mapping
- travel-time-driven pricing analysis
- operational diagnostics
- fee logic tracing tied to sessions and orders
- deeper DPS investigations

**Likely grain**
- likely session-to-order or order-session mapping grain
- confirm whether there can be multiple sessions per order or multiple rows per order due to experiment or fee components

**Known / expected important concepts**
From team usage, likely relevant fields include:
- order identifiers
- `entity_id`
- `created_date`
- sent / own-delivery flags
- `vertical_type`
- travel-time-related fields
- basket-value-related fields
- minimum-order-value-related fields
- small-basket-fee-related fields
- customer fee and vendor fee components
- cost and incentive components
- experiment exposure arrays or related fields

Confirm exact names via metadata.

**Date fields to confirm**
- `created_date`
- any local date fields
- partition field if present

**Likely join keys**
- order identifier
- `entity_id`

**Important caveats**
- validate duplication risk carefully, especially if experiments or repeated structures are present
- do not unnest repeated experiment fields without understanding duplication impact
- useful for deep diagnostics, but often heavier and more complex than curated test-order tables
- confirm whether filters such as `is_sent`, `is_own_delivery`, and `vertical_type` are needed for consistent business logic

**Validation priority**
Before using this table, confirm:
1. grain
2. order identifier
3. date field
4. experiment-related repeated fields
5. fee and cost component naming

## Cross-Table Notes

## Preferred source by use case

### High-level pricing KPI trend
Prefer:
- `dh-imd.growth_pricing.pricing_performance_agg`

### Unique user counting
Prefer:
- `dh-imd.growth_pricing.pricing_performance`

### Strict profitability and subsidy logic
Prefer:
- `fulfillment-dwh-production.curated_data_shared_mkt.bima_order_profitability`

### Control vs variant experiment analysis
Prefer:
- `fulfillment-dwh-production.curated_data_shared.dps_test_orders`

### Setup and rollout inspection
Prefer:
- `fulfillment-dwh-production.curated_data_shared.dps_experiment_setups`

### Low-level DPS tracing
Prefer:
- `fulfillment-dwh-production.cl.dps_sessions_mapped_to_orders`

## Known business rules that are not discoverable from metadata alone

These must be preserved in skill logic, not inferred from metadata:
- prefer `pricing_performance_agg` for macro analysis
- use `partition_date_local` for pricing performance filtering
- pricing performance data is generally reliable up to D-2 after refresh
- use `_eur` fields for cross-country analysis
- use `COUNT(DISTINCT analytical_customer_id)` for user counting
- avoid `AVG()` for daily averages on aggregate tables
- use weighted averages for rate-like metrics
- baseline pricing analysis may exclude campaign, subscriber, meal-for-one, and HVA orders when appropriate
- do not use Woowa coordinates for `BM_KR`
- `dps_standard_fee_eur` changes meaning before vs after 2024-09-08

## Next Recommended Expansion

The next version of this file should add confirmed field-level sections for:
1. `pricing_performance_agg`
2. `pricing_performance`
3. `dps_test_orders`
4. `dps_experiment_setups`
5. `dps_sessions_mapped_to_orders`
6. `bima_order_profitability`

For each one, add:
- exact field names
- business descriptions
- grain confirmation
- join examples
- sample validated query patterns