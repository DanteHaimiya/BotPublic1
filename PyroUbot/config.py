import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "9999"))

DEVS = list(map(int, os.getenv("DEVS", "8125506794").split()))

API_ID = int(os.getenv("API_ID", "39291287"))

API_HASH = os.getenv("API_HASH", "12065e00fd0bda9d0bf2ce9205b5be0c")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8437236910:AAHOKz8Kfz4lEs6yu_vFxX5fgz-8fEPuMeg")

OWNER_ID = int(os.getenv("OWNER_ID", "8125506794"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003701593699").split()))

RMBG_API = os.getenv("RMBG_API", "s6tucqWKCDGQPTfaV78xxTZs")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://rodilov859_db_user:AOctsCxRkx0gRWLs@cluster0.p2ssm7t.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003356598260"))