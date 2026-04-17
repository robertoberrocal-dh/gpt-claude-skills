1. Experimentation based Pricing @ DH

What is the goal of pricing? 
Orders?
Revenue?
Avg. DF?
GMV?
Market share?
Total Profit
The goal of Pricing is to maximise long term gross profit (i.e., CLTV) via: 
Capturing user’s willingness to pay 
Nudging users towards the most desired behaviour (shorter distances, bigger baskets, free delivery for HVAs)
Driving a fair and competitive price perception

How we drive towards that objective
2. Optimization
Are our pricing setups optimized across our pricing dimensions. Given our objective:
Are the fee levels and distributions optimized
Are we using the best mechanic to capture fees (e.g., flat, percent, caps)


Data & Analytics infrastructure (Order level profitability data, Eppo, Power Analysis, Significance Pipeline)
Experimentation infrastructure (DPS & Fun with Flags)
North Star: maximizing CLTV (FLGP)
1. Segmentation
Do we have the right segmentation dimensions / components to differentiate our fees on to best capture customer WtP, and address cost to serve
E.g., time conditions, weather conditions, area-based fees, basket based fees, etc.


2a. Opportunity identification & prioritization
Where do we think we can capture more value, aligned to local market objectives, and how (i.e., design)
2b. Experimentation
How do we set up the test to properly evaluate our hypothesis, balancing speed and accuracy


2c. Implementation
How do we make the most efficient decisions (Pricing Action Standards)


3. Communication & UX
How do we communicate our pricing structure to users to maximize understanding & acceptance of fees, and nudge towards better behaviors

Focus of today’s discussion

How we drive towards that objective
Running experiments
Making decisions efficiently
Communicating to customers
Deciding what to test
Running accurate tests
Enabling infrastructure (e.g., DPS)
Pricing Action Standards (PAS)
UX / UI Best practices
Experimenting on pricing interventions (i.e., mechanisms, levels), based on signals to identify pockets of value
Benchmarking (internal KPIs / external practices, e.g., competitor prices)
Research / surveys on customer affordability needs (e.g., VW tests, NPS, etc.)
Methodology for how to take decisions on pricing experiments with an objective, ROI-based, and long-term view


Ensuring the front-end experience clearly communicates the value of our pricing offering to the customer
Focus of today’s discussion


1
2
3

Develop test hypotheses and specify aim of the test. 
Including identifying test location, participating vendors and test MDE. 
A/B testing process with Pricing Action Standards
Create hypothesis
Running a power analysis to help inform how long the test will need to run for to have enough data to make conclusions* 

*in addition, tests should run for long enough for order deltas to stabilize
Run Power analysis
Test is launched under the assumption that it will run for as long as is necessary based on the power analysis in the previous step. 
Launch test
After recommended amount of time has passed analysts check results to understand if significance of orders and profit has been reached. 
Check significance
Evaluate the test results against PAS framework
Calculation of PPOL/CPiO and comparison to the target profit, if conditions are not met test is seen as a failure. 
Check vs Target
Profit (ROI)
Check to see if and how likely it would be for the profit gained could be reinvested to regain lost orders. 
Check Recoup ROI
Verification of the likelihood that orders will shift further turning the results negative. 

Acceptable order difference
If a test has passed all checks then the local team is free to implement. Otherwise the team dives deeper into data to gain new learnings for the next iteration and creates new hypotheses - return to Step 1. 
Next steps
1
2
3
4
5
6
7
8
Experimenting
Evaluating

2. Pricing action standards (PAS) framework

Potential challenges when running pricing experiments
Pricing investments are not comparable. KPIs in pricing tests are often not apples-to-apples with other growth investments, preventing efficient capital allocation
Tests don’t capture the full impact of a change. Pricing changes are “permanent” and have lasting impact on the customer, while pricing tests are run for relatively shorter periods of time
Decision making is difficult to scale. Entities run hundreds of pricing tests per year, and most tests measure impact across multiple (conflicting) metrics that make success more subjective
2
1
3
Action Standards
4
Market contexts differ. One additional order in Market X is often not worth the same as in Market Y (or even in Market X at a different point in time), making KPIs like CPIO difficult to benchmark against

Action standards are the success criteria that need to be met in order to roll out a test 

Pricing Action Standards guiding principles
Use Return on Investment (ROI) within the organization to make comparing investments easier
Consider not only current situation but also the long term impact - implement only what delivers on the long term
Utilize a standardised & pre-defined decision process for acting on pricing A/B tests, removing subjectivity from decision making
2
1
3
Action Standards
4
Ensure the global approach is flexible enough to incorporate market-level conditions - allowing more aggressive investments in highly competitive or strategic markets

