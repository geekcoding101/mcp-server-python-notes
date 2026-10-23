"""A tiny MCP server that gives an AI assistant a personal notes folder."""
from pathlib import Path

from mcp.server.mcpserver import MCPServer

NOTES_DIR = Path.home() / "mcp-notes"
NOTES_DIR.mkdir(exist_ok=True)

mcp = MCPServer("notes")


@mcp.tool()
def add_note(title: str, body: str) -> str:
    """Save a note. Overwrites a note with the same title."""
    path = NOTES_DIR / f"{title}.md"
    path.write_text(body, encoding="utf-8")
    return f"Saved {path.name}"


@mcp.tool()
def search_notes(query: str) -> list[str]:
    """Return the titles of notes whose title or body contains the query."""
    q = query.lower()
    return [
        p.stem
        for p in sorted(NOTES_DIR.glob("*.md"))
        if q in p.stem.lower() or q in p.read_text(encoding="utf-8").lower()
    ]


@mcp.resource("notes://{title}")
def read_note(title: str) -> str:
    """The full text of one note."""
    return (NOTES_DIR / f"{title}.md").read_text(encoding="utf-8")


@mcp.prompt()
def summarize_note(title: str) -> str:
    """Ask the model to summarize a note in three bullet points."""
    return f"Read the resource notes://{title} and summarize it in three bullet points."


if __name__ == "__main__":
    mcp.run()  # stdio transport by default
