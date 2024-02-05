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



AVATARS = [
    (0, "😎"),
    (1, "🤩"),
    (3, "😇"),
    (4, "🥸"),
]

COLORS = [
    (0, "D96661"),
    (1, "BF96C3"),
    (3, "6EBCB4"),
    (4, "D9D9D9"),
]

