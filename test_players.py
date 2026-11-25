import urllib.request
import json

url = "http://127.0.0.1:5000/players"

data = {
    "player_name": "Bala",
    "age": 20,
    "team_id": 1
}

json_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    url,
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

response = urllib.request.urlopen(request)

print("PLAYER REGISTRATION:")
print(response.status)
print(response.read().decode())

# View all players
get_response = urllib.request.urlopen(url)

print("\nREGISTERED PLAYERS:")
print(get_response.read().decode())