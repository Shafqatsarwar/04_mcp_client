import asyncio
from contextlib import AsyncExitStack
async def get_connection(name):
    class ctx():
        async def __aenter__(self):
            print (f"Enter...{name}")
            return name
        async def __aexit__(self, ec_type, exc, tb):
            print(f"Exit...{name}")
    return ctx()

# async def main():
#     async with await get_connection("A") as a:
#         async with await get_connection("B") as b:
#          print (f"Using Connection: {a} and {b}")

async def main():
    async with AsyncExitStack() as stack:
        a = await stack.enter_async_context(await get_connection("A"))
        if a == "A":
            b = await stack.enter_async_context(await get_connection("B"))
            print (f"Using Connection: {a} and {b}")

    async def customCleanup():
        print ("Custom cleanup Logic here")

    stack.push_async_callback(customCleanup)
    print(f"Doing work with {a} and maybe {locals().get('b')}")

asyncio.run(main())