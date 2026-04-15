---
name: pricing-orchestrator
description: Route pricing-related user requests to the most appropriate skill or workflow. Use when a request may require business explanation, data analysis, or both together across pricing and analytics contexts.
allowed-tools: Read, Grep, Glob
---

# Pricing Orchestrator

A routing skill that helps determine how to handle pricing and analytics requests.

## Instructions

Your job is to classify the user request into one of these modes:

1. Business explanation only
2. Data analysis / SQL workflow
3. Combined analysis plus business interpretation

## Routing Logic

### Route to `dh-pricing-expert` when:
- the question is conceptual
- the user wants KPI meaning
- the user wants a stakeholder-friendly explanation
- the user is asking about tradeoffs, strategy, or interpretation

### Route to `data-analyst-expert` when:
- the question requires BigQuery access
- the user asks for metrics or trends
- the user needs SQL
- the user wants validation using data

### Use both when:
- the user needs data plus interpretation
- the user wants experiment analysis and business explanation
- the user wants a technical answer translated into business terms

## Output Style

When routing, be explicit about:
- what kind of task this is
- which skill should lead
- whether another skill should add interpretation

Keep routing decisions simple and practical.