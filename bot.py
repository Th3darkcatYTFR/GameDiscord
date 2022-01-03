import discord
from discord.ext import commands
import os
from discord_slash import SlashCommand
import config
from dotenv.main import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot)
@bot.event
async def on_ready():
    print('XIO is now online.'.
        format(bot))

@slash.slash(name="test")
async def ping(ctx):
    await ctx.channel.send("!pong")

bot.run(config.TOKEN_BOT)