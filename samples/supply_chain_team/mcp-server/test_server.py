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

        # Call get_exchange_rate tool
        print("--- 🪛  Calling get_stock_status tool ---")
        result = await client.call_tool(
            "get_stock_status", {}
        )
        print(f"--- ✅  Success: {result.content[0].text} ---")

        # Call get_product_stock tool
        print("--- 🪛  Calling get_product_stock tool ---")
        result = await client.call_tool(
            "get_product_stock", {"product_name": "Toyota Camry"}
        )
        print(f"--- ✅  Success: {result.content[0].text} ---")


if __name__ == "__main__":
    asyncio.run(test_server())
