# --- Platform Detection ---
ifeq ($(OS),Windows_NT)
    # Windows (CMD or PowerShell)
    VENV_BIN := .venv\Scripts
    RM_DIR := rmdir /s /q
    # detect if we are in a bash-like shell on Windows (like Git Bash)
    ifeq ($(findstring sh,$(SHELL)),sh)
        CLEAN_VENV := rm -rf .venv
    else
        CLEAN_VENV := if exist .venv $(RM_DIR) .venv
    endif
else
    # Unix / macOS
    VENV_BIN := .venv/bin
    CLEAN_VENV := rm -rf .venv
endif

.PHONY: setup clean-venv test spec-check help

# --- Targets ---

help:
	@echo Project Chimera - Makefile Help
	@echo -------------------------------
	@echo make setup        - Create venv and sync all dependencies
	@echo make clean-venv   - Remove the .venv folder
	@echo make test         - Build and run Docker tests
	@echo make spec-check   - Validate specs alignment with code
	@echo make help         - Show this help

setup: clean-venv
	@echo [1/2] Creating virtual environment and syncing dependencies...
	@echo "Setting UV_HTTP_TIMEOUT to 180s for slow network connections..."
ifeq ($(OS),Windows_NT)
	@set UV_HTTP_TIMEOUT=180 && uv sync || (echo Retrying with increased timeout... && set UV_HTTP_TIMEOUT=300 && uv sync)
else
	@UV_HTTP_TIMEOUT=180 uv sync || (echo "Retrying with increased timeout (300s)..." && UV_HTTP_TIMEOUT=300 uv sync)
endif
	@echo [2/2] Setup complete.
	@echo ""
	@echo To activate the venv:
	@echo "  Windows (cmd):      .venv\\Scripts\\activate.bat"
	@echo "  Windows (PS):       .venv\\Scripts\\Activate.ps1"
	@echo "  Unix/Git Bash:      source .venv/Scripts/activate   (or .venv/bin/activate)"
	@echo "  macOS:      source .venv/bin/activate   (or .venv/bin/activate)"

clean-venv:
	@echo Cleaning .venv...
	-@$(CLEAN_VENV)

test:
	@echo "Building Docker image (no cache to ensure latest changes)..."
	docker build  -t chimera-test .
	@echo "============ Running Docker tests..."
	docker run --rm chimera-test

spec-check:
	@echo Running spec validation...
	python scripts/validate_specs.py