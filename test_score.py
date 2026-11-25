import urllib.request
import json

url = "http://127.0.0.1:5000/matches/1/score"

data = {
    "score1": 120,
    "score2": 98
}

json_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    url,
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="PUT"
)

response = urllib.request.urlopen(request)

print("SCORE UPDATE:")
print(response.status)
print(response.read().decode())

# View match result
get_response = urllib.request.urlopen(
    "http://127.0.0.1:5000/matches"
)

print("\nMATCH RESULT:")
print(get_response.read().decode())