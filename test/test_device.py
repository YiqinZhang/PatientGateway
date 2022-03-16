import requests
import pytest
from device import *


class TestDevice:
    measurements = {}

    def test_no_input_data(self):
        with pytest.raises(ValueError):
            add_data(1, measurements, "test.json")

    measurements = {
        "patient_id": "1",
        "temp": "97",
        "pulse": "60",
        "blood_pressure": "110",
        "oxygen_level": "90",
        "weight": "130",
        "glucose_level": "100"
    }

    def test_no_input_id(self):
        with pytest.raises(TypeError):
            add_data(measurements, "test.json")

    def test_no_output_file(self):
        with pytest.raises(TypeError):
            add_data(1, measurements)

    def test_invalid_userid(self):
        with pytest.raises(KeyError):
            add_data(1000, measurements, "test.json")

    def test_invalid_input(self):
        measurements["pulse"] = -1
        with pytest.raises(ValueError):
            add_data(1, measurements, "test.json")

    def test_invalid_input_type(self):
        measurements["blood_pressure"] = 'abc'
        with pytest.raises(ValueError):
            add_data(1, measurements, "test.json")

    def test_invalid_input_range(self):
        measurements["oxygen_level"] = 200
        with pytest.raises(ValueError):
            add_data(1, measurements, "test.json")