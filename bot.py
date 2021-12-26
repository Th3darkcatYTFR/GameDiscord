import os
import nextcord
#import asyncio
from nextcord import Member
from nextcord.colour import Color
from dotenv.main import load_dotenv
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions , MissingPermissions

def main():



    activity = nextcord.Activity(type=nextcord.ActivityType.watching, name="le futur")
    bot = commands.Bot(command_prefix="./", activity = activity, status=nextcord.Status.idle,help_command = None)

    load_dotenv()

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} est désormais connecté a discord avec succès !")

            #Identification du systeme de connexion
    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    main()