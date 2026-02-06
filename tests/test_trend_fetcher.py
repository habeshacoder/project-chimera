import pytest
from pydantic import BaseModel
from typing import List, Dict, Any


# These models must match your specs/technical.md and skill README contract
class TrendInput(BaseModel):
    query: str
    # Optional fields can be added later, but minimal contract is query
    limit: int = 5


class TrendOutput(BaseModel):
    trends: List[Dict[str, Any]]  # e.g. [{"topic": str, "relevance": float}, ...]
    # Not List[str] — specs usually expect richer objects


def test_trend_fetcher_interface_exists():
    """
    This test fails until the fetch_trends function is defined in the module.
    It checks both module presence and the expected function signature.
    """
    try:
        from skills.skill_trend_fetcher import fetch_trends
    except ImportError:
        pytest.fail("skills/skill_trend_fetcher module is missing")
    except AttributeError:
        pytest.fail("fetch_trends function is not defined in skill_trend_fetcher")

    # Basic signature check (without calling — calling would require impl)
    assert callable(fetch_trends), "fetch_trends must be a callable function"


def test_trend_fetcher_contract_validation():
    """
    This test is meant to fail until a real implementation exists.
    It tries to call the function and validate output against Pydantic schema.
    """
    from skills.skill_trend_fetcher import fetch_trends, TrendInput, TrendOutput

    input_data = TrendInput(query="fashion Ethiopia")

    try:
        output = fetch_trends(input_data)
        assert isinstance(
            output, TrendOutput
        ), "Output must validate as TrendOutput Pydantic model"
        assert isinstance(output.trends, list), "trends field must be a list"
        assert len(output.trends) > 0, "Must return at least one trend item"
        # Optional: check first item has expected keys (expand later)
        if output.trends:
            assert "topic" in output.trends[0], "Each trend should have 'topic' key"
    except Exception as e:
        pytest.fail(
            f"Calling fetch_trends failed — implementation missing or broken: {str(e)}"
        )
