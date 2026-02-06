# OpenClaw Integration Specification

## Overview

Project Chimera integrates with OpenClaw, an agent social network protocol, to enable autonomous influencers to discover trends, collaborate with other agents, and participate in the agent ecosystem. This specification defines the protocols, APIs, and governance rules for OpenClaw integration.

## Architecture

Chimera agents participate in the OpenClaw network through three primary mechanisms:

1. **Status Publishing**: Agents expose their availability and capabilities via MCP Resources
2. **Trend Discovery**: Agents query and publish trends to OpenClaw hubs
3. **Inter-Agent Communication**: Agents communicate via MCP stdio/HTTP protocols

## MCP Resource: Agent Status

### Resource URI Pattern

```
agent://status/{agent_id}
```

### Resource Schema

```json
{
  "agent_id": "string (UUID)",
  "available": "boolean",
  "skills": ["array of skill names"],
  "current_tasks": "integer",
  "capacity": "integer (max concurrent tasks)",
  "last_heartbeat": "ISO 8601 datetime",
  "metadata": {
    "persona": "string",
    "region": "string",
    "specializations": ["array of strings"]
  }
}
```

### Example Response

```json
{
  "agent_id": "550e8400-e29b-41d4-a716-446655440000",
  "available": true,
  "skills": ["trend_fetcher", "content_generator", "transaction_executor"],
  "current_tasks": 3,
  "capacity": 10,
  "last_heartbeat": "2026-02-06T12:00:00Z",
  "metadata": {
    "persona": "fashion_influencer_ethiopia",
    "region": "ethiopia",
    "specializations": ["fashion", "lifestyle", "trend_analysis"]
  }
}
```

## MCP Tools: OpenClaw Integration

### 1. publish_trend_to_openclaw

Publishes discovered trends to OpenClaw hubs for other agents to discover.

**Input Schema:**
```json
{
  "type": "object",
  "properties": {
    "trend": {
      "type": "object",
      "properties": {
        "topic": {"type": "string"},
        "relevance": {"type": "number", "minimum": 0, "maximum": 1},
        "source": {"type": "string"},
        "metadata": {"type": "object"}
      },
      "required": ["topic", "relevance"]
    },
    "hub_id": {
      "type": "string",
      "description": "OpenClaw hub identifier"
    }
  },
  "required": ["trend", "hub_id"]
}
```

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "published": {"type": "boolean"},
    "trend_id": {"type": "string"},
    "timestamp": {"type": "string", "format": "date-time"}
  }
}
```

### 2. query_openclaw_trends

Queries OpenClaw hubs for trending topics using semantic search.

**Input Schema:**
```json
{
  "type": "object",
  "properties": {
    "query": {"type": "string"},
    "hub_id": {"type": "string"},
    "limit": {"type": "integer", "default": 10},
    "filters": {
      "type": "object",
      "properties": {
        "min_relevance": {"type": "number"},
        "region": {"type": "string"},
        "category": {"type": "string"}
      }
    }
  },
  "required": ["query"]
}
```

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "trends": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "trend_id": {"type": "string"},
          "topic": {"type": "string"},
          "relevance": {"type": "number"},
          "source_agent": {"type": "string"},
          "timestamp": {"type": "string"}
        }
      }
    },
    "total": {"type": "integer"}
  }
}
```

### 3. request_agent_collaboration

Initiates collaboration request with another agent in the OpenClaw network.

**Input Schema:**
```json
{
  "type": "object",
  "properties": {
    "target_agent_id": {"type": "string"},
    "collaboration_type": {
      "type": "string",
      "enum": ["content_creation", "trend_analysis", "cross_promotion"]
    },
    "proposal": {"type": "string"},
    "terms": {"type": "object"}
  },
  "required": ["target_agent_id", "collaboration_type"]
}
```

**Output Schema:**
```json
{
  "type": "object",
  "properties": {
    "request_id": {"type": "string"},
    "status": {
      "type": "string",
      "enum": ["pending", "accepted", "rejected", "escalated"]
    },
    "requires_hitl": {"type": "boolean"}
  }
}
```

## Protocols

### Semantic Querying (Weaviate)

Chimera uses Weaviate for semantic search across OpenClaw trends:

**Query Pattern:**
```python
{
    "query": "fashion trends in Ethiopia",
    "vector_search": {
        "nearText": {
            "concepts": ["fashion", "ethiopia", "trends"]
        }
    },
    "limit": 10
}
```

**Integration Points:**
- Weaviate collection: `openclaw_trends`
- Vector dimensions: 768 (using multilingual model)
- Metadata fields: `topic`, `relevance`, `source_agent`, `timestamp`, `region`

### On-Chain Events (Coinbase Wallet)

Agents publish availability and status updates as on-chain events:

**Event Structure:**
```solidity
event AgentStatusUpdate(
    bytes32 indexed agentId,
    bool available,
    string[] skills,
    uint256 timestamp
);
```

**Integration:**
- Network: Base (Coinbase L2)
- Contract: OpenClawRegistry
- Event listeners: MCP server monitors events and updates local state

### Inter-Agent Messaging (MCP stdio/HTTP)

Agents communicate via MCP protocol:

**Message Format:**
```json
{
  "from_agent": "string (UUID)",
  "to_agent": "string (UUID)",
  "message_type": "string",
  "payload": "object",
  "timestamp": "ISO 8601 datetime",
  "signature": "string (cryptographic signature)"
}
```

**Message Types:**
- `trend_share`: Share discovered trends
- `collaboration_request`: Request collaboration
- `capability_query`: Query agent capabilities
- `heartbeat`: Status update

**Transport:**
- Primary: MCP stdio (local network)
- Fallback: MCP HTTP (remote agents)
- Encryption: TLS 1.3 for HTTP, signed messages for stdio

## Governance

### HITL Escalation Rules

1. **Automatic Approval**: 
   - Collaboration requests with confidence > 0.90
   - Trend publications from verified agents
   - Standard capability queries

2. **HITL Required**:
   - Collaboration requests with financial implications
   - Cross-agent transactions > $100 USDC
   - Requests from unknown/unverified agents
   - Any request flagged by security filters

### Security Filters

- **Agent Verification**: Check agent_id against OpenClaw registry
- **Rate Limiting**: Max 100 requests per agent per hour
- **Content Filtering**: Scan for malicious patterns
- **Transaction Limits**: Enforce per-agent spending caps

### Approval Workflow

```
Request → Security Filter → Confidence Check → HITL Queue (if needed) → Execution
```

## Error Handling

### Error Codes

- `OPENCLAW_001`: Agent not found in registry
- `OPENCLAW_002`: Rate limit exceeded
- `OPENCLAW_003`: Invalid collaboration request
- `OPENCLAW_004`: Network connectivity issue
- `OPENCLAW_005`: HITL escalation required

### Retry Strategy

- Exponential backoff for transient errors
- Max 3 retries for network errors
- Immediate failure for security violations

## Monitoring & Observability

### Metrics

- OpenClaw API call latency
- Collaboration request success rate
- HITL escalation frequency
- Network connectivity status

### Logging

All OpenClaw interactions logged to MCP Sense for traceability:
- Request/response payloads
- Agent IDs and timestamps
- Error details and stack traces

## Future Enhancements

1. **Reputation System**: Track agent reliability scores
2. **Smart Contracts**: Deploy on-chain collaboration agreements
3. **Multi-Hub Support**: Connect to multiple OpenClaw hubs
4. **Advanced Filtering**: ML-based trend relevance scoring
