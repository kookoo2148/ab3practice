import requests
import json

url = "https://e33hftfjpg.us-east-1.awsapprunner.com/api/test"

# A GET request to the API
response = requests.get(url)

# Print the response
#response_json = response.json()
#print(response_json)

print(response.status_code)