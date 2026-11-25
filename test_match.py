import urllib.request
import json

url = "http://127.0.0.1:5000/matches"

data = {
    "event_id": 1,
    "team1_id": 1,
    "team2_id": 2,
    "match_date": "2026-12-16"
}

json_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    url,
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

response = urllib.request.urlopen(request)

print("MATCH SCHEDULING:")
print(response.status)
print(response.read().decode())

# View all matches
get_response = urllib.request.urlopen(url)

print("\nALL MATCHES:")
print(get_response.read().decode())