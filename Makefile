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

.PHONY: setup clean-venv test help

# --- Targets ---

help:
	@echo Project Chimera - Makefile Help
	@echo -------------------------------
	@echo make setup        - Create venv and sync all dependencies
	@echo make clean-venv   - Remove the .venv folder
	@echo make test         - Build and run Docker tests
	@echo make help         - Show this help

setup: clean-venv
	@echo [1/2] Creating virtual environment and syncing dependencies...
	uv sync
	@echo [2/2] Setup complete.
	@echo ""
	@echo To activate the venv:
	@echo "  Windows (cmd):      .venv\\Scripts\\activate.bat"
	@echo "  Windows (PS):       .venv\\Scripts\\Activate.ps1"
	@echo "  Unix/Git Bash:      source .venv/Scripts/activate   (or .venv/bin/activate)"

clean-venv:
	@echo Cleaning .venv...
	-@$(CLEAN_VENV)

test:
	@echo Building Docker image...
	docker build -t chimera-test .
	@echo ============ Running Docker tests...
	docker run --rm chimera-test