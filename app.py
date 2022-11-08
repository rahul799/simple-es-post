import json
import requests,json

f = open('data.json')

data = json.load(f)

url = "http://localhost:9200/your_index/_doc"

count = 1
for i in data["values"]:
    print(i)
    req = requests.post(url,data=i)
    print(req.text)
    print("")
    print(req.json)
    print("----------------------------------------------")
    
# Closing file
f.close()
