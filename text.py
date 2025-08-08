# with open("data.txt", "r+") as file:
#     lines = file.readlines()


# with open ("data.txt", "w") as file:
#     file.write("This is new line. /n")
#     print(lines)

# with open("data.txt", "r+") as file, open ("outfile.txt", "w") as outfile:
#     data =file.read()
#     outfile.write(data)
#     print(data)

with open("data.txt", "r+") as file, open ("outfile.txt", "w") as outfile:
    data =file.read()
    outfile.write(data.upper())
    print(data)

import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def make_connection(name):
    print(f"Connecting...{name}")
    yield name
    print (f"Connected! {name}")

async def main():
    async with make_connection("A") as a:
        print (f"Using connection: {a}")

asyncio.run(main())