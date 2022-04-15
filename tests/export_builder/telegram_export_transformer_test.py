import pytest
from export_builder import telegram_export_transformer

class TestTelegramExportTransformer:
    def test_emoji_message(self):
        transformer = telegram_export_transformer.TelegramExportTransformer("tests/fixtures/message_is_sticker.json")
        count, results = transformer.process()
        assert count == 1
        assert results == ['2022-04-10, 13:21 - Eileen Kang: stickers/sticker.webp (file attached)']

    def test_text_message(self):
        transformer = telegram_export_transformer.TelegramExportTransformer("tests/fixtures/message_is_text_message.json")
        count, results = transformer.process()
        assert count == 0
        assert results == ['2022-04-10, 13:22 - Eileen Kang: test test test']
    
    def test_mentions_message(self):
        transformer = telegram_export_transformer.TelegramExportTransformer("tests/fixtures/message_is_mention.json")
        count, results = transformer.process()
        assert count == 0
        assert results == ['2022-04-10, 13:22 - Eileen Kang: @symbol']