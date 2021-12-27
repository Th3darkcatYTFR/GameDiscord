import os
from dotenv.main import load_dotenv

load_dotenv()


PREFIX = "/"
BOT_NAME = "Duel Bot - Game"
TEAM_RED_ID = int(float(os.getenv("TEAM_RED_ID","")))
TEAM_BLUE_ID = int((os.getenv("TEAM_BLUE_ID","")))
NO_TEAM_ID = int((os.getenv("NO_TEAM_ID","")))

TOKEN_BOT = os.getenv("DISCORD_TOKEN","")