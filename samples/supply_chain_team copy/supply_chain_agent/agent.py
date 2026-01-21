from google.adk.agents import LlmAgent
from supply_chain_agent.sub_agents.inventory.agent import inventory_agent
from supply_chain_agent.sub_agents.finance.agent import finance_agent
from supply_chain_agent.sub_agents.logistics.agent import logistics_agent

GEMINI_2_5_FLASH = "gemini-2.5-flash"

root_agent = LlmAgent(
    name="OrchestratorAgent",
    model=GEMINI_2_5_FLASH,
    description="An orchestrator agent that manages supply chain operations by coordinating with inventory, finance, and logistics sub-agents.",
    instruction="""
You are a supply chain planner agent. Your goal is to answer user questions and fulfill requests related to supply chain management by coordinating with your sub-agents: InventoryAgent, FinanceAgent, and LogisticsAgent.

Here are your sub-agents and their roles:
1. InventoryAgent: Use this agent to get information about inventory, like item details, stock levels, and reorder status.
2. FinanceAgent: This agent handles financial approvals for expenditures. Use it to approve budgets and expenses.
3. LogisticsAgent: This agent manages shipping and delivery logistics. Use it to arrange shipments and track deliveries.

""",
    sub_agents=[
        inventory_agent,
        finance_agent,
        logistics_agent,
    ],
)