import asyncio
async def get_connection(name):
    class ctx():
        async def __aenter__(self):
            print (f"Enter...{name}")
            return name
        async def __aexit__(self, ec_type, exc, tb):
            print(f"Exit...{name}")
    return ctx()

async def main():
    async with await get_connection("A") as a:
        async with await get_connection("B") as b:
         print (f"Using Connection: {a} and {b}")

asyncio.run(main())