import time
import threading
import requests

url = 'https://visitcount.itsvg.in/api?id=Robobo2022&icon=0&color=0'

request_count = 0

def send_requests():
    global request_count
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            request_count += 1
            print(f"Requests sent: {request_count}")
            time.sleep(1)
        elif response.status_code == 429:
            print("Rate limited, waiting and retrying...")
            time.sleep(60)
        else:
            print(f"Error {response.status_code} occurred")

for i in range(20):
    t = threading.Thread(target=send_requests)
    t.start()
