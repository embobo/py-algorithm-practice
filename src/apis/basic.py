import http
import json
from urllib import request

response = request.urlopen("https://swapi.dev/api/starships/9/")
text = response.read()
print(json.loads(text.decode("utf-8")))

# ------------------------ #

data = {"name": "Obi-Wan Kenobi"}

encoded_data = json.dumps(data).encode()

req = request.Request("https://httpbin.org/post", data=encoded_data)
req.add_header("Content-Type", "application/json")
response = request.urlopen(req)

text = response.read()

print(json.loads(text.decode("utf-8")))

# ------------------------ #

r = http.request("GET", "https://swapi.dev/api/starships/9/")

print(json.loads(r.data.decode("utf-8")))
