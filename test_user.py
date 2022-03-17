import pytest
import requests
import user 


# BASE = "http://127.0.0.1:5000/"

# user_data = [{"name": "tim", "DoB": "07/19/1998", "gender": "male", "bloodtype": "A", "height": 180, "weight": 170},
#              {"name": "eve", "DoB": "12/24/2004", "gender": "female", "bloodtype": "B", "height": 166, "weight": 120},
#              {"name": "adam", "DoB": "02/22/2002", "gender": "female", "bloodtype": "AB", "height": 178, "weight": 160}]


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

    # def test_login(self):
    #     response = requests.get(BASE + "user/1")
    #     result = response.json()
    #     assert response.status_code == 200
    #     assert result["user_id"] == 2

