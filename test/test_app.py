from flask import request
from app import app
import pytest

class TestRequest():
    def test_request_input(self):
        with app.test_request_context('/login', method='POST'):
            assert request.path == '/login'
            assert request.method == 'POST'