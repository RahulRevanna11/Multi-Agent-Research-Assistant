from typing import TypedDict, List

class ResearchState(TypedDict):
    question: str
    plan: List[str]
    research_notes: List[str]
    draft: str
    review_feedback: str
    final_answer: str
