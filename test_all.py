import urllib.request
import json

BASE_URL = "http://127.0.0.1:5000"

endpoints = [
    "/",
    "/events",
    "/events/1",
    "/teams",
    "/players",
    "/matches"
]

print("SPORTS EVENT MANAGEMENT API TEST")
print("=" * 40)

for endpoint in endpoints:
    try:
        url = BASE_URL + endpoint

        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())

        print(f"\nEndpoint: {endpoint}")
        print(f"Status: {response.status}")
        print("Result: PASS")

    except Exception as e:
        print(f"\nEndpoint: {endpoint}")
        print(f"Result: FAIL")
        print("Error:", e)

print("\n" + "=" * 40)
print("API TESTING COMPLETED")