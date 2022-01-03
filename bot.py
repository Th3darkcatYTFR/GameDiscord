import discord
import random
import config
from discord.ext import commands
from discord_slash import SlashCommand
from dotenv.main import load_dotenv


def main():




    bot = commands.Bot(command_prefix = "k!", description = "Test")
    slash = SlashCommand(bot, sync_commands = True)
    load_dotenv()

    @bot.event
    async def on_ready():
        print("Kurama est maintenant connecté !")

    @slash.slash(name="help", description="Affiche la liste des commandes disponible !")
    async def helping(ctx):
        embed = discord.Embed(description = "Liste des commandes !", url = "https://cdn.discordapp.com/avatars/833726936890867784/35a4505aa389a112a73b3dbd4051f78e.png", color=0xFF7D42)
        embed.add_field(name = "Fun", value = "`funfact`")

        await ctx.send(embed)

    bot.run(config.TOKEN_BOT)


if __name__ == '__main__':
    main()