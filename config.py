import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("", None)
API_HASH = os.getenv("", None)
GPT_API = os.getenv("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")

# Bot token and MongoDB URL fetched from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
MONGO_URL = os.getenv("MONGO_URL", None)

# Bot owner's Telegram user ID and username
OWNER_ID = os.getenv("OWNER_ID",1907873463)
OWNER_USERNAME = "SayaProject"

# Support group and update channel names
SUPPORT_GROUP = "SayaProject"
UPDATE_CHANNEL = "SayaProjectT"
