import aiohttp
import asyncio

url = 'https://visitcount.itsvg.in/api?id=Robobo2022&icon=0&color=0'

async def send_request(session):
    async with session.get(url) as response:
        if response.status == 200:
            print(f"\rRequest sent")
        elif response.status == 429:
            print("\rRate limited, waiting and retrying...", end='')
            await asyncio.sleep(60)
        else:
            print(f"\rError {response.status} occurred", end='')

async def send_requests(num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_requests):
            task = asyncio.ensure_future(send_request(session))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    num_requests = 2000
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_requests(num_requests))
