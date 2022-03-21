import pytest
import chat


<<<<<<< HEAD
class TestChat:
=======
class TestDevice:
>>>>>>> e678fbc19556e5fb44d72bab7ed09cbd5590d923
    def test_chat_no_contact(self):
        with pytest.raises(TypeError):
            chat.Chat("no contact")

    def test_chat_no_message(self):
        with pytest.raises(TypeError):
            chat.Chat(1, 2)

    def test_send_chat_invalid_sender(self):
        with pytest.raises(KeyError):
            chat.send_chat(chat.Chat(1000, 1, "invalid receiver"))

    def test_send_chat_invalid_receiver(self):
        with pytest.raises(KeyError):
            chat.send_chat(chat.Chat(1, 1000, "invalid receiver"))

    def test_send_chat_empty_message(self):
        with pytest.raises(ValueError):
            chat.send_chat(chat.Chat(1, 2, ""))

<<<<<<< HEAD
    def test_send_chat(self):
=======
    def test_send_chat_empty_message(self):
>>>>>>> e678fbc19556e5fb44d72bab7ed09cbd5590d923
        content = chat.send_chat(chat.Chat(1, 2, "sent"))
        assert content["sender"] == 1
        assert content["to"] == 2
        assert content["message"] == "sent"
        assert content["time"] is not None