import aiohttp
import asyncio
from fake_useragent import UserAgent
from tqdm import tqdm

link = input("Enter the link: ")
amount_request = int(input("Enter the amount of requests: "))

ua = UserAgent()
REQUEST_INTERVAL = 1

success_count = 0

async def send_request(session, progress_bar):
    global success_count
    try:
        headers = {'User-Agent': ua.random}
        async with session.post(link, headers=headers) as response:
            response.raise_for_status()
            success_count += 1
            progress_bar.update(1)
    except aiohttp.ClientError as e:
        print(f"Error: {e}")
        await asyncio.sleep(2)

async def main():
    async with aiohttp.ClientSession() as session:
        with tqdm(total=amount_request, desc="Sending Requests", unit="req") as progress_bar:
            tasks = [send_request(session, progress_bar) for _ in range(amount_request)]
            await asyncio.gather(*tasks)

asyncio.run(main())

print(f"\nSuccessfully sent {success_count} out of {amount_request} requests.")
