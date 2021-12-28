from .role_view import RoleView
from nextcord.ext import commands


class ButtonRoles(commands.Cog, name = "Roles Main"):

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.__bot.add_view(RoleView())

    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx: commands.Context):
        await ctx.send("Choisir votre équipe en cliquant sur le bouton de votre choix !", view = RoleView())

def setup(bot):
    bot.add_cog(ButtonRoles(bot))