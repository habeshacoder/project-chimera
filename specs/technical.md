Markdown# Technical Specifications

## API Contracts (Pydantic Schemas)

Example: Task Payload (JSON)

```python
from pydantic import BaseModel, UUID4
from datetime import datetime

class AgentTask(BaseModel):
    task_id: UUID4
    task_type: str  # e.g., "generate_content"
    priority: str  # "high|medium|low"
    context: dict  # {"goal": str, "persona_constraints": list[str]}
    assigned_worker_id: str
    created_at: datetime
    status: str  # "pending|in_progress|review|complete"
```

Database Schema (ERD in Mermaid)
#mermaid-diagram-mermaid-l0rwynu{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#000000;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-diagram-mermaid-l0rwynu .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-diagram-mermaid-l0rwynu .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-diagram-mermaid-l0rwynu .error-icon{fill:#552222;}#mermaid-diagram-mermaid-l0rwynu .error-text{fill:#552222;stroke:#552222;}#mermaid-diagram-mermaid-l0rwynu .edge-thickness-normal{stroke-width:1px;}#mermaid-diagram-mermaid-l0rwynu .edge-thickness-thick{stroke-width:3.5px;}#mermaid-diagram-mermaid-l0rwynu .edge-pattern-solid{stroke-dasharray:0;}#mermaid-diagram-mermaid-l0rwynu .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-diagram-mermaid-l0rwynu .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-diagram-mermaid-l0rwynu .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-diagram-mermaid-l0rwynu .marker{fill:#666;stroke:#666;}#mermaid-diagram-mermaid-l0rwynu .marker.cross{stroke:#666;}#mermaid-diagram-mermaid-l0rwynu svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-diagram-mermaid-l0rwynu p{margin:0;}#mermaid-diagram-mermaid-l0rwynu .entityBox{fill:#eee;stroke:#999;}#mermaid-diagram-mermaid-l0rwynu .relationshipLabelBox{fill:hsl(-160, 0%, 93.3333333333%);opacity:0.7;background-color:hsl(-160, 0%, 93.3333333333%);}#mermaid-diagram-mermaid-l0rwynu .relationshipLabelBox rect{opacity:0.5;}#mermaid-diagram-mermaid-l0rwynu .labelBkg{background-color:rgba(237.9999999999, 237.9999999999, 237.9999999999, 0.5);}#mermaid-diagram-mermaid-l0rwynu .edgeLabel .label{fill:#999;font-size:14px;}#mermaid-diagram-mermaid-l0rwynu .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#000000;}#mermaid-diagram-mermaid-l0rwynu .edge-pattern-dashed{stroke-dasharray:8,8;}#mermaid-diagram-mermaid-l0rwynu .node rect,#mermaid-diagram-mermaid-l0rwynu .node circle,#mermaid-diagram-mermaid-l0rwynu .node ellipse,#mermaid-diagram-mermaid-l0rwynu .node polygon{fill:#eee;stroke:#999;stroke-width:1px;}#mermaid-diagram-mermaid-l0rwynu .relationshipLine{stroke:#666;stroke-width:1;fill:none;}#mermaid-diagram-mermaid-l0rwynu .marker{fill:none!important;stroke:#666!important;stroke-width:1;}#mermaid-diagram-mermaid-l0rwynu :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}#mermaid-diagram-mermaid-l0rwynu p{margin:0;}assignsownsAGENTuuididstrnamestrwallet_addressstrpersona_soul_md_hashTASKuuididstrtypefloatconfidence_scoredatetimecreated_atstrstatusTRANSACTIONuuididfloatamount_usdcstrto_addressboolapproved

## MCP Tool Example

JSON{
"name": "post_content",
"description": "Publishes to social platform",
"inputSchema": {
"type": "object",
"properties": {
"platform": {"type": "string", "enum": ["twitter", "instagram"]},
"text": {"type": "string"},
"media_urls": {"type": "array", "items": {"type": "string"}}
}
}
}

# Technical Specification

Architecture, APIs, data models, and implementation notes.
