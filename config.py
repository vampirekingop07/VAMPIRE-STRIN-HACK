# TEAM BALLOONFLAME7 ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "24771953"
    API_HASH = "2dd99aa9f140d0eacb46368d1dd0994b"
    TOKEN = "8198847203:AAG_HuB34GjqAjN2YFHLiOrpo3btdYz5epE"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://Balloonflame7:jatin%40%230212@nobino-worm-gpt-ai.pnhvasg.mongodb.net/?retryWrites=true&w=majority&appName=Nobino-worm-gpt-ai"
    START_PIC = "https://files.catbox.moe/ppvvg0.jpg"
    SUDOERS = filters.user([""])
