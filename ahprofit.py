import requests
import humanize

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
    # Take response in as JSON to find total pages
    r = requests.get("https://api.hypixel.net/skyblock/auctions").json()

    total_pages = int(r['totalPages'])
    print(f"Total Pages: {total_pages}")

    items = []

    for i in range(0, total_pages):
        r = requests.get(f"https://api.hypixel.net/skyblock/auctions?page={i}").json()
        if 'auctions' in r:
            auctions = r['auctions']

            for auction in auctions:
                if auction.get("bin") and auction.get("starting_bid"):
                    bin_price = int(auction["starting_bid"])
                    item_name = auction.get("item_name", "Unknown")
                    items.append([bin_price, item_name, auction["uuid"]])

        print(f"\rChecking Page {i+1}/{total_pages}", end="")

    if not items:
        # If no data found
        print("\nNo BIN items found in the auctions.")
        continue

    items.sort(key=lambda x: x[0])

    best_profit_item = None
    best_profit_percentage = 0

    if len(items) >= 2:
        for i in range(len(items) - 1):
            lowest_bin = items[i][0]
            second_lowest_bin = items[i + 1][0]
            price_difference = second_lowest_bin - lowest_bin

            if (
                price_difference > 0
                and second_lowest_bin <= 10000000
                and lowest_bin <= 10000000
            ):
                profit_percentage = (price_difference / lowest_bin) * 100

                if (
                    profit_percentage > best_profit_percentage
                    and price_difference >= min_profit
                ):
                    best_profit_item = items[i]
                    best_profit_percentage = profit_percentage

        if best_profit_item:
            bin_price = best_profit_item[0]
            item_name = best_profit_item[1]
            item_uuid = best_profit_item[2]

            auction_link = f"/viewauction {item_uuid}"

            profit_amount = second_lowest_bin - lowest_bin

            formatted_bin_price = humanize.intword(bin_price)
            formatted_profit_amount = humanize.intword(profit_amount)
            formatted_profit_percentage = f"{best_profit_percentage:.2f}%"

            print("\nBest Profitable Item:")
            print(f"Item Name: {item_name}")
            print(f"BIN Price: {formatted_bin_price}")
            print(f"Profit Percentage: {formatted_profit_percentage}")
            print(f"Profit Amount: {formatted_profit_amount}")
            print(f"Auction Link: {auction_link}")
        else:
            print("\nNo items with a profitable price difference found.")
    else:
        print("\nInsufficient items to calculate price difference.")

    print("------------------------------")
