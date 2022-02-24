import unittest
import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "device/1")
print(response.json())
# response = requests.put(BASE + "device/1", {"email": "hello@bu.edu"})
response = requests.put(BASE + "device/1", {"name": "hello@bu.edu"})

response = requests.get(BASE + "device/1")
print(response.json())


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


# if __name__ == '__main__':
#     unittest.main()
