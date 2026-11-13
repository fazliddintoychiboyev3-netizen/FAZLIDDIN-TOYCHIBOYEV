import os
from mcp.server.fastmcp import FastMCP

app = FastMCP(
    "AI Reels Studio",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000))
)

@app.tool()
def create_reel_plan(topic: str, style: str = "Instagram trend") -> str:
    """Create a short Instagram Reels video plan."""
    return f"""
    Create an Instagram Reel about: {topic}

    Style: {style}
    Format: Vertical 9:16
    Resolution: 1080x1920

    Include:
    - Attention-grabbing opening
    - Scene-by-scene storyboard
    - Music and sound suggestions
    - Editing and transition suggestions
    - Final video generation prompt
    """

if __name__ == "__main__":
    app.run(transport="streamable-http")
