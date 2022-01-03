import discord
from discord.ext import commands
import os
import config
from dotenv.main import load_dotenv


def main():

    load_dotenv()

    bot = commands.Bot(command_prefix="!")

    @bot.event
    async def on_ready():
        print('XIO is now online.'.
            format(bot))

    @bot.command()
    async def ping(ctx):
        await ctx.channel.send("!pong")

    bot.run(config.TOKEN_BOT)


if __name__ == '__main__':
    main()