text### research/tooling_strategy.md

```markdown
# Tooling Strategy

## Developer Tools (MCP)

- git-mcp: For version control traceability.
- filesystem-mcp: For file editing in IDE.
- Configured in MCP Sense for telemetry.

## Runtime Agent Skills

- Separation: Skills are reusable functions (e.g., in skills/ dir); MCP Servers handle external bridges (e.g., DB connectors).
- Critical Skills (3+): trend_fetcher, content_generator, transaction_executor (see skills/ READMEs for I/O).

## Environment

- uv for Python env.
- Docker for reproducibility.
```

# Tooling Strategy

Notes on recommended developer tools, CI, linters, and test strategy.

TODO: list chosen tools and configuration steps.
