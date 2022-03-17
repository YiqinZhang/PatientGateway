import requests
from flask import request, Flask
import app

BASE = "http://127.0.0.1:5000/"

app = Flask(__name__)


class TestRequest:
    def test_request_input(self):
        with app.test_request_context('/login', method='POST'):
            assert request.path == '/login'
            assert request.method == 'POST'

    def test_login_response(self):
        response = requests.get(BASE + "login")
        assert response.status_code == 200