1
Unclear action → ??? 
Orders went up and profit went down
The main framework: There are 4 potential scenarios when you run a pricing test - orders and profit either increase or decrease; we calculate ROIs in scenarios with mixed results to determine the action plan (rollout / roll back)
If we decrease prices, [1] Orders go Up and [2] profit goes Down 
When decreasing prices, check CPIO (cost per incremental order) to calculate ROI

Δ Orders
Δ FLGPO
Action
Clear action → ✓✓✓  Rollout
Clear action → XXX Roll back
Action Standards
Challenge 1: Most pricing tests result in a tradeoff between orders and profit, which is subject to interpretation
Core of action standards:
If we increase prices, [1] Orders go Down and [2] profit goes Up
When increasing prices, check PPOL (profit gained per order lost) to calculate ROI…
…AND check Recoup ROI to make sure you can easily make those lost orders back with the profit you gained (i.e., at a low – or “cheap” – ROI)
Up
Up
Up
Down
Down
Up
Down
Down
*CPIO and PPOlLare calculated based on pricing A/B tests
Inspired by 
Unclear action → ??? 
Orders went down and profit went up
1

Recoup ROI for price increases: “I should only implement this price increase if I can redeploy these savings knowing I only need an ROI of at least X%, to ensure I can capture any lost orders
What is Recoup ROI?   

The minimum ROI you would need to achieve in order to “recoup” the lost orders, by reinvesting the profit from a price increase 
If we can find another growth channel where we can re-deploy this capital to recoup lost orders, and achieve at least the ROI of the recoup ROI, then we can increase prices without losing orders

The lower the recoup ROI, the lower the “bar” is for re-investing the profit gained from your pricing decision to “recoup” the lost orders (i.e., the easier / the better)
Recoup ROIs should be lower than the threshold set in your action standards
Recoup ROI

Recoup ROI   = 
HOW TO CALCULATE ROI
Challenge 2: We need pricing ROIs to be comparable for more efficient investment decisions
PPOL
FLGPOcontrol
— 1
ROI   = 
FLGPOcontrol
CPiO
— 1
ROI   = 
ΔOrders
Ordersvariant * ΔFLGPO
PPOL    = 
ΔOrders
Ordersvariant * ΔFLGPO
CPiO  = 
PPOL
FLGPOvariant
Recoup ROI
— 1
=
NOTE: Important for CPIO scenarios that the “cost” is translated to be comparable to other marketing / growth investments
Price decrease
Price increase
2
We can use CPIO and PPOL to calculate expected ROIs, using a direct relationship with order-level profit (FLGPO)
*Substitute expected “future FLGPO” into ROI equation (vs. FLGPO control) as one step in translating to longer term view

Expected future FLGPO (3Y Average) = 2€
The main framework: We need to incorporate the expected long-term impact of the pricing change, based on short-term (6-12 week) experiment results
Challenge 3: What we measure in the test is not fully representative of the future
2.2
1.9
1.8
1.7
Week 6
Week 2
Week 4
Week 8
Week 10
Week 12
“If today I make 1.5€/order, and I will make on average 2€/order in the next 3 years, paying 1.7€ per incremental order (CPIO) today makes sense”
CPiO
Today’s FLGPO  = 1.5€
2.0
€
What will change in the future vs. experiment results
Today’s FLGPO is likely lower than the future expected FLGPO → need to incorporate expected future FLGPO
Pricing changes take time for customers to adjust to (i.e., CPIOs and PPOLs tend to decrease / increase over time) → need to understand the risk of them changing enough to cause a different ROI-based decision
1
Action Standards
3

