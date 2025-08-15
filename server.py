from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="FastMCP", stateless_http=True)

docs = {
    "intro": "This is a simple example document of MCP server.",
    "readme": "This is the README document for FastMCP.",
    "guide": "This is the guide document for FastMCP.",
}

@mcp.resource("docs://documents", mime_type="application/json")
def list_docs():
    """List available documents."""
    return list(docs.keys())

print("Available Documents:", list_docs())

@mcp.resource("docs://documents/{doc_name}", mime_type="application/json")
def read_docs(doc_name: str):
    """Read a specific document."""
    if doc_name in docs:
        return {"name": doc_name, "content": docs[doc_name]}
    else:
        raise mcp.ResourceNotFound(f"Document '{doc_name}' not found.")

mcp_server = mcp.streamable_http_app()
