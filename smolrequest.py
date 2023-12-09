import requests
import threading
from fake_useragent import UserAgent
from tqdm import tqdm

link = input("Enter the link: ")
amount_request = int(input("Enter the amount of requests: "))

ua = UserAgent()
SUCCESS_COUNT = 0

def send_request(session, progress_bar):
    global SUCCESS_COUNT
    try:
        response = session.get(link, timeout=10)
        response.raise_for_status()
        SUCCESS_COUNT += 1
        progress_bar.update(1)
    except requests.RequestException as e:
        print(f"Error: {e}")

def main():
    session = requests.Session()
    session.headers.update({'User-Agent': ua.random})  

    progress_bar = tqdm(total=amount_request, desc="Sending Requests", unit="req")
    threads = [threading.Thread(target=send_request, args=(session, progress_bar)) for _ in range(amount_request)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    progress_bar.close()

if __name__ == "__main__":
    main()

print(f"\nSuccessfully sent {SUCCESS_COUNT} out of {amount_request} requests.")
