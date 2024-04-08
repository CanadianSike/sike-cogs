import asyncio
import discord
from redbot.core import Config, commands, checks
from redbot.core.bot import Red

class PinCog(commands.Cog):
    """Custom Pinning Cog"""

    @commands.command()
    async def sike(self, ctx):
        await ctx.send("SikeCogs Has been loaded. Good luck!")


    @checks.mod_or_permissions(manage_messages=True)
    @commands.guild_only()
    @commands.command()
    async def pinmsg(ctx, chnl_id, msg_id: int):
        channel = guild.get_channel(chnl_id)
        message = await ctx.chnl_id.fetch_message(msg_id)
        await message.pin(msg_id)
        