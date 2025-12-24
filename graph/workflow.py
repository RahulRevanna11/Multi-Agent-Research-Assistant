from langgraph.graph import StateGraph
from state import ResearchState

from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.synthesizer import synthesizer_agent
from agents.reviewer import reviewer_agent
from agents.final_answer import final_answer_agent

graph = StateGraph(ResearchState)

graph.add_node("planner", planner_agent)
graph.add_node("researcher", research_agent)
graph.add_node("synthesizer", synthesizer_agent)
graph.add_node("reviewer", reviewer_agent)
graph.add_node("final", final_answer_agent)

graph.set_entry_point("planner")

graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "synthesizer")
graph.add_edge("synthesizer", "reviewer")
graph.add_edge("reviewer", "final")

graph.set_finish_point("final")

app = graph.compile()
