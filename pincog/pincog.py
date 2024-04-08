from redbot.core import commands, checks, Config, commands
from redbot.core.i18n import Translator, cog_i18n
import discord


class PinCog(commands.Cog):
    """Custom Pinning Cog"""

    @commands.command()
    async def sike(self, ctx):
        await ctx.send("SikeCogs Has been loaded. Good luck!")


    @checks.mod_or_permissions(manage_messages=True)
    @commands.guild_only()
    @commands.command()
    async def pinmsg(ctx, msg_id: int):
        message = await ctx.get_partial_messageable(msg_id)
        await message.pin(msg_id)
        