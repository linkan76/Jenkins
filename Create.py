# =========
# create space
# =========
import requests
import json

# [CONFLUENCE-BASE-URL], i.e.: http(s)://confluence
# [SPACE-KEY], i.e.: ds (stands for Demonstration Space)
# [SPACE-TITLE], i.e.: Demonstration Space
url = 'https://abinash76.atlassian.net/wiki/rest/api/content/'
data = {"key":"[SPACE-KEY]","name":"[SPACE-TITLE]","description":{"plain":{"value":"This is an example space","representation":"plain"}}}
headers = {'Content-Type': 'application/json'}

# create page
# [USERNAME], i.e.: admin
# [PASSWORD], i.e.: admin
r = requests.post(url, data=json.dumps(data), headers=headers, auth=('pradhan.abinash76@gmail.com','Abinash@76'))
print(r.status_code)
print(r.text)