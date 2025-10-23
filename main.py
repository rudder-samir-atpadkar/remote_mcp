from fastmcp import FastMCP
import os

mcp = FastMCP(name="Calculator Remote MCP")

@mcp.tool
def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

@mcp.tool
def generte_number(a: int, b: int) -> int:
    """Generates a random number between a and b."""
    import random
    return random.randint(a, b)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)