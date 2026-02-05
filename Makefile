setup:
	uv venv .venv
	. .venv/Scripts/activate && uv pip sync pyproject.toml  # Windows path

test:
	docker build -t chimera-test .
	docker run chimera-test

spec-check:
	@echo "TODO: Implement spec alignment checker (e.g., grep for schema matches)"

.PHONY: test