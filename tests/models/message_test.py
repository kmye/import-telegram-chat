import pytest
from models.message import Message

class TestMessage:
    message = Message('date', 'time', 'name', 'this is a message')

    def test_instance_sets_correct_date(self):
        assert self.message.date == 'date'

    def test_instance_sets_correct_time(self):
        assert self.message.time == 'time'

    def test_instance_sets_correct_name(self):
        assert self.message.sender_name == 'name'

    def test_instance_sets_correct_message(self):
        assert self.message.message == 'this is a message'

    def test_instance_is_not_media(self):
        assert self.message.is_media() == False

    def test_instance_when_message_contains_media(self):
        self.message = Message('date', 'time', 'name', 'some_file.png (file attached)')
        assert self.message.is_media() == True