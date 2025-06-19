import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mohammedamer.atlassian.net/rest/api/3/project"

API_TOKEN = "Add api key"

auth = HTTPBasicAuth("mohammedamer9553@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)
name = output [0] ["name"] 
print(name)
