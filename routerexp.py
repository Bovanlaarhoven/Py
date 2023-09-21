import requests

# Define the token endpoint URL
token_url = "https://somtoday.nl/oauth2/token"

# Define your client credentials and user credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
username = "108205"
password = "Honest3!"

# Define the payload (data) for the token request
data = {
    "grant_type": "password",
    "client_id": client_id,
    "client_secret": client_secret,
    "username": username,
    "password": password,
    "scope": "openid"  # Adjust the scope as needed
}

# Send a POST request to obtain the access token
response = requests.post(token_url, data=data)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response to get the access token
    token_response = response.json()
    access_token = token_response.get("access_token")
    print(f"Access Token: {access_token}")
else:
    print(f"Request failed with status code {response.status_code}")
    print("Response content:")
    print(response.text)
