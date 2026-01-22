from google.adk.agents import LlmAgent
from .tool import find_shipping_options, execute_shipment

GEMINI_2_5_FLASH = "gemini-2.5-flash"

supplier_agent = LlmAgent(
    name="SupplierAgent",
    model=GEMINI_2_5_FLASH,
    description=("Manages shipping and logistics to find replenishment options."),
    instruction="""
You are a logistics and shipping coordinator.
Your goal is to find and present the best shipping options to solve supply chain issues.
When asked to execute a shipment, you must have a financial approval.
You have two tools: `find_shipping_options` and `execute_shipment`.
""",
    tools=[find_shipping_options, execute_shipment],
)