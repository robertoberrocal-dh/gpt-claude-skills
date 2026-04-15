# Business Metrics

This document defines key business terms, metric interpretations, and field preferences commonly used by the Global Pricing Team.

## Core Identifiers

### GEID / Country / Market
Use:
- `global_entity_id`

Unless explicitly instructed otherwise, prefer `global_entity_id` over country code.

### Brand / Entity / Platform
Use:
- `brand_name`

### Users / Customers / ACID
Use:
- `analytical_customer_id`

For user counting, prefer:
- `COUNT(DISTINCT analytical_customer_id)`

Do not default to `customer_account_id`.

## Core Value Metrics

### GBV / Food Value / GPV / GFV / Basket Value
Default field:
- `basket_value_paid_eur`

If the question is explicitly gross of incentives or nominal:
- `basket_value_nominal_eur`

### Actual Delivery Fee
Default field:
- `delivery_fee_eur`

### Baseline or Strikethrough Fee
Default field:
- `dps_standard_fee_eur`

Important timeline caveat:
- prior to 2024-09-08, `dps_standard_fee_eur` represented only the standard travel-time fee component
- after 2024-09-08, it represents the full standard fee

### MOV / SBF
Typical fields:
- `minimum_order_value_eur`
- `small_basket_fee_eur`

## Profitability and Unit Economics

### Profit / FLGP / Fully Loaded Gross Profit / Margin / Contribution Margin / CM
Default field:
- `analytical_profit`

### P&L fields
For strict unit economics and platform profit:
- prefer `_net`
- prefer `_net_eur`

Use gross paid fields only when the user is asking about customer out-of-pocket payment rather than strict platform economics.

## Customer Fees

Customer fees usually refer to customer-facing charges composed of:
- delivery fee
- service fee
- small basket fee
- priority fee
- payment method fee
- long distance fee
- bad weather fee
- any applicable pricing-related delivery fee components

Unless the user explicitly wants component decomposition:
- prefer pre-calculated total customer fee fields
- avoid manually summing fee components

## Pricing Scope Flags

### HVA
`is_hva` indicates a High Value Action.  
An order can only be HVA if `is_marketing = TRUE`.

### Meal for One
`is_meal_for_one` is a specific feature that allows users to order below standard MOV constraints with low-fee logic.

Do not treat Meal for One orders as normal MOV compliance anomalies.

### Subscriber
Subscription-related orders may affect fee comparability.

### DPS Campaign Assignment
Campaign-assigned orders may distort baseline pricing analysis.

## Baseline Pricing Analysis Scope

For baseline pricing analysis, unless explicitly asked otherwise, it is often appropriate to exclude:
- campaign-assigned orders
- subscriber orders
- meal-for-one orders
- HVA orders

This is not a universal rule.  
Use it only when the goal is comparable baseline pricing analysis.

## Currency Rules

### Cross-country analysis
Default to `_eur` fields.

### Local-currency analysis
Use `_local` fields only when:
- the analysis is within one currency context
- grouping by `currency_iso_code`
- the user explicitly wants local price point behavior

Never aggregate `_local` values across multiple entities without proper currency grouping.

## Verticals

### Vertical Parent
Use:
- `vertical_parent`

Typical high-level buckets include:
- Dmarts
- Food
- Local Shops

Important note:
coffee-related vendors may appear under different vertical logic depending on business mapping and market-specific exceptions.

## Additional Terms

### DPS
Dynamic pricing system that determines fees such as delivery fee, small basket fee, and surge-related pricing.

### BIMA
Marketing and financial profitability source with strict net-of-tax revenue and cost logic.

### VV
Willingness-to-pay style logic derived from customer survey inputs and mapped against current pricing and basket behavior.

### CIT Stream
Financial ledger logic handling deduplication and funding-source splits for vouchers and discounts.

### Pandora
Internal platform naming used for brands such as Foodora, Foodpanda, and Yemeksepeti.