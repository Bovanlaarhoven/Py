import requests
import threading
import time
import sys

link = input("Enter the link: ")
amount_request = int(input("Enter the amount of requests: "))

num_requests = 0
num_requests_lock = threading.Lock()
barrier = threading.Barrier(amount_request)

def send_Request():
    global num_requests
    while True:
        try:
            with num_requests_lock:
                if num_requests >= amount_request:
                    break
            response = requests.post(link)
            response.raise_for_status()
            num_requests += 1
            sys.stdout.write(f"\rSent request {num_requests}")
            sys.stdout.flush()
        except (requests.exceptions.RequestException, ConnectionError) as e:
            print(f"Error: {e}")
            time.sleep(2 ** min(num_requests, 10))
        finally:
            barrier.wait() 
            time.sleep(0.1)

threads = []

for i in range(amount_request):
    t = threading.Thread(target=send_Request)
    threads.append(t)

for i in range(amount_request):
    threads[i].start()

for i in range(amount_request):
    threads[i].join()

print()
