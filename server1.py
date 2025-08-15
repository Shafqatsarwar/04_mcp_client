from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="FastMCP", stateless_http=True)

docs = {
    "intro": "This a simple example document of MCP server.",
    "readme": "This is the README document for FastMCP.",
    "guide": "This is the guide document for FastMCP.",
}

@mcp.resources("docs://documents", mime_type="application/json")
def list_docs():
    """ List available documents. """
    return {"documents": list(docs.keys())}  # Return as a dict for clarity

mcp_server = mcp.streamable_http_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:mcp_server", host="127.0.0.1", port=8000, reload=True)