CPIO: Roll out a “decrease” in pricing if:
CPIO vs. expected FLGPO yields an ROI above the ROI threshold  
(usually ROI > 0; i.e., breakeven)
PPOL: Roll out an “increase” in pricing if:
PPOL vs. expected FLGPO yields an ROI above the ROI threshold  
And if Recoup ROI is below the Recoup ROI threshold
The main framework: An ROI-based set of rules, calculated by comparing expected long term CPIO/PPOL of pricing changes relative to market FLGPO (i.e., ROIs), using A/B experiment results
When decreasing prices, check ROI by comparing CPIO to expected future FLGPO
“If the cost of each incremental order from this pricing change is less than my (expected) profit per order, then this is a positive ROI decision”
Δ Orders
Δ FLGPO
Action
Win-win ⇒ Rollout!!!
Lose-lose ⇒ Roll back!!!
Action Standards
How this comes together: A pricing test should only be implemented if it passes the ROI checks set in the action standard framework
Core of action standards:
When increasing prices, check ROI by comparing PPOL to expected future FLGPO
“If the Profit I gain Per Order I Lose (PPOL) from this pricing change is more than my (expected) profit per order, then this is a positive ROI decision”
AND check if Recoup ROI < Recoup ROI threshold
“If I am confident I can also recover the orders I’m losing through another channel, then I can roll out this pricing test”
Up
Up
Up
Down
Down
Up
Down
Down
*CPIO and PPOL are calculated based on pricing A/B tests
Inspired by 
CHECK
CHECK
CHECK

Action Standards: evaluating an experiment under PAS Framework
After test is run for recommended time, check results to see if significance of orders and/or profit has been reached 
Reaching significant results on focus KPIs validates impact of Pricing Action led to an impact (non-significance does not prove absence of effect)
E.g., Launching Saver to boost growth in market, or DF decrease to drive growth in Orders →  we need to see a significant impact on Orders
Checking for Significance
(existing check even before PAS)
Calculate CPIOs and ROI
If Focus KPI (Orders per user or Profit per Order) has reached significance → 
Calculate PPOL/CPiO as per the updated methodology (aligned with other Growth levers) and ROIs
Evaluate ROI against market specific ROI threshold
Confidence Interval (CPIO cases)
Verification of the likelihood that orders will shift further, and not turn the results in unfavorable direction  
Recoup ROI check (PPOL Cases)
Check to see if and how likely it would be for the profit gained could be reinvested to regain lost orders. 

Evaluate Orders Confidence Interval (CPIO cases) / Recoup ROI (PPOL cases)
Additionally, partial rollouts done based on elasticity experiments, need to be re-validated with B/A testing to ensure that conclusions determined for partial implementation were not impacted by cannibalisation effects
Test should be deprecated and hypothesis redesigned if any of the checks above are failed
1
2
3
3



A/B Experiment Significance dashboard


ROI Simulator
Relevant global dashboards

Elasticity Experiments
Run Elasticity tests on large population
Measure performance
Analyze
Group
Customers/ Vendors
Running elasticity test with varying price points to assess impact on CVRs due to price
Analyze the results of the elasticity tests with groupings
Rely on CVR variations across different groups to analyze sensitivities across different segments
The results are groups of areas that are significantly “distinctive”, to limit operational overheads
4-6 weeks
8-10 weeks**
2-3 weeks
Re-test with “analyzed” hypothesis
Setup the analyzed configuration as a B/A experiment to validate the Grouping made via analysis
Segmentation Strategy
Global Pricing is working on a new methodology (using Impressions data) to shorten the 1st stage significantly (aim: 1-2 weeks)
Would vary based on Market being tested (duration varying on magnitude of price change and testing methodology)

3. ROI methodology

3a. Making pricing investments comparable

Cost per incremental order =
Traditionally, we assess pricing tests on basis of CPiO and PPOL 

Profit per order lost =
Marginal gain
Diff in orders
Incremental cost
Diff in orders
DF
DF
Cool, so what is my Return on Investment?
But what did you invest?
Also, what did you want as return? GMV? GP? CP? FLGP? AEBITDA?

Simplified PnL for OD food and implications of affordability investments 
   Pricing and Basket Incentives impact PnL differently
Commission Revenues	based on basket size & contractual commission rates and vendor funded deals
Delivery Revenues	based on several factors as determined by DPS and any DF campaigns (exc. SF)
Other Revenues and Fees	includes any other revenue streams, e.g., subscription revenues, service fees, etc. 
Rider Costs	costs to cover rider salary and bonuses for executing deliveries
Cost of Sales	other costs of doing business - includes payment gateway costs, contact center, etc. 
Other Delivery Costs	associated with delivery riders - includes customer compensation, rider recruitment, dispatcher, etc.
Gross Profit	profit earned by delivering/executing orders
Basket Incentives	money spent as part of marketing initiatives to offer basket discounts to customers for acquisitions or reorders
Fully Loaded Gross Profit	effective profit per order including impact from basket incentives
Slight detour into the world of Accounting and Finance

