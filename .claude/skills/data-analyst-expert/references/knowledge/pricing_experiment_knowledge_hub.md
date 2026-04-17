Pricing Experiment Knowledge Hub
Central Growth Pricing Team

Contents
Methodology
Best Practices
	Partition Pricing
	Clustering
Basket Value Deals
Small Basket Fee
Top Experiments by Month

Methodology

Measuring Pricing Performance based on AB tests
This process outlines the steps for measuring the cumulative incrementality driven by Pricing, using rolled out AB tests to extrapolate results
(2) Data Normalization and Comparability
Before calculating the impact, the raw data must be adjusted to ensure fair comparison between variants and experiments over time
Adjust Orders for User Exposure: Reduce randomization bias by normalizing the # of Variant Orders based on the actual number of users exposed to that Variant vs Control
Adjust Profit per Order: Make variants more comparable over time by adding the Delta between the Monthly Actuals during the experiment life and the Yearly Budget FLGPO
(1) Data Collection and Integration
This step involves joining data from multiple systems
Collect data by variant: Identify experiments ended in a given month, and isolate performance metrics for each variant
Data Joining: Consolidate data from multiple tables:
[Core Data] Orders
[CDP] Perseus Session Events
[DPS] Sessions Mapped to Orders & Test Orders
[MKT] BIMA Orders Profitability
(3) Core A/B Test Analysis
This is the central analytical step where the performance of the new pricing is compared against the control group.
Calculate Uplift vs Control: Determine the % or abs change (lift) in key metrics for each Variation vs Control
Check for PAS Compliance: Review the test results against the Pricing Action Standards (PAS) to ensure the experiment met all success criteria (e.g., statistical significance, min. ROI).
Normalize Experiment Duration: Adjust the experiment's financial and growth results to a standard 30-day range for consistent reporting and comparison across different tests.
(4) Extrapolation and Impact Estimation
The final step is to project the total business impact expected when rolling out the change, and sum the overall impact from implemented tests.
Scale up A/B test results: Extrapolate the observed uplift from the test sample (e.g., 20% of users) to the 100% of users population to estimate the full potential incremental impact
Estimate p.p. uplift relative to the market size: Calculate the projected increase in percentage points (p.p.) by factoring in the total size of the relevant market, using data from:
Monthly Analytical Profit from BIMA
Monthly Orders from Core Data

Calculations
Growth Combined = Est. Monthly Growth ÷ Market’s Vertical 30-day Orders
Growth Profit = Est. Monthly AP ÷ Market’s Vertical 30-day AP (min. 3% GMV)
Growth Orders = Est. Monthly Orders ÷ Market’s Vertical 30-day Orders

Est. Monthly Growth = Est. Monthly AP ÷ Target FLGPO1-year + Est. Monthly Orders
Est. Monthly AP = iAP ÷ Traffic Share ÷ Test Length × 30
Est. Monthly Orders = iOrders ÷ Traffic Share ÷ Test Length × 30

iAP = Adj APvar - Adj APctrl 
iOrders = Adj Ordersvar - Adj Ordersctrl 
iAPO = Adj APOvar - Adj APOctrl 

Adj APctrl = Adj APctrl × Adj Ordersctrl
Adj APvar = Adj APvar × Adj Ordersvar

Adj Ordersctrl = Ordersctrl
Adj Ordersvar = Ordersvar÷ Usersvar× Usersctrl

Adj APOctrl = APOctrl + Target FLGPO1-year- Market’s Vertical APOWeighted avg testing period
Adj APOvar = APOvar + Target FLGPO1-year- Market’s Vertical APOWeighted avg testing period
How the ranking works?
Experiments are ranked in desc. order by Growth Combined, estimating the full incrementality relative to the total country market size
Sources
BIMA Order Profitability
OneStream (within 5%-15% GMV for Food, 2.5%-15% QC)
DPS Test Orders
DPS Users CVR

Definitions
Operational data
AP = Analytical Profit
APO = AP per Order
Financial data
FLGP = Fully Loaded Gross Profit
FLGPO = FLGP per Order
If Growth Combined:
Then:
≥ 2%
Top Experiment
≥ 1%
Relevant Experiment 
≥ 0%
Good Experiment
< 0%
Ad-hoc Experiments

Create a copy of the calculator above here: https://docs.google.com/spreadsheets/d/1fnjFWMWJFMTihji5VHhsA_05QZWAvTqjzZD7ODBqftg/edit?gid=0#gid=0 
Plugging numbers to the previous formulae:
Adjusts for traffic split imbalances
Adjusts for long-term comparability
Scale impact assuming 100% rollout for 30 days
Adjusts for market size (in Profit and Orders)
Calc. add. Profit into add. Orders using Target FLGPO

