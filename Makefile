Makefile
makefilesetup:
	uv venv .venv
	. .venv/Scripts/activate && uv pip sync pyproject.toml  # Windows-friendly

test:
	docker build -t chimera-test .
	docker run chimera-test  # Runs pytest; expect failures

spec-check:
	@echo "TODO: Implement spec alignment checker (e.g., grep for schema matches)"
PYTEST ?= pytest

.PHONY: test
test:
	$(PYTEST)