I want to drive higher topline - Should I invest in Pricing or Basket Incentives?
Successful Orders [units]
100
110
110
110
GPO [€]
1.00
0.85
1.00
1.00
Gross Profit [€]
100
93.5
110
110
Marketing investment [€]
0
0.0
-6.5
-16.5
Fully Loaded Gross Profit [€]
100
93.5
103.5
93.5
Δ Orders
-
+10 
+10
+10
abs (Marketing investment)
-
-
6.5
16.5
Δ GP
-
-6.5
+10
+10
CPiO = ΔCost / ΔOrders
-
0.65
0.65
1.65
ROI = ΔFLGP / abs (Mkt. Investment)
-
???
54%
-39%
Pricing reduction
Basket Incentives 
Adjusted Pricing PnL
Status Quo 
Simplified UE
Incrementality
Decision KPIs
Comparing 		to 		
Δ FLGP
-
-6.5
+3.5
-6.5
= ΔFLGPO * Ordersvariant
CPiO simulation (pricing vs. basket incentives)
FLGPO [€]
1.00
0.85
0.94
0.85

Defining CPiO, PPOL, and "equivalent" Marketing Investment
CPiO Scenario: Orders           Profit
PPOL Scenario: Orders 	         Profit
Mkt. Investment = Ordersvariant * Δ FLGPO
ΔOrders
Ordersvariant * ΔFLGPO
CPiO  = 
Mkt. Investment = Δ Orders * FLGPOcontrol
ΔOrders
Ordersvariant * ΔFLGPO
PPOL  = 
CPiO (status quo) = net loss in profit due to pricing decrease
PPOL (status quo) = net gain in profit due to pricing increase
Incremental orders 
Orders lost

3b. ROI equations

Δ Orders
Total Profitcontrol
CPiO Scenario: Price dilution to drive topline [Orders		FLGPO       ] 
Total Profitvariant
Orderscontrol ; FLGPOcontrol 
Profit per order → 
Total Orders → 
Ordersvariant ; FLGPOvariant 
ROI   = 
Mkt. Investment 
Ordersvariant * Δ FLGPO
Ordersvariant * FLGPOvariant —  Orderscontrol * FLGPOcontrol
Δ Orders * FLGPOvariant —  (Ordersvariant – Δ Orders) *Δ FLGPO
Ordersvariant * Δ FLGPO
Δ Orders * FLGPOvariant +  Δ Orders *Δ FLGPO
Ordersvariant * Δ FLGPO
— 1
Δ Orders * (FLGPOvariant +  FLGPOcontrol — FLGPOvariant)
Ordersvariant * Δ FLGPO
— 1
Δ Orders * FLGPOcontrol
Ordersvariant * Δ FLGPO
— 1
Δ Profit
ROI   = 
ROI   = 
ROI   = 
ROI   = 
ROI   = 
FLGPOcontrol
CPiO
— 1
ROI   = 
ΔOrders
Ordersvariant * ΔFLGPO
CPiO  = 
ROI   = 
Mkt. Investment 
Total Profitvariant — Total Profitcontrol
Δ Orders * FLGPOvariant —  Orderscontrol *Δ FLGPO
Ordersvariant * Δ FLGPO
ROI   = 
Δ FLGPO
** if Mkt investment is not included in numerator, the factor of -1 is not needed

Total Profitcontrol
Total Profitvariant
PPOL Scenario: Price increase to drive up profitability [Orders	FLGPO       ] 

Orderscontrol ; FLGPOcontrol 
Profit per order → 
Total Orders → 
ROI   = 
Mkt. Investment 
Δ Orders * FLGPOcontrol
Ordersvariant * FLGPOvariant —  Orderscontrol * FLGPOcontrol
Ordersvariant * FLGPOvariant —  (Ordersvariant + Δ Orders) * FLGPOcontrol
Δ Orders * FLGPOcontrol
Ordersvariant  * FLGPOvariant —  Ordersvariant * FLGPOcontrol
Δ Orders * FLGPOcontrol
— 1
Ordersvariant * (FLGPOvariant —   FLGPOcontrol )
Δ Orders * FLGPOcontrol
— 1
Ordersvariant * Δ FLGPO
Δ Orders * FLGPOcontrol
— 1
Δ Profit
ROI   = 
ROI   = 
ROI   = 
ROI   = 
ROI   = 
PPOL
FLGPOcontrol
— 1
ROI   = 
ΔOrders
Ordersvariant * ΔFLGPO
PPOL  = 
ROI   = 
Mkt. Investment 
Total Profitvariant — Total Profitcontrol
Ordersvariant ; FLGPOvariant 
Δ Orders
Δ FLGPO
** if Mkt investment is not included in numerator, the factor of -1 is not needed

