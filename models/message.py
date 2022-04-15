import re

class Message:
    def __init__(self, date, time, sender_name, message):
        self.date = date
        self.time = time
        self.sender_name = sender_name
        self.message = message

    def is_media(self):
        return self.message.endswith("(file attached)")
