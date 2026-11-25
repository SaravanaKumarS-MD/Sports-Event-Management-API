import urllib.request
import json

url = "http://127.0.0.1:5000/events"

# Event details
data = {
    "event_name": "Annual Sports Meet 2026",
    "sport": "Cricket",
    "venue": "College Ground",
    "event_date": "2026-12-15"
}

# Convert data into JSON
json_data = json.dumps(data).encode("utf-8")

# Send POST request
request = urllib.request.Request(
    url,
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

# Get response
response = urllib.request.urlopen(request)

print("POST RESPONSE:")
print(response.status)
print(response.read().decode())

# Send GET request
get_response = urllib.request.urlopen(url)

print("\nGET RESPONSE:")
print(get_response.read().decode())