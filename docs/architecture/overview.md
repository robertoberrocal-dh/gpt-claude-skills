# Architecture Overview

This repository is designed around modular Claude skills for the Global Pricing Team.

## Design Philosophy

The architecture follows three principles:

1. **Specialization**  
   Each skill should have a clear purpose and activation scope.

2. **Composability**  
   Skills should work well together rather than trying to solve every problem alone.

3. **Scalability**  
   The repository should support future integrations with external systems and user-facing interfaces.

## Skills

### data-analyst-expert
Primary analytics execution skill.

Responsibilities:
- Understand business questions
- Map them to approved BigQuery datasets
- Validate schema
- Generate safe SQL
- Execute queries when appropriate
- Explain findings clearly

### dh-pricing-expert
Primary business and pricing knowledge skill.

Responsibilities:
- Explain pricing concepts and KPIs
- Support business interpretation
- Help with experiment reasoning
- Translate technical findings into stakeholder language

### pricing-orchestrator
Routing and coordination skill.

Responsibilities:
- Detect whether a request is analytical, business-oriented, or mixed
- Invoke the most relevant skill or combination of skills
- Help produce the most appropriate response style

## Future Integrations

Planned future integrations may include:
- Slack as user-facing chat UI
- BigQuery execution tools or MCP
- Jira and Confluence knowledge and workflow access
- Google Drive and Google Docs
- Gemini / Gemini CLI as complementary tools where appropriate

## Intended Flow

A typical future interaction may look like this:

1. User asks a question in Slack
2. Claude receives the request
3. `pricing-orchestrator` routes the task
4. `data-analyst-expert` handles SQL/data retrieval if needed
5. `dh-pricing-expert` adds business interpretation if needed
6. Final answer is returned in a user-friendly format

## Key Constraint

Skills should remain useful even before all tool integrations are available.  
That means each skill should be valuable on its own, while also being ready for future orchestration.