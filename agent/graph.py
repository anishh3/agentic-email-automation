from langgraph.graph import StateGraph, END
from agent.state import AgentState
import json
from agent.prompts import INTENT_PROMPT, RISK_PROMPT
from agent.llm import get_llm
from agent.llm import safe_json_loads
# -------- STATES -------- #
llm = get_llm()

def ingest_email(state: AgentState):
    print("\n[INGEST]")
    print(state.email_text)
    return state


def classify_intent(state: AgentState):
    print("\n[CLASSIFY INTENT - LLM]")

    response = llm.invoke(
        INTENT_PROMPT.format(email=state.email_text)
    )

    # ✅ ADD THIS BLOCK HERE ⬇️
    if hasattr(response, "content"):
        response = response.content

    print("\n[RAW INTENT RESPONSE]")
    print(response)
    # ✅ ADD THIS BLOCK HERE ⬆️

    data = safe_json_loads(response)
    state.intent = data["intent"]
    state.confidence = data["confidence"]

    print("Intent:", state.intent)
    print("Confidence:", state.confidence)

    return state





def assess_risk(state: AgentState):
    print("\n[ASSESS RISK - LLM]")

    response = llm.invoke(
        RISK_PROMPT.format(email=state.email_text)
    )

    if hasattr(response, "content"):
        response = response.content

    print("\n[RAW RISK RESPONSE]")
    print(response)
    K

    data = safe_json_loads(response)
    state.risk_level = data["risk_level"]

    print("Risk:", state.risk_level)
    print("Reason:", data.get("reason"))

    return state





def decide_action(state: AgentState):
    print("\n[DECIDE]")

    if state.risk_level == "HIGH":
        state.decision = "HUMAN_REVIEW"

    elif state.intent == "TASK_CREATION" and state.confidence >= 0.8:
        state.decision = "AUTO_EXECUTE"

    else:
        state.decision = "NO_ACTION"

    print("Decision:", state.decision)
    return state


# def select_tool(state: AgentState):
#     print("\n[SELECT TOOL]")

#     if state.decision == "AUTO_EXECUTE" and state.intent == "TASK_CREATION":
#         state.tool_name = "create_task"
#         state.tool_payload = {
#             "title": "Follow up on invoice",
#             "description": state.email_text
#         }
#     else:
#         state.tool_name = None
#         state.tool_payload = None

#     print("Tool:", state.tool_name)
#     return state
# from agent.tools import call_tool

# def execute_tool(state: AgentState):
#     print("\n[EXECUTE TOOL]")

#     if not state.tool_name:
#         state.tool_result = "No tool executed"
#         return state

#     try:
#         result = call_tool(state.tool_name, state.tool_payload)
#         state.tool_result = result
#     except Exception as e:
#         state.tool_result = f"Tool execution failed: {e}"

#     print("Result:", state.tool_result)
#     return state

# -------- GRAPH -------- #

# builder = StateGraph(AgentState)

# builder.add_node("ingest", ingest_email)
# builder.add_node("classify", classify_intent)
# builder.add_node("risk", assess_risk)
# builder.add_node("decide", decide_action)

# builder.set_entry_point("ingest")

# builder.add_edge("ingest", "classify")
# builder.add_edge("classify", "risk")
# builder.add_edge("risk", "decide")
# builder.add_edge("decide", END)

# builder.add_node("select_tool", select_tool)
# builder.add_node("execute_tool", execute_tool)

# builder.add_edge("decide", "select_tool")
# builder.add_edge("select_tool", "execute_tool")
# builder.add_edge("execute_tool", END)


# graph = builder.compile()
builder = StateGraph(AgentState)

builder.add_node("ingest", ingest_email)
builder.add_node("classify", classify_intent)
builder.add_node("risk", assess_risk)
builder.add_node("decide", decide_action)

builder.set_entry_point("ingest")

builder.add_edge("ingest", "classify")
builder.add_edge("classify", "risk")
builder.add_edge("risk", "decide")
builder.add_edge("decide", END)

graph = builder.compile()



# if __name__ == "__main__":
#     with open("examples/email.txt") as f:
#         email = f.read()

#     final_state = graph.invoke(
#         AgentState(email_text=email)
#     )

#     print("\n✅ FINAL STATE")
#     print(final_state)
