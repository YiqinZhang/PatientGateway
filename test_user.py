import pytest
import requests
import user
import device


# BASE = "http://127.0.0.1:5000/"


class TestUser:
    def test_abort_if_user_id_doesnt_exist(self):
        with pytest.raises(KeyError):
            user.abort_if_user_id_doesnt_exist(10000)

    def test_abort_empty_user_id(self):
        with pytest.raises(TypeError):
            user.abort_if_user_id_doesnt_exist()

    def test_abort_if_id_exists(self):
        with pytest.raises(KeyError):
            user.abort_if_id_exists(1)

    def test_get_user_id_doesnt_exist(self):
        with pytest.raises(KeyError):
            test_user = user.get_user(1000)

    def test_get_user(self):
        test_user = user.get_user(1)
        assert test_user['user_id'] == 1

    def test_add_user_id_exists(self):
        with pytest.raises(KeyError):
            user.add_user(1, 'jack', '2/22/2000')

    def test_add_user(self):

        test_user = user.add_user(500, 'jack', '2/22/2000')
        assert test_user['user_id'] == 500

    def test_modify_user_id_doesnt_exist(self):
        updates = {
            "systolic_blood_pressure": 120,
            "diastolic_blood_pressure": 80,
            "blood_type": "O",
            "oxygen_level": 97,
            "weight": 138,
            "glucose_level": 120,
        }
        with pytest.raises(KeyError):
            test_user = user.modify_user(200, updates)

    def test_modify_user(self):
        updates = {
            "systolic_blood_pressure": 120,
            "diastolic_blood_pressure": 80,
            "blood_type": "O",
            "oxygen_level": 97,
            "weight": 138,
            "glucose_level": 120,
        }
        test_user = user.modify_user(1, updates)
        assert test_user["blood_type"] == 'O'

    def test_del_user_id_doesnt_exist(self):
        with pytest.raises(KeyError):
            test_user = user.del_user(1000)

    def test_del_user(self):
        user.add_user(350, 'jack', '2/22/2000')
        deleted_user = user.del_user(350)
        assert deleted_user['user_id'] == 350



