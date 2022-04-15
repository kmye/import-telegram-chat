import json
from export_builder import whatsapp_export_formatter
from models.message import Message

class TelegramExportTransformer:
    input_data = {}

    def __init__(self, input_filepath):
        json_file = open(input_filepath)
        self.input_data = json.load(json_file)
        json_file.close()

    def process(self):
        message_objects = self._build_message_object()
        return self._format_to_output(message_objects)

    def _build_message_object(self):
        messages_list = self.input_data["messages"]

        output = []

        for message in messages_list:
            message_text = message["text"]
            if message["type"] == "message":
                date, time = self._parse_date(message["date"])
                message_text = self._extract_text(message)
                output.append(Message(date, time, message["from"], message_text))
        
        return output

    def _format_to_output(self, messages):
        output = []
        total_media_count = 0
        for data in messages:
            total_media_count += 1 if data.is_media() else 0
            output.append(whatsapp_export_formatter.process(data))
        
        return total_media_count, output

    def _extract_text(self, message):
        message_text = message["text"]
        is_media = message_text == ""

        if is_media:
            message_text = self._format_emoji_text(message["file"])          
        else:
            is_mention = isinstance(message_text, list)
            message_text = message_text[0]["text"] if is_mention else message_text

        return message_text

    def _parse_date(self, date):
        return date[0:10], date[11:16]

    def _format_emoji_text(self, text):
        return "{text} (file attached)".format(text=text)

