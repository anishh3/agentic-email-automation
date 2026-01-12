from fastapi import FastAPI
from pydantic import BaseModel

from agent.graph import graph
from agent.state import AgentState

app = FastAPI()


class EmailPayload(BaseModel):
    email_text: str


@app.post("/process-email")
def process_email(payload: EmailPayload):
    # Create initial agent state
    state = AgentState(email_text=payload.email_text)

    # Run LangGraph
    final_state = graph.invoke(state)

    # Return everything for now (debug-friendly)
    return final_state

