import pytest
import importlib
from pydantic import BaseModel
from typing import Literal


class ContentInput(BaseModel):
    type: Literal["text", "image", "video"]
    prompt: str
    persona_id: str


class ContentOutput(BaseModel):
    artifact_url: str
    confidence: float


def test_content_generator_module_exists():
    """Test MUST fail until skills/skill_content_generator module exists."""
    try:
        importlib.import_module("skills.skill_content_generator")
        module_exists = True
    except ImportError:
        module_exists = False

    assert module_exists, (
        "skills/skill_content_generator module is missing. "
        "Create the directory and implementation as per specs."
    )


def test_content_generator_interface_exists():
    """Test MUST fail until generate_content function is defined."""
    try:
        from skills.skill_content_generator import generate_content
    except ImportError:
        pytest.fail("skills/skill_content_generator module is missing")
    except AttributeError:
        pytest.fail("generate_content function is not defined")

    assert callable(generate_content), "generate_content must be callable"


def test_content_generator_contract_validation():
    """Test MUST fail until implementation validates I/O contracts."""
    from skills.skill_content_generator import generate_content, ContentInput, ContentOutput

    input_data = ContentInput(
        type="text",
        prompt="Create a post about fashion in Ethiopia",
        persona_id="persona_001"
    )

    try:
        output = generate_content(input_data)
        assert isinstance(output, ContentOutput), "Output must validate as ContentOutput"
        assert isinstance(output.artifact_url, str), "artifact_url must be string"
        assert 0.0 <= output.confidence <= 1.0, "confidence must be between 0 and 1"
    except NotImplementedError:
        # Expected until implementation is complete
        pytest.fail("generate_content is not yet implemented - this is expected in TDD approach")
    except Exception as e:
        pytest.fail(f"Calling generate_content failed: {str(e)}")
