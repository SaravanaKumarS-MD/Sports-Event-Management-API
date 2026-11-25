import urllib.request
import json

url = "http://127.0.0.1:5000/teams"

data = {
    "team_name": "Warriors",
    "captain": "Arun",
    "event_id": 1
}

json_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    url,
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

response = urllib.request.urlopen(request)

print("TEAM REGISTRATION:")
print(response.status)
print(response.read().decode())

# View all teams
get_response = urllib.request.urlopen(url)

print("\nREGISTERED TEAMS:")
print(get_response.read().decode())

import urllib.request
import json

url = "http://127.0.0.1:5000/teams"

data = {
    "team_name": "Challengers",
    "captain": "Vijay",
    "event_id": 1
}

json_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    url,
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

response = urllib.request.urlopen(request)

print("TEAM REGISTRATION:")
print(response.status)
print(response.read().decode())

# View all teams
get_response = urllib.request.urlopen(url)

print("\nALL TEAMS:")
print(get_response.read().decode())