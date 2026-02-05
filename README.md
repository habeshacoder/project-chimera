# Project Chimera: Autonomous Influencer Network

This repository implements the infrastructure for Project Chimera, per the SRS and 3-Day Challenge. It follows Spec-Driven Development: Specs define intent, failing tests set goals for AI agents to implement code.

## Setup

- Install prerequisites: `pip install uv`
- Run `make setup`
- Test: `make test` (expect failures—ready for implementation)

## Structure

- `specs/`: Ratified specifications.
- `tests/`: Failing TDD tests.
- `skills/`: Runtime skill interfaces.
- `research/`: Day 1/2 research.
- `.claude/rules.md`: Context rules for IDE AI (adapt for VSCode extensions).
- CI/CD: Runs on push.

MCP Sense: Connected for telemetry.
