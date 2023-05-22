import asyncio
import re
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer
import time

import pandas as pd
import requests

from pync import Notifier

c = requests.get("https://api.hypixel.net/skyblock/auctions?page=0")
resp = c.json()
now = resp['lastUpdated']
toppage = resp['totalPages']

results = []
prices = {}

REFORGES = [" ✦", "⚚ ", " ✪", "✪", "Stiff ", "Lucky ", "Jerry's ", "Dirty ", "Fabled ", "Suspicious ", "Gilded ", "Warped ", "Withered ", "Bulky ", "Stellar ", "Heated ", "Ambered ", "Fruitful ", "Magnetic ", "Fleet ", "Mithraic ", "Auspicious ", "Refined ", "Headstrong ", "Precise ", "Spiritual ", "Moil ", "Blessed ", "Toil ", "Bountiful ", "Candied ", "Submerged ", "Reinforced ", "Cubic ", "Warped ", "Undead ", "Ridiculous ", "Necrotic ", "Spiked ", "Jaded ", "Loving ", "Perfect ", "Renowned ", "Giant ", "Empowered ", "Ancient ", "Sweet ", "Silky ", "Bloody ", "Shaded ", "Gentle ", "Odd ", "Fast ", "Fair ", "Epic ", "Sharp ", "Heroic ", "Spicy ", "Legendary ", "Deadly ", "Fine ", "Grand ", "Hasty ", "Neat ", "Rapid ", "Unreal ", "Awkward ", "Rich ", "Clean ", "Fierce ", "Heavy ", "Light ", "Mythic ", "Pure ", "Smart ", "Titanic ", "Wise ", "Bizarre ", "Itchy ", "Ominous ", "Pleasant ", "Pretty ", "Shiny ", "Simple ", "Strange ", "Vivid ", "Godly ", "Demonic ", "Forceful ", "Hurtful ", "Keen ", "Strong ", "Superior ", "Unpleasant ", "Zealous "]

LOWEST_PRICE = 5
NOTIFY = True
LOWEST_PERCENT_MARGIN = 1/2

START_TIME = default_timer()

def fetch(session, page):
    global toppage
    base_url = "https://api.hypixel.net/skyblock/auctions?page="
    with session.get(base_url + page) as response:
        data = response.json()
        toppage = data['totalPages']
        if data['success']:
            toppage = data['totalPages']
            for auction in data['auctions']:
                if not auction['claimed'] and auction['bin'] == True and not "Furniture" in auction["item_lore"]:
                    index = re.sub("\[[^\]]*\]", "", auction['item_name']) + auction['tier']
                    for reforge in REFORGES: index = index.replace(reforge, "")
                    if index in prices:
                        if prices[index][0] > auction['starting_bid']:
                            prices[index][1] = prices[index][0]
                            prices[index][0] = auction['starting_bid']
                        elif prices[index][1] > auction['starting_bid']:
                            prices[index][1] = auction['starting_bid']
                    else:
                        prices[index] = [auction['starting_bid'], float("inf")]
                        
                    if prices[index][1] > LOWEST_PRICE and prices[index][0]/prices[index][1] < LOWEST_PERCENT_MARGIN and auction['start']+60000 > now:
                        results.append([auction['uuid'], auction['item_name'], auction['starting_bid'], index])
        return data

async def get_data_asynchronous():
    pages = [str(x) for x in range(toppage)]
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            loop = asyncio.get_event_loop()
            START_TIME = default_timer()
            tasks = [
                loop.run_in_executor(
                    executor,
                    fetch,
                    *(session, page)
                )
                for page in pages if int(page) < toppage
            ]
            for response in await asyncio.gather(*tasks):
                pass

def main():
    global results, prices, START_TIME
    START_TIME = default_timer()
    results = []
    prices = {}
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    future = asyncio.ensure_future(get_data_asynchronous())
    loop.run_until_complete(future)
    
    if len(results): results = [[entry, prices[entry[3]][1]] for entry in results if (entry[2] > LOWEST_PRICE and prices[entry[3]][1] != float('inf') and prices[entry[3]][0] == entry[2] and prices[entry[3]][0]/prices[entry[3]][1] < LOWEST_PERCENT_MARGIN)]
    
    if len(results):

        if NOTIFY:
            lowest_bin = max(results, key=lambda entry: entry[1])[0][2]
            second_lowest = max(results, key=lambda entry: entry[1])[1]

            notification_title = f"2e LBIN: {second_lowest:,}"
            notification_subtitle = f"LBIN: {lowest_bin:,}"

            Notifier.notify(
                notification_title,
                title=max(results, key=lambda entry: entry[1])[0][1],
                subtitle=notification_subtitle,
                sound='default',
            )

        df = pd.DataFrame(['/viewauction ' + str(max(results, key=lambda entry: entry[1])[0][0])])
        df.to_clipboard(index=False, header=False)
        
        done = default_timer() - START_TIME
        play_sound()
        for result in results:
            print("Auction UUID: " + str(result[0][0]) + " | Item Name: " + str(result[0][1]) + " | Item price: {:,}".format(result[0][2]), " | Second lowest BIN: {:,}".format(result[1]) + " | Time to refresh AH: " + str(round(done, 2)))
        print("\nLooking for auctions...")

def play_sound():
    if os.name == 'posix':
        subprocess.call(["afplay", "/System/Library/Sounds/Glass.aiff"])

print("Looking for auctions...")
main()

def dostuff():
    global now, toppage

    if time.time() * 1000 > now + 60000:
        prevnow = now
        now = float('inf')
        c = requests.get("https://api.hypixel.net/skyblock/auctions?page=0").json()
        if c['lastUpdated'] != prevnow:
            now = c['lastUpdated']
            toppage = c['totalPages']
            main()
        else:
            now = prevnow
        time.sleep(0.25)

while True:
    dostuff()
