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
    bot = commands.Bot(command_prefix="/", activity = activity, status=nextcord.Status.idle,help_command = None)

    load_dotenv()

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} est désormais connecté a discord avec succès !")
        bot.startGame = False

    # Démarrage du jeu
    @bot.command(name = "start", description = "Démarrer le jeu")
    async def start(ctx):
        if bot.startGame == False:
            bot.startGame = True
            ctx.message.send("Que le jeu commence !")
        else:
            ctx.message.send("Le jeu est déjà en cours !")

    # Arret du jeu
    @bot.command(name = "stop", description = "Arreter le jeu")
    async def stopgame(ctx):
        if bot.startGame == True:
            bot.starGame = False
            ctx.message.send("Arret du jeu !")
        else:
            ctx.message.send("Aucun jeu en cours !")

    #Identification du systeme de connexion
    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    main()