import requests
import json

try:
    url = "http://localhost:9696/givescore"
    client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
    response = requests.post(url, json=client).json()
    print(response)

except json.JSONDecodeError as e:
    print("JSON decoding failed: ", e)
