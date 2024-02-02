from dotenv import load_dotenv
import os

load_dotenv()

# t.me/wget_bash_bot
TOKEN = os.getenv("TOKEN")
BOT_URL = os.getenv("BOT_URL")

#
DOMAIN_NAME = "http://127.0.0.1:8000/"
BASH_BEGINING = "#!/bin/bash\r\n\r\n"
BASH_SPLITER = "\r\n\r\necho \"----------------------------------------------------------------\""