import requests

MCP_SERVER_URL = "http://localhost:5678/webhook/create-task"

ALLOWED_TOOLS = {"create_task"}


def call_tool(tool_name: str, payload: dict) -> str:
    if tool_name not in ALLOWED_TOOLS:
        raise ValueError(f"Tool '{tool_name}' is not allowed")

    response = requests.post(
        MCP_SERVER_URL,
        json={
            "tool": tool_name,
            "args": payload
        },
        timeout=5
    )

    response.raise_for_status()
    return response.json().get("message", "ok")
