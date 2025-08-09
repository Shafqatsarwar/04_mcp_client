from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
import asyncio
from contextlib import AsyncExitStack

class MCPClient:
    def __init__(self, url):
        self.session = ClientSession(url)
        self.stack = AsyncExitStack()
    async def list_tools(self):
        async with self.session as session:
            response = (await session.list_tools()).tools
            return response
    async def __aenter__(self):
        read, write, _ = await self.stack.enter_async_context(
            streamablehttp_client(self.url)
        )
        
async def main():
    async with MCPClient("http://localhost:8000/mcp") as client:
        tools = await client.list_tools()
        for tool in tools:
            print(tool)

asyncio.run(main())

# Chat GPT 5
# from mcp.client.streamable_http import streamable_http_client
# from mcp import ClientSession
# import asyncio
# from contextlib import AsyncExitStack

# class MCPClient:
#     def __init__(self, url):
#         self.url = url
#         self.session = ClientSession(url)
#         self.stack = AsyncExitStack()

#     async def list_tools(self):
#         async with self.session as session:
#             response = (await session.list_tools()).tools
#             return response

#     async def __aenter__(self):
#         read, write, _ = await self.stack.enter_async_context(
#             streamable_http_client(self.url)
#         )
#         return self

#     async def __aexit__(self, exc_type, exc, tb):
#         await self.stack.aclose()

# async def main():
#     async with MCPClient("http://localhost:8000/mcp") as client:
#         tools = await client.list_tools()
#         for tool in tools:
#             print(tool)

# asyncio.run(main())


# import requests
# URL = "http://localhost:8000/mcp"
# PAYLOAD = {
#     "jsonrpc": "2.0",
#     "method": "tools/list",
#     "params": {},
#     "id": 1
# }
# HEADERS = {
#     "Content-Type": "application/json",
#     "Accept": "application/json, text/event-stream"     
# }

# response = requests.post(URL, json = PAYLOAD, headers = HEADERS, stream = True)

# for line in response.iter_lines():
#     if line:
#         print (line.decode("utf-8"))
#         # Process the line as needed
