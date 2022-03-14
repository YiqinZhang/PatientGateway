import unittest
import requests

BASE = "http://127.0.0.1:5000/"
# temperature, blood pressure, pulse, oximeter, weight and Glucometer
response = requests.get(BASE + "device/1")
print(response.json())
response = requests.put(BASE + "device/1", {"temperature": 37})
response = requests.put(BASE + "device/1", {"blood pressure": "70/90", "pulse": 60})

response = requests.get(BASE + "device/1")
print(response.json())

# data = [{"temperature": "tim", "DoB": "07/19/1998", "gender": "male", "bloodtype":"A", "height": 180, "weight": 170},
#         {"name": "eve", "DoB": "12/24/2004", "gender": "female", "bloodtype":"B", "height": 166, "weight": 120},
#         {"name": "adam", "DoB": "02/22/2002", "gender": "female", "bloodtype":"AB", "height": 178, "weight": 160}]

# for i in range(len(data)):
#     response = requests.put(BASE + "device/" + str(i), data[i])
#     print(response.json())

# response = requests.delete(BASE + "device/1")
# print(response)
# input()

# response = requests.get(BASE + "device/2")
# print(response.json())
# input()

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


# if __name__ == '__main__':
#     unittest.main()
