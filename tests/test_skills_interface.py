import importlib


def test_trend_fetcher_module_exists():
    """
    This test MUST fail until skills/skill_trend_fetcher/__init__.py or .py file exists.
    It enforces that the skill directory structure is created per challenge instructions.
    """
    try:
        importlib.import_module("skills.skill_trend_fetcher")
        module_exists = True
    except ImportError:
        module_exists = False

    assert module_exists, (
        "skills/skill_trend_fetcher module is missing. "
        "Create the directory and README.md (or __init__.py) as per the challenge."
    )


def test_content_generator_module_exists():
    """
    This test MUST fail until the content generator skill is created.
    """
    try:
        importlib.import_module("skills.skill_content_generator")
        module_exists = True
    except ImportError:
        module_exists = False

    assert module_exists, (
        "skills/skill_content_generator module is missing. "
        "Create the directory and README.md with I/O contract as specified."
    )


def test_transaction_executor_module_exists():
    """
    This test MUST fail until the transaction skill is stubbed.
    """
    try:
        importlib.import_module("skills.skill_transaction_executor")
        module_exists = True
    except ImportError:
        module_exists = False

    assert module_exists, (
        "skills/skill_transaction_executor module is missing. "
        "This is required for Agentic Commerce per SRS."
    )
