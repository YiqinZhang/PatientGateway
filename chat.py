# from typing import List, Union
import json
import user
from datetime import datetime


with open('inbox.json', 'r') as f:
    chat_dict = json.load(f)
    if not chat_dict:
        chat_dict = {}


class Chat:
    def __init__(self, sender, to, message):
        self.sender = sender
        self.to = to
        self.message = message

    @property
    def contact(self):
        return [self.sender] + [self.to]

    def is_valid(self):
        if len(self.message) > 1000 or len(self.message) < 2:
            return False
        for person in self.contact:
            user.abort_if_user_id_doesnt_exist(person)
        return True

    @property
    def content(self):
        return {
            "sender": self.sender,
            "to": self.to,
            "message": self.message,
            "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


def send_chat(chat):
    if not chat.is_valid():
        raise ValueError("Chat is not valid. Check length or member ids")
    content = dict(sender=chat.sender, to=chat.to, message=chat.message,
                   time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    with open('inbox.json', 'w') as f:
        num = len(chat_dict)
        chat_dict[str(num)] = content
        json.dump(chat_dict, f, indent=2)

    return chat_dict


# send_chat(Chat(1, 2, "The First message"))
# send_chat(Chat(2, 3, "Second message sent"))
# def get_chat_history(user_id):
#     abort_if_user_id_doesnt_exist(user_id)
#     for user in data:
#         if user['user_id'] == user_id:
#             return user
#
#
# def del_chat_history(user_id):
#     abort_if_user_id_doesnt_exist(user_id)
#     for u in data:
#         if u['user_id'] == user_id:
#             deleted = u
#             data.remove(u)
#             if not u:
#                 raise ValueError(f"User {user_id} is not deleted")
#             break
#     with open('user.json', 'w') as f:
#         user_dict.update({"users": data})
#         json.dump(user_dict, f, indent=2)
#     return deleted


