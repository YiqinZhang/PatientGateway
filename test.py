import unittest
import requests

Base = "http://127.0.0.1:5000/"

response = requests.get(Base + "device")
print(response.json())


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
