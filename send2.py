import concurrent.futures
import random
import requests
import time

url = 'https://visitcount.itsvg.in/api?id=Robobo2022&icon=0&color=0'

proxies = [
    'http://72.221.171.135:4145',
    'socks4://142.54.236.97:4145',
    'http://157.100.28.18:999',
    'http://125.66.100.112:9091',
    'socks5://184.178.172.3:4145',
    'http://142.93.221.60:8080',
    'socks4://185.139.56.133:4145',
    'socks4://45.118.205.156:1080',
    'http://146.59.147.70:8888',
    'socks5://184.181.217.206:4145',
    'socks4://187.177.30.154:4145',
    'http://64.225.4.12:9995',
    'http://61.53.66.116:9091',
    'http://120.234.203.171:9002',
    'socks4://72.210.208.101:4145',
    'http://64.225.105.92:8080',
    'socks4://72.206.181.103:4145',
    'http://103.150.18.218:80',
]

request_count = 0

def send_requests():
    global request_count
    while True:
        try:
            proxy = {'https': proxies[random.randint(0, len(proxies)-1)]}
            response = requests.get(url, proxies=proxy)
            if response.status_code == 200:
                request_count += 1
                print(f"\rRequests sent: {request_count}", end='')
            elif response.status_code == 429:
                print("\rRate limited, waiting and retrying...", end='')
                time.sleep(60)
            else:
                print(f"\rError {response.status_code} occurred", end='')
        except KeyboardInterrupt:
            break

with concurrent.futures.ThreadPoolExecutor(max_workers=2000) as executor:
    futures = [executor.submit(send_requests) for i in range(2000)]
    for future in concurrent.futures.as_completed(futures):
        pass
