text### specs/openclaw_integration.md

```markdown
# OpenClaw Integration Specification

## Plan

- Expose agent status via MCP Resource: `agent://status/{agent_id}` (e.g., JSON: {"available": true, "skills": ["trend_fetch"]}).
- Publish trends/collaborations to OpenClaw hubs via MCP Tools.
- Protocols: Semantic querying (Weaviate), on-chain events (Coinbase wallet), inter-agent messaging (MCP stdio/HTTP).
- Governance: Only approved signals; HITL for collaborations.
```

# OpenClaw Integration

Notes for integrating with OpenClaw (external system) and required adapters.
