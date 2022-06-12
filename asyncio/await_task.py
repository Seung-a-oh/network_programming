import time, asyncio

async def add(a,b):
    print(f"add task start time: {time.strftime('%X')}")
    await asyncio.sleep(1)
    print(a+b)

async def mul(a,b):    
    print(f"mul task start time: {time.strftime('%X')}")
    await asyncio.sleep(2)
    print(a*b)

async def main():
    print(f"start time: {time.strftime('%X')}")
    task1 = asyncio.create_task(add(1,2))
    task2 = asyncio.create_task(mul(2,3))
    await task1
    await task2
    print(f"end time: {time.strftime('%X')}")

asyncio.run(main())