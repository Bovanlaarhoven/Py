import requests

url = "https://quantumixwebsite.zenithdust.repl.co/increment_players"

# Define the number of requests you want to send
num_requests = 5

for _ in range(num_requests):
    # Send a POST request
    response = requests.post(url)

    # Check the response status code
    if response.status_code == 200:
        print("POST request was successful!")
        # Print the response content
        print("Response Content:")
        print(response.text)
    else:
        print(f"POST request failed with status code {response.status_code}")
