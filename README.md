
# Agentic Email Automation System

A decision-driven AI agent that reads real Gmail messages, reasons about intent and risk, and safely triggers operational actions using workflow automation.

---

## 🚀 What this project does

This system automatically processes incoming emails and decides whether to take action — such as creating a follow-up task — without human intervention, while enforcing safety checks.

In simple terms:
> The agent **reads emails, understands what they mean, decides what to do, and acts only when it’s confident and safe.**

---

## 🧠 How it works (high level)

1. **Gmail Trigger (n8n)**
   - Listens for new incoming emails

2. **AI Decision Engine (LangGraph + LLM)**
   - Classifies the email intent
   - Estimates confidence in interpretation
   - Assesses operational risk
   - Makes a decision:
     - `AUTO_EXECUTE`
     - `HUMAN_REVIEW`
     - `NO_ACTION`

3. **Workflow Automation (n8n)**
   - Executes actions only when the decision is safe
   - Logs all decisions for auditability

---

## 🧩 Example Decision Output

```json
{
  "email_text": "Please follow up with the vendor regarding the pending invoice.",
  "intent": "TASK_CREATION",
  "confidence": 0.95,
  "risk_level": "LOW",
  "decision": "AUTO_EXECUTE"
}