Ordersvariant * Δ FLGPO

Recoup ROI for PPOL scenario: “If i can redeploy these savings at an ROI of X%, then I should implement this price increase”
Δ Orders   *    FLGPOvariant— Ordersvariant * Δ FLGPO
Recoup ROI   = The minimum ROI you would need to achieve in order to make up the lost orders from a price increase
=
PPOL
FLGPOvariant
=
ΔOrders
Ordersvariant * ΔFLGPO
PPOL  = 
ROI   = 
Mkt. Investment 
Δ Profit
Mkt. Investment = Ordersvariant * Δ FLGPO
Same equation as the CPIO scenario
Δ Profit = Δ Orders   *    FLGPOvariant (*) — Ordersvariant * Δ FLGPO
What is the total profit (FLGP variant) I would get back if I recovered the lost orders from the price increase (Δ Orders)
(*) FLGPO variant or FLGPO control could arguably be used for the Recoup ROI formula depending on whether or not the implemented price change would impact the “recovered” orders
Recoup ROI 
Ordersvariant * Δ FLGPO

Δ Orders   *    FLGPOvariant
=
—  1
— 1
Recoup ROI 
** if Mkt investment is not included in numerator, the factor of -1 is not needed
If we can find another growth channel where we can re-deploy this capital to recoup lost orders, and achieve at least the ROI of the recoup ROI, then we can increase prices without losing orders

CE ROI - Calculation and integration of segmentation
Inc. value (C-FLGP)
inc. Cost
Inc. transactional FLGP + Inc. HVA downstream FLGP 
Inc. DH Incentives Cost
ROI =
=
For most customer engagement actions, incentives are the only costs, channel costs (e-mail) are considered negligible at this stage.
Long-term value through behavioural change driven by HVAs. this value is calculated through lookalike and take into account :
HVA & Programme 
Lifecycle of the customer 
Value segment of the customer 
Incrementality of the marketing activities, or our ability to nudge extra customers to order/perform HVA.
Can be transformed into payback
Short-term value generated from the transaction (order FLGP).


4. Process to set ROI thresholds

How did we set ROI thresholds for each vertical?
Food:
Establish Investment Intensity (min/mid/max) per market based on Competition and Strategic Priority
Set ROI thresholds for 1yr calculation for each Investment Intensity bucket
Assess if high share of spend in non-targeted incentives - evaluate CPIOs for these incentives
Set ROI threshold as minimum of above 2 levers
Qcommerce:
Starting point: pre-aligned ROI thresholds on Food
Leverage vertical FLGPO to translate respective ROI thresholds into CPIOs
Compare CPIOs for Dmarts and Local Shops - if there is a wide disparity in the two, opt for the lower CPIO as the threshold for the market



Setting ROI thresholds: Set ROI thresholds per market-vertical, depending on the “investment level” of a market (i.e., how aggressively do we want to invest)
Long term, individual markets will have different ROI thresholds “X” and “Y”, set based on a framework of investment intensities… 
“X” and “Y” thresholds are set based on “Investment levels”, ranging from MIN to MAX
Entities may set their own thresholds per investment intensity with central team alignment
Markets should not deviate within an entity’s framework


If we are looking at a time period of less than 2 yrs, ROIs may be slightly below 0 (breakeven) as we aren’t fully capturing the incrementality (only in the case of a price decrease)

Investment matrix
ROI above threshold [X]
Recoup ROI below threshold [Y]
MIN
0%
-40%
MID
0%
-50%
MAX
-20%
-70%
Action Standards
Example ROI thresholds per investment intensity

…which utilize competitive position and strategic importance to determine pricing investment levels (and ideally, other growth levers)
Categorizing markets: Set the investment level based on the competitive position of the market…
“Leveling up” strategically important markets : …allowing movement “one level up” for any top strategically important markets, based on*:
Market AEBITDA at full potential (TAM AEBITDA)
Current state with TAM coverage (SAM as % TAM)
Positioning/penetration (Active users as %SAM)

* Details in Appendix
Updated quarterly: Re-evaluate the investment level on a quarterly basis, to prevent overly frequent / erratic decisions
Future granularity: Break down into further granularity by:
Customer segment (e.g., lifecycle, value segmentation)
Geography (e.g., city, capital / ex-capital)
Action Standards
