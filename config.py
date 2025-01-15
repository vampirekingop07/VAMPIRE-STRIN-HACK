# TEAM PURVI ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20536459"
    API_HASH = "c1c01c363ed3dcd6017d89d5938afb6f"
    #TOKEN = "7902063510:AAGHx9Y0VngL7FoXGgCWWvfkCpgoLhtWpUQ"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://nakuldkdhacker:nakuldkdhacker$100@cluster0.45znzoj.mongodb.net/"
    START_PIC = "https://files.catbox.moe/ppvvg0.jpg"
    SUDOERS = filters.user(["6961211249"])
