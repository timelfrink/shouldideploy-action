import urllib.request
import json
import sys

url = f"https://shouldideploy.today/api?tz={sys.argv[1]}"
req = urllib.request.urlopen(url)

data = json.loads(req.read().decode("utf-8"))
print(data)
print(sys.argv[2])
if "Force deploy" in sys.argv[2]:
     sys.exit(0)
elif not data['shouldideploy']:
    sys.exit('You should not deploy!')
