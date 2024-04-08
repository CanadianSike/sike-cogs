from redbot.core import commands, checks, Config, commands
from redbot.core.i18n import Translator, cog_i18n
import discord




@cog_i18n(_)
class PinCog(commands.Cog):
    """Custom Pinning Cog"""

    default_channel = {}
    default_guild = {}

    def __init__(self):
        self.settings = Config.get_conf(self, identifier=59595922, force_registration=True)
        self.settings.register_channel(**self.default_channel)
        self.settings.register_guild(**self.default_guild)

    @commands.command()
    async def sike(self, ctx):
        await ctx.send("SikeCogs Has been loaded. Good luck!")


    @checks.mod_or_permissions(manage_messages=True)
    @commands.guild_only()
    @commands.command()
    async def pinmsg(ctx, msg_id: int):
        message = await ctx.fetch_message(msg_id)
        await message.pin(msg_id)
        