import asyncio
import logging
import os

import httpx
from fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("Currency MCP Server 💵")


@mcp.tool()
def get_stock_status():
    """Use this to get the stock status of cars in the store.

    Returns:
        A dictionary containing mock stock data for various car models.
    """
    logger.info("--- 🛠️ Tool: get_stock_status called ---")
    
    # Mock data for car stock
    stock_data = {
        "Toyota Camry": {"available": 10, "price": 24000},
        "Honda Accord": {"available": 5, "price": 26000},
        "Ford Mustang": {"available": 3, "price": 30000},
        "Chevrolet Malibu": {"available": 7, "price": 22000},
    }
    
    return stock_data

@mcp.tool()
def get_product_stock(product_name):
    """Use this to get the stock status of a specific car model.

    Args:
        product_name (str): The name of the car model to check.

    Returns:
        A dictionary containing the stock status of the specified car model or a message if not found.
    """
    logger.info(f"--- 🛠️ Tool: get_product_stock called for {product_name} ---")
    
    stock_data = {
        "Toyota Camry": {"available": 10, "price": 24000},
        "Honda Accord": {"available": 5, "price": 26000},
        "Ford Mustang": {"available": 3, "price": 30000},
        "Chevrolet Malibu": {"available": 7, "price": 22000},
    }

    product_stock = stock_data.get(product_name)

    if product_stock:
        logger.info(f"✅ Stock data for {product_name}: {product_stock}")
        return product_stock
    else:
        logger.warning(f"❌ {product_name} not found in stock.")
        return {"message": f"{product_name} not found in stock."}

@mcp.tool()
def get_approval_threshold():
    """Use this to get the current approval threshold for expenditures.

    Returns:
        The current approval threshold as a float.
    """
    logger.info("--- 🛠️ Tool: get_approval_threshold called ---")
    # Mock approval threshold
    approval_threshold = 5000.00
    return approval_threshold

@mcp.tool()
def request_approval(amount, description):
    """Use this to submit an approval request for a specific expenditure.

    Args:
        amount (float): The amount of the expenditure.
        description (str): A brief description of the expenditure.
    Returns:
        A confirmation message indicating the approval request has been submitted.
    """
    logger.info(f"--- 🛠️ Tool: request_approval called for amount: {amount}, description: {description} ---")
    # Mock approval request submission
    return f"Approval request for ${amount} - '{description}' has been submitted."

@mcp.tool()
def finalize_approval(request_id, approved):
    """Use this to finalize and record the decision on an approval request.

    Args:
        request_id (str): The ID of the approval request.
        approved (bool): Whether the request was approved or not.

    Returns:
        A confirmation message indicating the decision has been recorded.
    """
    logger.info(f"--- 🛠️ Tool: finalize_approval called for request_id: {request_id}, approved: {approved} ---")
    # Mock finalization of approval
    decision = "approved" if approved else "denied"
    return f"Approval request {request_id} has been {decision}."

if __name__ == "__main__":
    logger.info(f"🚀 MCP server started on port {os.getenv('PORT', 8080)}")
    # Could also use 'sse' transport, host="0.0.0.0" required for Cloud Run.
    asyncio.run(
        mcp.run_async(
            transport="http",
            host="0.0.0.0",
            port=os.getenv("PORT", 8080),
        )
    )
