import unittest
import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "tim", "DoB": "07/19/1998", "gender": "male", "bloodtype":"A", "height": 180, "weight": 170},
        {"name": "eve", "DoB": "12/24/2004", "gender": "female", "bloodtype":"B", "height": 166, "weight": 120},
        {"name": "adam", "DoB": "02/22/2002", "gender": "female", "bloodtype":"AB", "height": 178, "weight": 160}]

for i in range(len(data)):
    response = requests.put(BASE + "user/" + str(i), data[i])
    print(response.json())

response = requests.delete(BASE + "user/0")
print(response)
input()

response = requests.get(BASE + "user/2")
print(response.json())
input()
