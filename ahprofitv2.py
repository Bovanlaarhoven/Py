import re
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
import subprocess
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer
import time

import pandas as pd
import requests

from plyer import notification
import asyncio
import aiohttp

c = requests.get("https://api.hypixel.net/skyblock/auctions?page=0")
resp = c.json()
now = resp['lastUpdated']
toppage = resp['totalPages']

results = []
prices = {}

# stuff to remove
REFORGES = [" ✦", "⚚ ", " ✪", "✪", "Stiff ", "Lucky ", "Jerry's ", "Dirty ", "Fabled ", "Suspicious ", "Gilded ", "Warped ",
            "Withered ", "Bulky ", "Stellar ", "Heated ", "Ambered ", "Fruitful ", "Magnetic ", "Fleet ", "Mithraic ",
            "Auspicious ", "Refined ", "Headstrong ", "Precise ", "Spiritual ", "Moil ", "Blessed ", "Toil ", "Bountiful ",
            "Candied ", "Submerged ", "Reinforced ", "Cubic ", "Warped ", "Undead ", "Ridiculous ", "Necrotic ", "Spiked ",
            "Jaded ", "Loving ", "Perfect ", "Renowned ", "Giant ", "Empowered ", "Ancient ", "Sweet ", "Silky ", "Bloody ",
            "Shaded ", "Gentle ", "Odd ", "Fast ", "Fair ", "Epic ", "Sharp ", "Heroic ", "Spicy ", "Legendary ", "Deadly ",
            "Fine ", "Grand ", "Hasty ", "Neat ", "Rapid ", "Unreal ", "Awkward ", "Rich ", "Clean ", "Fierce ", "Heavy ",
            "Light ", "Mythic ", "Pure ", "Smart ", "Titanic ", "Wise ", "Bizarre ", "Itchy ", "Ominous ", "Pleasant ",
            "Pretty ", "Shiny ", "Simple ", "Strange ", "Vivid ", "Godly ", "Demonic ", "Forceful ", "Hurtful ", "Keen ",
            "Strong ", "Superior ", "Unpleasant ", "Zealous "]

# Constant for the lowest priced item you want to be shown to you; feel free to change this
LOWEST_PRICE = 5

# Constant to turn on/off desktop notifications
NOTIFY = False

# Constant for the lowest percent difference you want to be shown to you; feel free to change this
LOWEST_PERCENT_MARGIN = 1 / 2

START_TIME = default_timer()

async def fetch(session, page):
    global toppage
    base_url = "https://api.hypixel.net/skyblock/auctions?page="
    async with session.get(base_url + page) as response:
        # puts response in a dict
        data = await response.json()
        toppage = data['totalPages']
        if data['success']:
            toppage = data['totalPages']
            for auction in data['auctions']:
                if not auction['claimed'] and auction['bin'] == True and not "Furniture" in auction[
                    "item_lore"]:  # if the auction isn't a) claimed and b) not a BIN, then continue
                    index = auction['item_name']
                    for r in REFORGES:
                        index = index.replace(r, "")
                    if index not in prices:
                        prices[index] = auction['starting_bid']
                    else:
                        prices[index] += auction['starting_bid']


async def get_data_asynchronous():
    tasks = []
    pages = list(range(0, toppage))
    async with aiohttp.ClientSession() as session:
        for page in pages:
            task = asyncio.ensure_future(fetch(session, str(page)))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)

        if prices:
            for index in prices:
                price = prices[index]
                average = price / toppage
                margin = round(price / average, 3)
                if margin > LOWEST_PERCENT_MARGIN and price > LOWEST_PRICE:
                    results.append((index, price, margin))
            results.sort(key=lambda x: x[1])
            for result in results:
                if result[1] < 500000:
                    message = "Lowest BIN: {:,}\nSecond Lowest: {:,}".format(result[0][2], result[1])
                    if NOTIFY:
                        notification.notify(
                            title="AH Notification",
                            message=message,
                            timeout=5,
                        )
                    else:
                        print(message)


async def main():
    async with aiohttp.ClientSession() as session:
        await get_data_asynchronous()

if __name__ == '__main__':
    asyncio.run(main())
