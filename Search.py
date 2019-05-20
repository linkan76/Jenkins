import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://abinash76.atlassian.net/wiki/rest/api/content/search?cql=text~Install"
#url = "https://abinash76.atlassian.net/wiki/rest/api/content"
#url = "https://abinash76.atlassian.net/wiki/rest/api/content/search?cql=space=devopschat"
auth = HTTPBasicAuth("pradhan.abinash76@gmail.com", "HsIdmCd3YeXBYZKkQ59a9AD4")

headers = {
   "Accept": "application/json"
}

query = {
   'cql': '{cql}'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)
print(response.json)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))




