import requests
import json

url = "https://api.hypixel.net/skyblock/bazaar"

response = requests.get(url)
data = response.json()

item_profits = {}

for product_id, product_data in data["products"].items():
    buy_price = product_data["quick_status"]["buyPrice"]
    sell_price = product_data["quick_status"]["sellPrice"]
    product_name = product_data["product_id"]

    if buy_price != 0:
        profit = sell_price - buy_price
        profit_percentage = (profit / buy_price) * 100
        item_profits[product_name] = (profit_percentage, profit)

if not item_profits:
    print("No items found")
else:
    print("Items with Profitable Sell Price:")
    for product_name, (profit_percentage, profit) in item_profits.items():
        print(f"Item: {product_name}")
        print(f"Profit Percentage: {abs(profit_percentage):.2f}%")
        print(f"Profit Amount: {abs(profit)}\n")
