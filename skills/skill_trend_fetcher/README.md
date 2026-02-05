Markdown# Skill: Trend Fetcher

## Description

Fetches semantic trends via MCP (e.g., news://ethiopia/fashion).

## Input Contract (Pydantic)

```python
class TrendInput(BaseModel):
    query: str  # e.g., "fashion Ethiopia"
    limit: int = 5
```

Output Contract
Pythonclass TrendOutput(BaseModel):
trends: list[dict] # [{"topic": str, "relevance": float}]

# Skill: Trend Fetcher

Purpose: fetch trending topics and provide structured output.
