# from typing import List, Union
import json
import user
from datetime import datetime

with open('user.json', 'r') as f:
    data = json.load(f)
    sample = data['users']
    print(sample)


class Chat:
    def __init__(self, sender, to, message):
        self.sender = sender
        self.to = to
        self.message = message


    @property
    def contact(self):
        return [self.sender] + [self.to]

    def is_valid(self):
        # message must be less than or equal to 1000 chars
        if len(self.message) > 1000:
            return False
        # need at least 2 chatters
        if len(set(self.message)) < 2:
            return False
        # Check if all members exist in the patients list
        for person in self.contact:
            try:
                sample[person]
            except:
                return False
            return True

    @property
    def content(self):
        return {
            "sender": self.sender,
            "to": self.to,
            "content": self.message,
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }


def send_chat(chat):
    if not chat.is_valid():
        raise ValueError("Chat is not valid. Check length or member ids")
    content = dict(sender=chat.sender, to=chat.to, content=chat.message,
                   timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    with open('inbox.json', 'w') as f:
        json.dump(content, f)
    return content


test_message = Chat(1, 2, "The first message")
send_chat(test_message)