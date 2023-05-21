import requests
import json

url = "https://api.hypixel.net/resources/skyblock/election"
response = requests.get(url)
data = response.json()

mayor = data["mayor"]
current = data["current"]

mayor_name = mayor["name"]
current_name = max(current["candidates"], key=lambda x: x["votes"])["name"]

print("Current Mayor:", mayor_name)
print("Current Candidate with Most Votes:", current_name)
