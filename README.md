# import-telegram-chat
Simple script to import telegram chat exports to another telegram chats.

First it takes the telegram export (JSON format version) and transform it into a whatsapp chat export file format.
Then it exports to a file and tries to upload the export using the telethron InitHistoryImportRequest method.

# Note
This is still a work-in-progress. I have not tested it.

This README file might not be complete too. I'm still improving this README as well as the code base.

# Contribute
To contribute, feel free to make a PR!

# Setup
Run command inside virtual env
```
pipenv run
```

Install dependencies by running: pipenv install <package_name>

# Running the tests
```
python -m pytest
```

# .env file
Create a .env file in the root of the project directory. The environment file should store your secrets to the app.

The API ID and values can be obtained from https://my.telegram.org/auth

Example of `.env` file:
```
API_ID=1234567
API_HASH=abcdefg
TARGET_CHAT_ID=-12345678
```