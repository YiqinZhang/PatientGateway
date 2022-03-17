# from typing import List, Union
import json
import user
from datetime import datetime


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
        json.dump(content, f)
    # print(content)
    return content