Refresh on Pricing Action Standards:
¹ Those are defined by quarter, market, and  vertical. See values here.
² Deltas (e.g. iOrders) are indicated in absolute numbers - even if the delta is negative, a “positive” number is used in the trade-off calculations
See this file for more details: https://docs.google.com/presentation/d/1alIrPbMjsJjT8w_KO-FM-ggYTD67XwhElQUjKMnYMZ4/edit?slide=id.g35f7b99f0bb_0_0#slide=id.g35f7b99f0bb_0_0 
Scenario
Win-Win 🎰
CPiO 🚀
PPOL 🤑
Lose-Lose 💸
Situation
🔼iAPO 🔼iOrders
🔻iAPO 🔼iOrders
🔼iAPO 🔻iOrders
🔻iAPO 🔻iOrders
ROI
N/A
Adj APOctrl ÷ CPiO - 1
PPOL ÷ Adj APOctrl - 1
N/A
     ROI check
N/A
ROI >= Threshold¹
N/A
Trade-off²
N/A
Adj Ordersvar × iAPO ÷ iOrders
N/A
     Trade-off check
N/A
Trade-off <= Target FLGPO ÷ (1 + ROI)
Trade-off  >= Target FLGPO
N/A
Recoup ROI
N/A
N/A
Adj APOvar ÷ PPOL - 1
N/A
     Recoup ROI check
N/A
N/A
Recoup ROI <= Cap¹
N/A
     Statistical significance (positive uplift with p-value <= 0.05) on:
AP / User, Orders / User, or AP / Order
Orders / User
AP / Order
N/A
Plugging the numbers from the example in the previous slide:

By Month
Top Experiments

xxx
March 2026
Month
Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
xxxx

xxx
February 2026
Month
Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
xxxx

Few experiments with high growth impact in Jan- Service Fee introduction led to increased profitability in Cambodia 
January 2026
Month
Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
xxxx

Strategic fee adjustments on Top Chains and MOV thresholds defined the month's profitability.
December 2025
Month
Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
Profitability is not always about reducing friction; sometimes, it is about pricing the friction correctly. 
Experiments in Sweden proved that high demand can be less elastic than assumed: increasing the Delivery Fee for the top 4 short chains resulted in a massive "Win-Win," generating over +€106k without negative impact on orders.
Conversely, Argentina highlighted the substantial leverage of MOV adjustments: raising the thresholds for Dmarts did sacrifice volume but ultimately delivered the highest financial impact of the month, with a +€107k uplift.



Innovative approaches involving Saver, BVD, and aggressive DF changes - in addition to partition pricing - marked the month's results.
November 2025
Month
Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
True innovation often lies not in refining the known, but in dismantling the assumed: experiments in Nordics showed that SE/NO customers didn't value the existing Basket Value Deals so much; discontinuing those reductions increased profitability sharply in the impacted verticals.

Focusing on the basics led to big rewards in UY and LA
October 2025
Month
Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
Pricing partition drove most of the incrementality, but revisiting the basics with DF optimization in UY and MOV / SBF improvements in MD and LA also proved very impactful.

Value driven by Partitioning + Travel Time Fee optimization in EG & CY
September 2025
Month
Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
Partitioned Pricing continues to be a major driving force, but a thorough vendor reclustering and scheme merging exercise with new area-based clusters in Cairo and Cyprus also revealed the power of investing in continuous updates of the basic Travel Time Fee setups.


Service Fees and Prio Fees optimization drove most of the value in August
August 2025
Month
Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
The best performing tests either introduce SF, change it from flat to %, raise the %, or optimize SF caps. 
Tests introducing Priority Fees also produced strong results.

Find out more about the test results here: https://tableau.deliveryhero.net/#/site/GlobalStandardReporting/workbooks/36696/views 
Partitioning Prices drove most of the value in July
July 2025
Month
The best performing tests either introduce SF, change it from flat to %, raise the %, or optimize SF caps. 
They also used the added SF revenue to invest in DF reduction among selected areas, distances, or vendor clusters.

Examples of Best Practices
Partition Pricing

More details: https://docs.google.com/presentation/d/10Gpf2tyZHiwcjfy_yocDdqmTXxVH0sgjG7clumf3yeI/edit?slide=id.g381085232b0_0_157#slide=id.g381085232b0_0_157 
Scope
San Jose, Costa Rica, Food

