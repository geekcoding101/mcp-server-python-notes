import asyncio

from mcp import Client, StdioServerParameters


async def main():
    server = StdioServerParameters(command="uv", args=["run", "server.py"])
    async with Client(server) as client:
        tools = await client.list_tools()
        print("tools:", [t.name for t in tools.tools])

        saved = await client.call_tool("add_note", {"title": "mcp", "body": "MCP connects AI apps to tools."})
        print(saved.content[0].text)

        found = await client.call_tool("search_notes", {"query": "tools"})
        print(found.structured_content)

        note = await client.read_resource("notes://mcp")
        print("resource:", note.contents[0].text)

        prompt = await client.get_prompt("summarize_note", {"title": "mcp"})
        print("prompt:", prompt.messages[0].content.text)


asyncio.run(main())
