import asyncio
import logging
import os

from fastmcp import FastMCP
from pydantic import BaseModel
from typing import List, Optional

# import mock data
from mock_data import SALES_HISTORY, INVENTORY_LEVELS, SUPPLIERS, PRICING, LEAD_TIMES

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP(name="Car Store Supply Chain MCP 🛠️")

class SalesRecord(BaseModel):
    product_id: str
    date: str
    units: int

class InventoryLocation(BaseModel):
    product_id: str
    location_id: str
    on_hand: int
    reserved: int
    available: int

class SupplierInfo(BaseModel):
    supplier_id: str
    name: str
    region: str
    rating: float

class PricingInfo(BaseModel):
    supplier_id: str
    product_id: str
    unit_price: float
    currency: str
    min_order_qty: int

class LeadTimeInfo(BaseModel):
    supplier_id: str
    product_id: str
    lead_time_days: float
    on_time_delivery_pct: float

# --- Tools using imported mock data ---

@mcp.tool()
def get_historical_sales(product_id: str, start_date: str, end_date: str) -> List[SalesRecord]:
    logger.info(f"Called get_historical_sales({product_id}, {start_date}, {end_date})")
    return [SalesRecord(**rec) for rec in SALES_HISTORY if rec["product_id"] == product_id and start_date <= rec["date"] <= end_date]

@mcp.tool()
def get_inventory_levels(product_id: str) -> List[InventoryLocation]:
    logger.info(f"Called get_inventory_levels({product_id})")
    return [InventoryLocation(**loc) for loc in INVENTORY_LEVELS if loc["product_id"] == product_id]

@mcp.tool()
def get_supplier_list(max_results: int = 10) -> List[SupplierInfo]:
    logger.info(f"Called get_supplier_list")
    return [SupplierInfo(**sup) for sup in SUPPLIERS[:max_results]]

@mcp.tool()
def get_supplier_pricing(supplier_id: str, product_id: str) -> Optional[PricingInfo]:
    logger.info(f"Called get_supplier_pricing({supplier_id}, {product_id})")
    for p in PRICING:
        if p["supplier_id"] == supplier_id and p["product_id"] == product_id:
            return PricingInfo(**p)
    return None

@mcp.tool()
def get_lead_time_info(supplier_id: str, product_id: str) -> Optional[LeadTimeInfo]:
    logger.info(f"Called get_lead_time_info({supplier_id},{product_id})")
    for l in LEAD_TIMES:
        if l["supplier_id"] == supplier_id and l["product_id"] == product_id:
            return LeadTimeInfo(**l)
    return None

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
