import json
import requests,json

f = open('data.json')

data = json.load(f)

url = "http://localhost:9200/my-index-000001/_doc"

headers = {
    'Content-Type': 'application/json',
}

count = 1
for i in data["values"]:
    print(i)
    req = requests.post(url + "/" + str(count),data=json.dumps(i), headers=headers)
    count = count + 1
    print(req.text)
    print("")
    print(req.json)
    print("----------------------------------------------")
    
# Closing file
f.close()
