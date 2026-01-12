from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToolRequest(BaseModel):
    tool: str
    args: dict

@app.post("/execute")
def execute_tool(req: ToolRequest):
    if req.tool == "create_task":
        # In real life: forward to n8n webhook
        return {
            "status": "success",
            "message": f"Task created: {req.args.get('title')}"
        }

    return {"status": "error", "message": "Unknown tool"}
