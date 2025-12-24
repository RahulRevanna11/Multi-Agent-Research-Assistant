from model import LLM

def final_answer_agent(state):
    prompt = f"""
You are a senior technical writer.

Improve the draft using the reviewer feedback.

Rules:
- Correct all issues
- Improve clarity
- Keep concise
- Provide a final, complete answer
- No mention of review process

Draft:
{state['draft']}

Reviewer Feedback:
{state['review_feedback']}
"""

    response = LLM.invoke(prompt)

    return {"final_answer": response.content}
