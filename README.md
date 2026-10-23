# mcp-server-python-notes

A tiny MCP server (Python SDK 2.x, `MCPServer`) that gives an AI assistant a personal notes folder: two tools (`add_note`, `search_notes`), one resource template (`notes://{title}`) and one prompt (`summarize_note`). Plus a Python client that exercises all of them over stdio.

Code from the article: **[What Is an MCP Server? How to Build One in Python](https://geekcoding101.com/posts/what-is-an-mcp-server)**

## Run

```bash
uv sync
uv run client.py          # starts server.py as a subprocess and calls every primitive
uv run mcp dev server.py  # optional: MCP Inspector web UI
```

Connect it to Claude Code:

```bash
claude mcp add notes -- uv run --directory /absolute/path/to/mcp-server-python-notes server.py
```

Notes are stored as Markdown files in `~/mcp-notes`. No API keys needed. As the article says, the demo builds paths from the note title without validation; reject `../` titles before using this for anything real.
