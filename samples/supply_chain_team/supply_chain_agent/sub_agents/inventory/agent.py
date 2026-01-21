from google.adk.agents import LlmAgent
from toolbox_core import ToolboxSyncClient

GEMINI_2_5_FLASH = "gemini-2.5-flash"

toolbox = ToolboxSyncClient("http://localhost:5000")
tools = toolbox.load_toolset("inventory_toolset")

inventory_agent = LlmAgent(
    name="InventoryAgent",
    model=GEMINI_2_5_FLASH,
    description=("Agent to search for inventory items by name or ID, and retrieve full details about them."),
    instruction="""
You are an inventory management agent. Your role is to provide accurate and up-to-date information about inventory items in response to user queries.
You have tools to search for items by name or ID.
You also have a `calculate_order_cost` tool to calculate the total cost of an order based on item prices and quantities.
""",
    tools=tools,
)