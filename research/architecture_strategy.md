Markdown# Architecture Strategy

## Insights from Readings (Summary from Day 1 Report)

- a16z: AI agents in structured envs (repos, sandboxes) for productivity; treat agents as users.
- OpenClaw: Agent social networks for collaboration; need protocols for status sharing.
- MoltBook: Bot-only social media; risks of unconstrained autonomy → need governance.
- SRS: Swarm pattern, MCP, Agentic Commerce, HITL, scalability.

## Architectural Decisions

- Pattern: Hierarchical Swarm (Planner-Worker-Judge) per SRS 3.1. Why: Parallelism, governance over alternatives (sequential too slow, flat lacks coherence).
- HITL: In Judge layer only, for escalated cases (low confidence/sensitive).
- Database: PostgreSQL (transactional/ACID for finance/logs), Weaviate (semantic memory/RAG), Redis (queues/cache).
- Scaling: Kubernetes/Docker for Workers.
- OpenClaw: Expose status via MCP Resources; on-chain signaling.

## Diagrams (Mermaid)

```mermaid
flowchart TD
    A[Orchestrator Dashboard / Human HITL] --> B[Set Goals]
    B --> C[Planner]
    C -->|Monitor MCP Resources| D[MCP Resources e.g. twitter://mentions, news://trends]
    C -->|Push Tasks| E[Task Queue Redis]
    E --> F[Worker Pool Stateless Containers]
    F -->|Execute MCP Tools| G[MCP Servers e.g. twitter, ideogram, coinbase]
    F -->|Result + Confidence| H[Review Queue Redis]
    H --> I[Judge]
    I -->|Approve OCC Check| J[Global State Weaviate + PostgreSQL]
    I -->|Reject/Retry| C
    I -->|Escalate Medium/Low Confidence| A
    J -->|Feedback Loop| C
    (See Day 1 Report for more diagrams.)
```

# Architecture Strategy

Summary of high-level architecture decisions and trade-offs.

TODO: expand with diagrams and component boundaries.
