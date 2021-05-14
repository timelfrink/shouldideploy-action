import urllib.request
import json
import sys

url = f"https://shouldideploy.today/api?tz={sys.argv[1]}"
req = urllib.request.urlopen(url)

data = json.loads(req.read().decode("utf-8"))
print('test')
print(data)
print(f"::set-output name=deploy::{data['shouldideploy']}")
print('test2')
print(data['shouldideploy'])
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
x = "fstring"
print(f"{x}")