Setup
Control: SF 5.5% (300-600)
Var1: -25% DF; SF 8.2% (300-1200); SBF (0-600)

Insight
By adding SBF the team could limit the increase of unprofitable orders where the lower basket and proportionally low SF would not be enough to offset the loss in DF

Next steps
💡To further optimize the individual setups of SF and SBF, additional tests are planned
In addition to SF, Small Basket Fee in CR was introduced to fund a lower DF

PedidosYa
Brand
CR_20250612_R_Z0_O_SanJoseFood_DF_SF_SOF
Identifier

Examples of Best Practices
Clustering

More details: https://docs.google.com/presentation/d/1AU7Isbi5JvdL1GZllJZkoJNZr1SXI9-3cjWAqCGIKcQ/edit?slide=id.g1116fe4ad88_0_0#slide=id.g1116fe4ad88_0_0 
Adjusting DF by Time generated +10% in FLGP with minimal order loss

Glovo
Brand
ES_20251215_Z_J0_R_BCN_Food_ToW
Identifier
Scope
Barcelona, Spain

Setup
Delivery Fees (DF) were adjusted based on Time of Day (Morning, Lunch, Afternoon, Dinner, Night) and Day of Week (Weekday vs. Weekend)
Winning Setup (Var A): +2pp fee increase during peaks (Lunch, Weekday Dinner, Night), -2pp fee decrease during valleys (Morning, Afternoon), and Weekend Dinner maintained at Control.

Insight
Elasticity in Orders is very symmetric
Significant spikes in orders and average order value (AOV) during lunch and dinner presented an opportunity to adjust DF to leverage customer willingness to pay (WTP)
Weekdays are in general more inelastic than weekends
Weekday dinners proved highly inelastic, experiencing an order increase despite the +2pp fee increase
Nights are very inelastic
Nights were found to be more elastic than expected, and lunch saw expected order drops

More details: https://docs.google.com/presentation/d/1HHYQcgT9YklkDLNTr6tBNECGaisuoyXK43Wzaz1qfgY/edit?slide=id.g307f7680c0e_0_52#slide=id.g307f7680c0e_0_52 
Scope
Cairo, Egypt

Setup
Schemes were simplified: Vendors were clustered based on historical orders (Low, Med and High GBV) and areas were clustered based on WTP levels (Low, High, Super High).

Insight
A more intentional clustering allowed EG to match different pricing elasticities, within vendor and locations groups, with tailored DF increases.

Next steps
Expand this vendor and area based clustering to other markets to further optimize DF and price sensitivity across TB.
Area-based DBDF recalibration allowed ~10% DF increase with min. order loss

Talabat
Brand
EG_20250822_R_B_P_DBDF_Revamp_Cairo_Q3
Identifier

More details: https://docs.google.com/presentation/d/1CkcQCns7AE_N9WMxMwOitb1K28-lWwteKX3sHPil7MA/edit?slide=id.g3becfb6ed41_1_0#slide=id.g3becfb6ed41_1_0 
Scope
Target vendors: Burger King, Subway, Bastard Burgers, Max Hamburgare (20% of OD)
City clustering: Stockholm vs other cities (grouped into short, mid, and long distance).

Setup
Avg DF increase: +10 SEK per distance bucket

Insight
- Low Elasticity: Most top-tier chains customers were willing to pay a premium to order from them, increasing DF revenue.

- The "Nudge" Effect: Remaining customers mostly shifted toward less-known (local) chains. These vendors typically pay higher commissions, which boosted overall profitability.

- Product Mix: As a result, adoption of "Saver" fees among Top Chains also increased.
Improving Profitability Through DF Optimization for Key Chains

Foodora
Brand
SE_20251107_R_B0_P_Increase-Short-Chains
Identifier
Impact & Results
iOrders
iProfit
PpOL
+1.1k
+€105k
win-win
KPI
ALL
Top Chains
Orders
+0.1%
-5.2%
⌀ DF
+5.0%
+20.5%
⌀ Prio
+1.0%
-2.5%
⌀ Comm.
+1.2%
+2.4%
⌀ GFV
+1.0%
+2.4%
⌀ Distance
+0.7%
+1.0%
⌀ Profit
+6.3%
+170%
Design

Examples of Best Practices
Basket Value Deals

More details: https://docs.google.com/presentation/d/1NFbbte7tOwtMWmP1SBHodVVX3m-kGnrWm4ztLoiqHYQ/edit?slide=id.g38823020466_0_647#slide=id.g38823020466_0_647 
Scope
Sweden, Shops

