from model import LLM

def synthesizer_agent(state):
    combined_notes = "\n\n".join(state["research_notes"])

    prompt = f"""
You are a synthesis agent.

Combine the research notes into a coherent, structured draft.

Rules:
- Use headings
- Maintain factual accuracy
- Do NOT add new information
- No conclusions yet

Research Notes:
{combined_notes}
"""

    response = LLM.invoke(prompt)

    return {"draft": response.content}
