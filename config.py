import os
from dotenv.main import load_dotenv

load_dotenv()


PREFIX = "/"
BOT_NAME = "Duel Bot - Game"
TEAM_RED = os.getenv("RED", "")
TEAM_BLUE = os.getenv("BLUE", "")
NO_TEAM = os.getenv("NO", "")

TOKEN_BOT = os.getenv("DISCORD_TOKEN")