from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    """Use this tool to greet a person by name.

    Args:
        name: The name of the person to greet.
    
    Returns:
        A greeting message.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()