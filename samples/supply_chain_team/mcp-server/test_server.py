import asyncio

from fastmcp import Client


async def test_server():
    # Test the MCP server using streamable-http transport.
    # Use "/sse" endpoint if using sse transport.
    async with Client("http://localhost:8080/mcp") as client:
        # List available tools
        tools = await client.list_tools()
        for tool in tools:
            print(f"--- 🛠️  Tool found: {tool.name} ---")
        
        # print("--- 🪛  Calling get_historical_sales tool ---")
        # result = await client.call_tool(
        #     "get_historical_sales", {"product_id": "Camry", "start_date": "2025-11-01", "end_date": "2025-11-05"}
        # )
        # print(f"--- ✅  Success: {result.content[0].text} ---")

        print("--- 🪛  Calling get_inventory_levels tool ---")
        result = await client.call_tool(
            "get_inventory_levels", {"product_id": "Camry"}
        )
        print(f"--- ✅  Success: {result.content[0].text} ---")

if __name__ == "__main__":
    asyncio.run(test_server())
