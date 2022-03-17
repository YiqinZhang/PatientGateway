import pytest
# from chat import *


class TestDevice:
    def test_chat_no_contact(self):
        with pytest.raises(TypeError):
            Chat("no contact")

    def test_chat_no_message(self):
        with pytest.raises(TypeError):
            Chat(1, 2)

    def test_send_chat_invalid_sender(self):
        with pytest.raises(KeyError):
            send_chat(Chat(1000, 1, "invalid receiver"))

    def test_send_chat_invalid_receiver(self):
        with pytest.raises(KeyError):
            send_chat(Chat(1, 1000, "invalid receiver"))

    def test_send_chat_empty_message(self):
        with pytest.raises(ValueError):
            send_chat(Chat(1, 2, ""))

    def test_send_chat_empty_message(self):
        content = send_chat(Chat(1, 2, "sent"))
        assert content["sender"] == 1
        assert content["to"] == 2
        assert content["message"] == "sent"
        assert content["time"] is not None
