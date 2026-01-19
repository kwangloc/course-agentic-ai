import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        # List available tools
        tools = await client.list_tools()
        print(tools)
        # for tool in tools:
        #     print(f"--- 🛠️  Tool found: {tool.name} ---")
        

        # Call greet tool
        result = await client.call_tool("greet", {"name": name})
        print(result.structured_content['result'])

asyncio.run(call_tool("Ford"))