Setup
Var1: Removes all BVD
Var2: Retains Free Delivery tier

Insight
Customers showed low sensitivity to the removal of BVD. It highlights that a BVD scheme is not always necessary; in segments with high WTP having no discount in place at all yields significantly better economics without hurting volume.

Next steps
Reallocate the recovered margin to markets or verticals where price elasticity is higher and incentives are proven to drive incremental orders.
Removing Basket Value Based Discounts led up to +4% in FLGP at 0% Order loss

Foodora
Brand
SE_20250911_Z_G0_P_BVD_REMOVAL_V2
Identifier

Examples of Best Practices
Small Basket Fee



* For orders with Travel Time above 16 minutes
More details: https://docs.google.com/presentation/d/1NFbbte7tOwtMWmP1SBHodVVX3m-kGnrWm4ztLoiqHYQ/edit?slide=id.g38823020466_0_647#slide=id.g38823020466_0_647 
Scope
Vientiane, Laos | Food

Setup
To reduce negative margins among small basket orders, increased soft MOV from 20k to 25k/40k* with 5k SBF cap.

Insight
Finding the right Soft MOV, ideally with SBF cap,  can have a disproportionate impact on profitability by weeding out loss-making orders. Some of those orders are also replaced by higher Basket ones, further improving overall economics.

Next steps
Consider the introduction of Hard MOV as a guardrail against fraudulent orders.
Higher Soft MOV reduced loss-making orders, increased AFV/Commission + SBF

Foodpanda
Brand
LA_20250827_R_DM_P_VTE_MOVSBF
Identifier
Additional SBF revenue and less unprofitable orders improve total margins
Reduction in unprofitable orders
Higher soft MOV nudges customers towards larger baskets; SBF cap prevents affordability perception risk
Margin increase among small basket orders

Examples of Best Practices
Service Fee

More details: https://docs.google.com/presentation/d/1zsXMzzV0ZcBbf6RhvBHiwhbA8cUXMwxMEQD5Y_5ThHY/edit?slide=id.g371caf25b6d_0_38#slide=id.g371caf25b6d_0_38 
Scope
Vientiane, Laos, Food

Setup
SF: 3% BV
Control: ~3% AOV
Var1: ~5% AOV
Var2: No cap

Insight
Optimizing the SF cap after this remained for long time unchanged allowed avg SF to increase with limited order impact

Next steps
💡Var2 was tested with no cap, the results can be used to explore different potential caps for future experiments
Adjusting SF Max Cap in Laos led to major Profit uplift at little Order loss
Pandora
Brand
LA _20250626_R_H0_P_VTE_SFCap
Identifier




More details:
Scope
Lima, Peru | Food

Setup
Control: No SF
Variant 1: Service Fee of 3% [min of 0.7 PEN, cap of 2.4 PEN]; DF decrease of -1 PEN in each distance bucket

Insight
Competitive benchmarking showed competitors with 6% SF and more aggressive min/max caps. Reduced the DF by the average SF (1 PEN). Set the cap to prevent a high volume of orders where the SF > DF. Combined, this resulted in a much more competitive overall price than the competitor. 

Results were overall, successful with increase to order volume and frequency among non-subscribers, but lead to decrease in order frequency among subscribers.



Introducing a Service Fee …

PedidosYa
Brand
PE_20251204_R_H0_P_SF_Lima
Identifier



* For orders with Travel Time above 16 minutes
More details: https://docs.google.com/presentation/d/1NFbbte7tOwtMWmP1SBHodVVX3m-kGnrWm4ztLoiqHYQ/edit?slide=id.g38823020466_0_647#slide=id.g38823020466_0_647 
Scope
xxx

Setup
xxx

Insight
xxx

Next steps
xxx
Lower Soft MOV increased profitable orders, increased AFV/Commission + SBF

Glovo
Brand
MD_20250910_R_C0_O_Food_MBS_decrease
Identifier
Additional orders more than offset the reduction in SBF revenue
Increase in profitable orders
Leveraging SBF to protect margins, a lower soft MOV can unlock new (profitable) occasions
Margin decrease among small basket orders
Glovo FLGP data in Oct looks currently broken

Pricing Experiment 
Knowledge Hub


This Document is Maintained by the Central Growth Pricing Team
Reach out to laurent.broering@deliveryhero.com for questions and feedbacks

[TBC]
About the Strategy

More details: xxx
Scope
xxx

Setup
xxx

Insight
xxx

Next steps
xxx
xxx
xx
Brand
xx
Identifier
