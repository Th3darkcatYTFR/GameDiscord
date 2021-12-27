from .role_view import RoleView
from nextcord.ext import commands

from JoinTeam.role_view import RoleView

class ButtonRoles(commands.Cog, name = "Roles Main"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(RoleView())

    @commands.command()
    @commands.has_permissions(manage_message = True)
    async def roles(self, ctx: commands.Context):
        await ctx.send("Choisir votre équipe en cliquant sur le bouton de votre choix !", view = RoleView())