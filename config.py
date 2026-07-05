import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API credentials
API_ID = os.getenv("30422005", None)
API_HASH = os.getenv("5170ded206641d73215baf40175a6924", None)
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
