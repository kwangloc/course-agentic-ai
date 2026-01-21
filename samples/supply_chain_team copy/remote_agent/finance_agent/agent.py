import os 
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from remote_agent.finance_agent.tool import (
    get_approval_threshold, request_approval, finalize_approval
)

from google.adk.a2a.utils.agent_to_a2a import to_a2a

dotenv_path = os.path.join(os.path.dirname(__file__),".env")
load_dotenv(dotenv_path)

GEMINI_2_5_FLASH = "gemini-2.5-flash"

root_agent = LlmAgent(
    name="FinanceAgent",
    model=GEMINI_2_5_FLASH,
    description="Handles financial approvals for expenditures.",
    instruction="""
You are a finance agent responsible for managing financial approvals for expenditures.
Your goal is to review approval requests and make decisions based on the organization's financial policies.     
You have three tools at your disposal:
1. `get_approval_threshold`: Use this tool to retrieve the current approval threshold for expenditures.
2. `request_approval`: Use this tool to submit an approval request for a specific expenditure.
3. `finalize_approval`: Use this tool to finalize and record the decision on an approval request.
""",
    tools=[
        get_approval_threshold,
        request_approval,
        finalize_approval,
    ],
)

a2a_app = to_a2a(root_agent, port=8001)