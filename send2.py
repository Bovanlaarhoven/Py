import requests
import time
import concurrent.futures
import random

url = 'https://visitcount.itsvg.in/api?id=Robobo2022&icon=0&color=0'

proxies = [
    'http://10.10.1.10:3128',
    'https://10.10.1.10:1080',
    'http://10.10.1.11:3128',
    'https://10.10.1.11:1080',
]

request_count = 0

def send_requests():
    global request_count
    while True:
        try:
            proxy = {'https': proxies[random.randint(0, len(proxies)-1)]}
            response = requests.get(url, proxies=proxy, timeout=10)
            if response.status_code == 200:
                request_count += 1
                print(f"\rRequests sent: {request_count}", end='')
            elif response.status_code == 429:
                print("\rRate limited, waiting and retrying...", end='')
                time.sleep(60)
            else:
                print(f"\rError {response.status_code} occurred", end='')
        except requests.exceptions.RequestException:
            print("\rError occurred while making request", end='')

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(send_requests) for i in range(2000)]
    for future in concurrent.futures.as_completed(futures):
        pass
