from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6139759254"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://i.ibb.co/h9GBt42/file-6320.jpg")
API_ID = int(getenv("API_ID", "23631217"))
API_HASH = str(getenv("API_HASH", "
e50b6c6e9dc8077ec3e9db0e565631e4

"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "-1002006400723") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://mrnoffice692:PsO4VGHI9heKd7WA@cluster0.o1vcj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
