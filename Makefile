setup:
	uv venv .venv
	. .venv/Scripts/activate && uv pip sync pyproject.toml  # Windows path

test:
	docker build -t chimera-test .
	docker run chimera-test

spec-check:
	@echo "TODO: Implement spec alignment checker (e.g., grep for schema matches)"

clean-venv:
	- rmdir /s /q .venv 2>nul || exit /b 0
	@echo Cleaned .venv folder (if it existed)

.PHONY: test