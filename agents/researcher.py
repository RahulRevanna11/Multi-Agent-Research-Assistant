from model import LLM

def research_agent(state):
    notes = []

    for step in state["plan"]:
        prompt = f"""
You are a professional research agent.

Research the task below using factual knowledge.
If information is uncertain, explicitly say so.

Rules:
- Be concise
- No speculation
- No opinions
- Use bullet points

Research Task:
{step}
"""
        response = LLM.invoke(prompt)
        notes.append(response.content)

    return {"research_notes": notes}
