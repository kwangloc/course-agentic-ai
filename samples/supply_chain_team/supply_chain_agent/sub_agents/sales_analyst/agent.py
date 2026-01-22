from google.adk.agents import LlmAgent
from toolbox_core import ToolboxSyncClient

GEMINI_2_5_FLASH = "gemini-2.5-flash"

toolbox = ToolboxSyncClient("http://localhost:5000")
tools = toolbox.load_toolset("sales_toolset")

sales_analyst_agent = LlmAgent(
    name="SalesAnalystAgent",
    model=GEMINI_2_5_FLASH,
    description=(""),
    instruction="""
You are a sales data analyst for a car dealership.

Your job:
- Analyze historical sales data
- Identify demand trends
- Estimate short-term demand

Rules:
- Always base conclusions on provided sales data
- Respond with clear numeric estimates
- Output JSON only
""",
    tools=tools,
)