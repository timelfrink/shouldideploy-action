import urllib.request
import json
import sys

url = f"https://shouldideploy.today/api?tz={sys.argv[1]}"
req = urllib.request.urlopen(url)

data = json.loads(req.read().decode("utf-8"))
print(data)
print(f"::set-output name=deploy::{data['shouldideploy']}")
