Markdown# Project Chimera Rules

## Project Context

This is Project Chimera, an autonomous influencer system per SRS: FastRender Swarm (Planner-Worker-Judge), MCP for integrations, Agentic Commerce via Coinbase AgentKit, HITL safety, RAG with Weaviate/Redis/PostgreSQL.

## Prime Directive

NEVER generate code without checking specs/ first. Always reference specs/functional.md, specs/technical.md.

## Traceability

Explain your plan before writing code. Log all actions for MCP Sense telemetry.

## MCP Requirement

Keep Tenx MCP Sense connected. Use MCP for dev tools (e.g., git-mcp, filesystem-mcp).

## Governance

Enforce SDD: Specs are source of truth. Use pydantic for schemas. No direct API calls—use MCP.

## Question Handling Example

If asked: "Implement trend fetcher", respond: "Per specs/technical.md, schema is {...}. Plan: Define function with pydantic validation. Code: ..."

# Claude Rules

Purpose: store workspace-specific rules and prompts for Claude integrations.

- Keep rules concise and actionable.
- Do not include secrets.
