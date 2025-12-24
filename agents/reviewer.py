from model import LLM
def reviewer_agent(state):
    prompt = f"""
You are a critical fact-checking reviewer.

Review the draft below.

Check for:
- Factual errors
- Hallucinations
- Missing critical points
- Overgeneralizations

Rules:
- Be strict
- Suggest improvements
- If no issues, say "No major issues found"

Draft:
{state['draft']}
"""

    response = LLM.invoke(prompt)

    return {"review_feedback": response.content}
