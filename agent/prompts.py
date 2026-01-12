INTENT_PROMPT = """
Return ONLY valid JSON. No explanation. No markdown.

Email:
{email}

JSON schema:
{{
  "intent": "TASK_CREATION | OTHER",
  "confidence": number
}}
"""

RISK_PROMPT = """
You are a risk classifier.

Given the email below, output ONLY valid JSON.

Email:
{email}

Return ONLY this JSON schema:
{{
  "risk_level": "LOW | MEDIUM | HIGH",
  "reason": "short explanation"
}}

DO NOT include any text before or after the JSON.
"""

