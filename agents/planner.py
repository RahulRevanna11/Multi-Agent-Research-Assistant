from model import LLM

def planner_agent(state):
    prompt = f"""
You are an expert research planner.

Your task:
- Break the user's question into 3 to 5 precise research tasks.
- Each task must be factual and verifiable.
- Avoid overlap between tasks.
- Do NOT answer the question.

Rules:
- Output ONLY a numbered list.
- No explanations.
- No extra text.

Question:
{state['question']}
"""

    response = LLM.invoke(prompt)

    steps = [
        line.strip()
        for line in response.content.split("\n")
        if line.strip()
    ]

    return {"plan": steps}
