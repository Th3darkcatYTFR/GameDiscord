from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
import config
from dotenv.main import load_dotenv


def main():

    bot = Client(intents=Intents.default())
    slash = SlashCommand(bot)
    load_dotenv()

    @bot.event
    async def on_ready():
        print("Mon Bot est maintenant connecté !")

    @slash.slash(name="test")
    async def test(ctx: SlashContext):
        embed = Embed(title="Embed Test")
        await ctx.send(embed=embed)

    bot.run(config.TOKEN_BOT)


if __name__ == '__main__':
    main()