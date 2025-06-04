import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

details = response.json()

print(details[0]["user"]["id"])
