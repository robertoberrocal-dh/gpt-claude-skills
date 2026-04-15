# Schema Reference

This file is the starting schema reference for `data-analyst-expert`.

## Current Status

This is currently a lightweight placeholder.  
It should be expanded with:
- important datasets
- key tables
- frequent join paths
- important date columns
- common duplication risks
- notes on nested and repeated fields

## Suggested Documentation Pattern

For each important table, document:
- full table name
- business purpose
- key columns
- date or partition fields
- common join keys
- common filters
- caveats

## Example Template

### `project.dataset.table_name`

**Purpose**  
Short description of what the table is used for.

**Important columns**
- `column_a`: meaning
- `column_b`: meaning
- `column_c`: meaning

**Date fields**
- `created_date`
- `partition_date`

**Common joins**
- joins to `project.dataset.other_table` on `entity_id`
- joins to `project.dataset.third_table` on `order_id`

**Caveats**
- possible duplicates after unnest
- null-heavy fields
- delayed freshness
- historical logic changes

## Initial Priority Tables To Document

Suggested early candidates:
- experiment assignment tables
- orders-related curated tables
- vendor and entity reference tables
- pricing team derived tables
- DPS-related operational tables used frequently by the team