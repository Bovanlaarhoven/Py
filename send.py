import threading
import requests
import time

url = ''

request_count = 0

def send_requests():
    global request_count
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            request_count += 1
            print(f"\rRequests sent: {request_count}", end='')
            time.sleep(1)
        elif response.status_code == 429:
            print("\rRate limited, waiting and retrying...", end='')
            time.sleep(60)
        else:
            print(f"\rError {response.status_code} occurred", end='')

for i in range(2000):
    t = threading.Thread(target=send_requests)
    t.start()
