import requests
from flask import request
from app import app
import pytest


BASE = "http://127.0.0.1:5000/"


class TestRequest:
    def test_request_input(self):
        with app.test_request_context('/login', method='POST'):
            assert request.path == '/login'
            assert request.method == 'POST'

    def test_login_response(self):
        response = requests.get(BASE + "login")
        assert response.status_code == 200
