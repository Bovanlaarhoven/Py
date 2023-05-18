import requests
import humanize
import time
import concurrent.futures

def process_auction_profit(min_profit):
    processed_items = set()
    start_time = time.time()

    def process_page(page):
        r = requests.get(f"https://api.hypixel.net/skyblock/auctions?page={page}").json()
        if 'auctions' in r:
            auctions = r['auctions']

            items = []
            for auction in auctions:
                if auction.get("bin") and auction.get("starting_bid"):
                    bin_price = int(auction["starting_bid"])
                    item_name = auction.get("item_name", "Unknown")
                    item_uuid = auction["uuid"]

                    if item_uuid in processed_items:
                        continue

                    items.append([bin_price, item_name, item_uuid])

            return items

        return []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        r = requests.get("https://api.hypixel.net/skyblock/auctions").json()
        total_pages = int(r['totalPages'])
        print(f"Total Pages: {total_pages}")

        items = []

        futures = [executor.submit(process_page, page) for page in range(total_pages)]

        for future in concurrent.futures.as_completed(futures):
            page_items = future.result()
            items.extend(page_items)

        if not items:
            print("\nNo BIN items found in the auctions.")
            exit()

        items.sort(key=lambda x: x[0])

        best_profit_items = []

        if len(items) >= 2:
            for i in range(len(items) - 1):
                lowest_bin = items[i][0]
                second_lowest_bin = items[i + 1][0]
                price_difference = second_lowest_bin - lowest_bin

                if (
                    price_difference > 0
                    and second_lowest_bin <= 10000000
                    and lowest_bin <= 10000000
                    and price_difference >= min_profit
                ):
                    profit_percentage = (price_difference / lowest_bin) * 100
                    best_profit_items.append({
                        "bin_price": lowest_bin,
                        "item_name": items[i][1],
                        "profit_amount": price_difference,
                        "profit_percentage": profit_percentage,
                        "item_uuid": items[i][2]
                    })

            if best_profit_items:
                print("\nBest Profitable Items:")
                for item in best_profit_items:
                    bin_price = item["bin_price"]
                    item_name = item["item_name"]
                    profit_amount = item["profit_amount"]
                    profit_percentage = item["profit_percentage"]
                    item_uuid = item["item_uuid"]

                    auction_link = f"/viewauction {item_uuid}"

                    formatted_bin_price = humanize.intword(bin_price)
                    formatted_profit_amount = humanize.intword(profit_amount)
                    formatted_profit_percentage = f"{profit_percentage:.2f}%"

                    print(f"\nItem Name: {item_name}")
                    print(f"BIN Price: {formatted_bin_price}")
                    print(f"Profit Percentage: {formatted_profit_percentage}")
                    print(f"Profit Amount: {formatted_profit_amount}")
                    print(f"Auction Link: {auction_link}")

                    processed_items.add(item_uuid)

            else:
                print("\nNo items with a profitable price difference found.")
        else:
            print("\nInsufficient items to calculate price difference.")

        print("------------------------------")

        elapsed_time = time.time() - start_time
        if elapsed_time < 60:
            time.sleep(1)
        else:
            start_time = time.time()
            processed_items = set()

min_profit_input = input("Enter the minimum profit (example: 100k, 1m): ")
min_profit_input = min_profit_input.lower().strip()

if min_profit_input.endswith("k"):
    min_profit = int(min_profit_input[:-1]) * 1000
elif min_profit_input.endswith("m"):
    min_profit = int(min_profit_input[:-1]) * 1000000
else:
    try:
        min_profit = int(min_profit_input)
    except ValueError:
        print("Invalid input. Exiting the script.")
        exit()

while True:
    process_auction_profit(min_profit)
