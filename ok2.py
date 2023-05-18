import requests
import json

url = "https://api.hypixel.net/skyblock/bazaar"

# Make a GET request to the API endpoint
response = requests.get(url)
data = response.json()

item_profits = {}

# Iterate over the products
for product_id, product_data in data["products"].items():
    buy_price = product_data["quick_status"]["buyPrice"]
    sell_price = product_data["quick_status"]["sellPrice"]

    # Compare buy price with sell price
    if buy_price < sell_price:
        profit = sell_price - buy_price
        item_profits[product_id] = profit

# Print the item names and profits
for product_id, profit in item_profits.items():
    print(f"Item: {product_id}, Profit: {profit}")
