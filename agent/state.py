from typing import Optional
from pydantic import BaseModel


class AgentState(BaseModel):
    # Input
    email_text: str

    # Understanding
    intent: Optional[str] = None
    confidence: Optional[float] = None

    # Risk & policy
    risk_level: Optional[str] = None

    # Final decision
    decision: Optional[str] = None
