import urllib.request
import json
import sys

if "force deploy" in sys.argv[2].lower():
     sys.exit(0)

url = f"https://shouldideploy.today/api?tz={sys.argv[1]}"
req = urllib.request.urlopen(url)

data = json.loads(req.read().decode("utf-8"))
print(data)

if not data['shouldideploy']:
    sys.exit('You should not deploy!')
