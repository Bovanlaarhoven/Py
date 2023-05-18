import requests
import json
import humanize

# Take response in as JSON to find total pages
r = requests.get("https://api.hypixel.net/skyblock/auctions").json()

total_pages = int(r['totalPages'])
print(f"Total Pages: {total_pages}")

items = []
num_items_to_show = 10  # Number of items to display

webhook_url = "https://discord.com/api/webhooks/1108713124317626368/UNZjkTkJXjII8DveZF9Jjsq772qqbFXOrtsj8izkRY3gVZsZkAN4orykKUAdEQMHU2IE"  # Replace with your actual webhook URL

# Function to format the prices
def format_price(price):
    if price >= 1000000:  # If the price is a million or more
        return humanize.intword(price).replace("M", "m")
    elif price >= 1000:  # If the price is a thousand or more
        return humanize.intword(price).replace("K", "k")
    else:
        return str(price)

# Loop through every page
for i in range(0, total_pages):
    r = requests.get(f"https://api.hypixel.net/skyblock/auctions?page={i}").json()
    auctions = r['auctions']

    # Get each individual auction
    for auction in auctions:
        # Check if it is a BIN auction with a BIN price
        if auction.get("auction_type") == "BIN" and auction.get("starting_bid"):
            bin_price = auction["starting_bid"]
            # Append the BIN price and UUID
            items.append([bin_price, auction["uuid"]])

    # Tracking progress
    print(f"Checking Page {i+1}/{total_pages}")

# Sort the items by BIN price
if not items:
    # If no data found
    print("No BIN items found in the auctions.")
else:
    items.sort(key=lambda x: x[0])

    # Check if there are at least two items
    if len(items) >= 2:
        lowest_bin = items[0][0]
        second_lowest_bin = items[1][0]

        # Calculate the price difference
        price_difference = second_lowest_bin - lowest_bin

        if price_difference >= 10000:
            lowest_bin_uuid = items[0][1]

            # Generate the auction link with /viewauction command
            auction_link = f"/viewauction {lowest_bin_uuid}"

            # Format the BIN prices
            formatted_lowest_bin = format_price(lowest_bin)
            formatted_second_lowest_bin = format_price(second_lowest_bin)

            # Compose the payload for the webhook request
            payload = {
                "embeds": [
                    {
                        "title": "Lowest BIN Item with Significant Price Difference",
                        "description": f"Lowest BIN: {formatted_lowest_bin}\nSecond Lowest BIN: {formatted_second_lowest_bin}\nPrice Difference: {price_difference}\nAuction Link: {auction_link}",
                        "color": 16711680  # Red color
                    }
                ]
            }

        # Set the headers for the webhook request
        headers = {
            "Content-Type": "application/json"
        }

        # Send the webhook request
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        # Check if the request was successful
        if response.status_code == 204:
            print("Webhook request sent successfully.")
        else:
            print(f"Failed to send webhook request. Status Code: {response.status_code}")
