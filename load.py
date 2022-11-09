import time
import json
from locust import HttpUser, task, between

url = "/_search"

f1 = open('query1.json')
f2 = open('query2.json')
f3 = open('query3.json')
f4 = open('query4.json')

data1 = json.load(f1)
data2 = json.load(f2)
data3 = json.load(f3)
data4 = json.load(f4)

headers = {
    'Content-Type': 'application/json',
}

class test(HttpUser):
    wait_time = between(1,5)

    @task
    def index_page1(self):
        r = self.client.post(url = url, data=json.dumps(data1), headers = headers)

    @task
    def index_page2(self):
        r = self.client.post(url = url, data=json.dumps(data2), headers = headers)
    
    @task
    def index_page3(self):
        r = self.client.post(url = url, data=json.dumps(data3), headers = headers)
    
    @task
    def index_page4(self):
        r = self.client.post(url = url, data=json.dumps(data4), headers = headers)