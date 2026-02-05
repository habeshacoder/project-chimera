text### skills/skill_content_generator/README.md

````markdown
# Skill: Content Generator

## Description

Generates text/image/video with consistency (LoRA ref).

## Input Contract

```python
class ContentInput(BaseModel):
    type: str  # "text|image|video"
    prompt: str
    persona_id: str
```
````

Output Contract
Pythonclass ContentOutput(BaseModel):
artifact_url: str
confidence: float

```
# Skill: Content Generator

Purpose: generate content pieces from structured inputs.
```
