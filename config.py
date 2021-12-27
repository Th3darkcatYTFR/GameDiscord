import os
from dotenv.main import load_dotenv

load_dotenv()


PREFIX = "/"
BOT_NAME = "Duel Bot - Game"
TEAM_RED = int(os.getenv("RED", ""))
TEAM_BLUE = int(os.getenv("BLUE", ""))
NO_TEAM = int(os.getenv("NO", ""))

TOKEN_BOT = os.getenv("DISCORD_TOKEN")