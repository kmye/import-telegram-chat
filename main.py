import os

from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import *
from export_builder.file_writer import FileWriter
from export_builder.telegram_export_transformer import TelegramExportTransformer

from dotenv import load_dotenv

load_dotenv()

TARGET_CHAT_ID = os.getenv('TARGET_CHAT_ID')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BACKUP_FILE_PATH = "backups/input_file.json" # backup file json path

with TelegramClient('Messages Importer', API_ID, API_HASH) as client:
    client.get_dialogs()
    chat = client.get_entity(PeerChannel(TARGET_CHAT_ID))

    media_count, messages = TelegramExportTransformer(BACKUP_FILE_PATH).process()
    export_writer = FileWriter(messages)
    export_writer.write()

    result = client(functions.messages.InitHistoryImportRequest(
        peer=chat,
        file=client.upload_file(export_writer.file_name),
        media_count=media_count
    ))
    print(result.stringify())

    result = client(functions.messages.StartHistoryImportRequest(
        peer=chat,
        import_id=result.id
    ))
    print(result)