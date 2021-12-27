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


    class JoinTeam(nextcord.ui.View):
        def __init__(self):
            super().__init__()
            self.value = 0

        @nextcord.ui.button(label = "Equipe Rouge", style = nextcord.ButtonStyle.red)
        async def teamRed(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
            await interaction.response.send_message(f"Un joueur a été mis dans l'équipe rouge !", ephemeral = False)
            self.value = True
            bot.team = 0
            self.stop

        @nextcord.ui.button(label = "Equipe Bleue", style = nextcord.ButtonStyle.primary)
        async def teamBlue(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
            await interaction.response.send_message(f"Un joueur a été mis dans l'équipe Bleue !", ephemeral = False)
            self.value = True
            bot.team = 1
            self.stop

        @nextcord.ui.button(label = "Quitter votre équipe", style = nextcord.ButtonStyle.gray)
        async def leaveTeam(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
            await interaction.response.send_message(f"Un joueur a quitter une équipe !", ephemeral = False)
            self.value = False
            self.stop


    @bot.command(name = "team", description = "Permettre d'afficher des boutons de choix d'équipe")
    async def team(ctx, team = None):
        if team == "bleu":
            await ctx.send(f"{ctx.author.Display_name} est maintenant dans l'équpe bleue !")
        elif team == "rouge":
            await ctx.send(f"{ctx.author.Display_name} est maintenant dans l'équpe rouge !")
        elif team == None:
            await ctx.send(f"Vous n'avez pas utilisée correctement la commande !")

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
    bot.run(os.getenv("DISCORD_TOKEN"))


if __name__ == '__main__':
    main()