# from langchain.chat_models import ChatOpenAI
from langchain_openai import OpenAI
from dotenv import load_dotenv

import json
import re

import json
import re

def safe_json_loads(text: str) -> dict:
    """
    Extract and parse the FIRST valid JSON object from LLM output.
    Raises a clear error if parsing fails.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Fallback: extract first JSON object
    matches = re.findall(r"\{[\s\S]*?\}", text)

    if not matches:
        raise ValueError(f"No JSON object found in LLM output:\n{text}")

    for m in matches:
        try:
            return json.loads(m)
        except json.JSONDecodeError:
            continue

    raise ValueError(f"Could not parse JSON from LLM output:\n{text}")



load_dotenv()
def get_llm():
    return OpenAI(model="gpt-4o-mini")

