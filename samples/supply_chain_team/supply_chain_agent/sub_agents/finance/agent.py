from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

finance_agent = RemoteA2aAgent(
    name="FinanceAgent",
    description="Handles financial approvals for expenditures.",
    agent_card=f"http://localhost:8001/{AGENT_CARD_WELL_KNOWN_PATH}",
)
