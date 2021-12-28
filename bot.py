import os
import nextcord
#import asyncio
import config
from nextcord import Member
from nextcord.colour import Color
from dotenv.main import load_dotenv
from nextcord.ext import commands
from nextcord.utils import get
from nextcord.ext.commands import has_permissions , MissingPermissions

def main():



    activity = nextcord.Activity(type=nextcord.ActivityType.watching, name="le futur")
    bot = commands.Bot(command_prefix=config.PREFIX, activity = activity, status=nextcord.Status.idle,help_command = None)

    load_dotenv()

    bot.load_extension("cog")

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} est désormais connecté a discord avec succès !")
        bot.startGame = False

    # Démarrage du jeu
    @bot.command(name = "start", description = "Démarrer le jeu")
    async def start(ctx):
        await ctx.channel.purge(limit = 1)
        if bot.startGame == False:
            bot.startGame = True
            em = nextcord.Embed(title = "Duel Game - Par Th3darkcatYT", description = "Que le jeu commence !")
            await ctx.send(embed = em)
        else:
            em = nextcord.Embed(title = "Duel Game - Par Th3darkcatYT", description = "Le jeu est déjà en cours !")
            await ctx.send(embed = em)

    # Arret du jeu
    @bot.command(name = "stop", description = "Arreter le jeu")
    async def stopgame(ctx):
        await ctx.channel.purge(limit = 1)
        if bot.startGame == True:
            bot.startGame = False
            em = nextcord.Embed(title = "Duel Game - Par Th3darkcatYT", description = "Arret du jeu !")
            await ctx.send(embed = em)
        else:
            em = nextcord.Embed(title = "Duel Game - Par Th3darkcatYT", description = "Aucun jeu en cours !")
            await ctx.send(embed = em)

    #Identification du systeme de connexion
    bot.run(config.TOKEN_BOT)


if __name__ == '__main__':
    main()