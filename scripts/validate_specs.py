#!/usr/bin/env python3
"""Validate that code implementations align with specifications."""
import json
import re
from pathlib import Path
from typing import Dict, List


def check_spec_files_exist():
    """Verify all required spec files exist."""
    required_specs = [
        "specs/_meta.md",
        "specs/functional.md",
        "specs/technical.md",
        "specs/openclaw_integration.md"
    ]
    missing = []
    for spec in required_specs:
        if not Path(spec).exists():
            missing.append(spec)
    return missing


def check_markdown_formatting():
    """Check for common markdown formatting issues."""
    issues = []
    spec_files = list(Path("specs").glob("*.md"))
    for spec_file in spec_files:
        content = spec_file.read_text()
        if "Markdown#" in content:
            issues.append(f"{spec_file}: Contains 'Markdown#' prefix")
        if "#mermaid-diagram-mermaid" in content and "```mermaid" not in content:
            issues.append(f"{spec_file}: Contains broken Mermaid HTML")
        if "text###" in content:
            issues.append(f"{spec_file}: Contains 'text###' prefix")
    return issues


def check_skill_contracts():
    """Verify skill READMEs define I/O contracts."""
    skill_dirs = list(Path("skills").glob("skill_*"))
    missing_contracts = []
    for skill_dir in skill_dirs:
        readme = skill_dir / "README.md"
        if not readme.exists():
            missing_contracts.append(f"{skill_dir}: Missing README.md")
            continue
        content = readme.read_text()
        if "Input Contract" not in content or "Output Contract" not in content:
            missing_contracts.append(f"{skill_dir}: Missing I/O contracts in README")
    return missing_contracts


def check_skill_implementations():
    """Verify skills have __init__.py files."""
    missing_impls = []
    skill_dirs = list(Path("skills").glob("skill_*"))
    for skill_dir in skill_dirs:
        init_file = skill_dir / "__init__.py"
        if not init_file.exists():
            missing_impls.append(f"{skill_dir}: Missing __init__.py")
    return missing_impls


def check_test_files():
    """Verify test files exist for all skills."""
    missing_tests = []
    skill_dirs = list(Path("skills").glob("skill_*"))
    test_dir = Path("tests")
    
    # Map skill names to expected test files
    skill_to_test = {
        "skill_trend_fetcher": "test_trend_fetcher.py",
        "skill_content_generator": "test_content_generator.py",
        "skill_transaction_executor": "test_transaction_executor.py"
    }
    
    for skill_dir in skill_dirs:
        skill_name = skill_dir.name
        expected_test = skill_to_test.get(skill_name)
        if expected_test:
            test_file = test_dir / expected_test
            if not test_file.exists():
                missing_tests.append(f"Missing test file: tests/{expected_test} for {skill_name}")
    
    return missing_tests


def check_mermaid_diagrams():
    """Verify Mermaid diagrams are properly formatted."""
    issues = []
    spec_files = list(Path("specs").glob("*.md"))
    for spec_file in spec_files:
        content = spec_file.read_text()
        # Check for proper mermaid code blocks
        mermaid_blocks = re.findall(r'```mermaid\s*\n(.*?)```', content, re.DOTALL)
        if "erDiagram" in content or "flowchart" in content:
            if not mermaid_blocks:
                issues.append(f"{spec_file}: Contains Mermaid keywords but no proper code block")
    return issues


def main():
    """Run all validation checks."""
    errors = []
    warnings = []
    
    # Check spec files exist
    missing_specs = check_spec_files_exist()
    if missing_specs:
        errors.extend([f"Missing spec file: {s}" for s in missing_specs])
    
    # Check formatting
    formatting_issues = check_markdown_formatting()
    if formatting_issues:
        errors.extend(formatting_issues)
    
    # Check skill contracts
    contract_issues = check_skill_contracts()
    if contract_issues:
        warnings.extend(contract_issues)
    
    # Check skill implementations
    impl_issues = check_skill_implementations()
    if impl_issues:
        warnings.extend(impl_issues)
    
    # Check test files
    test_issues = check_test_files()
    if test_issues:
        warnings.extend(test_issues)
    
    # Check Mermaid diagrams
    mermaid_issues = check_mermaid_diagrams()
    if mermaid_issues:
        warnings.extend(mermaid_issues)
    
    # Report results
    if errors:
        print("❌ ERRORS:")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    if not errors and not warnings:
        print("✅ All spec validations passed!")
        return 0
    
    return 1 if errors else 0


if __name__ == "__main__":
    exit(main())
