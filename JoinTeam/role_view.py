import nextcord
import config
from utils import custom_id

VIEW_NAME = "RoleView"

class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handled_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id = int(button.custom_id.split(":")[-1])
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("Vous avez quitté votre équipe..", ephemeral = True)

        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Add to Team", ephemeral = True)

    @nextcord.ui.button(label = "Equipe rouge", emoji = "RED:925135933932732496", style = nextcord.ButtonStyle.red, custom_id = custom_id(VIEW_NAME, config.TEAM_RED_ID))
    async def red_button(self, button, interaction):
        await self.handle_click(button, interaction)

    @nextcord.ui.button(label = "Equipe bleue", emoji = "BLUE:925135962835681341", style = nextcord.ButtonStyle.primary, custom_id = custom_id(VIEW_NAME, config.TEAM_BLUE_ID))
    async def blue_button(self, button, interaction):
        await self.handle_click(button, interaction)