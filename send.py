import time
import threading
import requests

url = 'https://camo.githubusercontent.com/77e56b1873f7b8d1f5068cef42dbe33055583e7d56b94e30f3021732222f536b/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d726f626f626f32303232266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174'

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

for i in range(10):
    t = threading.Thread(target=send_requests)
    t.start()
