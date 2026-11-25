import urllib.request
import urllib.error
import json

BASE_URL = "http://127.0.0.1:5000"

print("API ERROR TESTING")
print("=" * 40)

# Test 1: Invalid Event ID
try:
    response = urllib.request.urlopen(BASE_URL + "/events/999")
    print("Test 1: Unexpected Success")
except urllib.error.HTTPError as e:
    print("Test 1: Invalid Event ID")
    print("Status Code:", e.code)
    print("Result: PASS")

# Test 2: Invalid Team ID
data = {
    "player_name": "Test Player",
    "age": 20,
    "team_id": 999
}

json_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    BASE_URL + "/players",
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    response = urllib.request.urlopen(request)
    print("Test 2: Unexpected Success")
except urllib.error.HTTPError as e:
    print("Test 2: Invalid Team ID")
    print("Status Code:", e.code)
    print("Result: PASS")

print("=" * 40)
print("ERROR TESTING COMPLETED")

# Test 3: Negative Score
data = {
    "score1": -10,
    "score2": 50
}

json_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    BASE_URL + "/matches/1/score",
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="PUT"
)

try:
    response = urllib.request.urlopen(request)
    print("Test 3: Unexpected Success")
except urllib.error.HTTPError as e:
    print("\nTest 3: Negative Score")
    print("Status Code:", e.code)
    print("Result: PASS")

    # Test 4: Missing Required Field

data = {
    "event_name": "Test Event",
    "sport": "Football"
}

json_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    BASE_URL + "/events",
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    response = urllib.request.urlopen(request)
    print("Test 4: Unexpected Success")
except urllib.error.HTTPError as e:
    print("\nTest 4: Missing Required Field")
    print("Status Code:", e.code)
    print("Result: PASS")