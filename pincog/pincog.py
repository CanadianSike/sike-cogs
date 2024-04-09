import asyncio
import discord
from discord.ext import commands
from redbot.core import Config, commands, checks
from redbot.core.bot import Red

from redbot.core import commands

class PinCog(commands.Cog):
    """Custom Pinning Cog"""

    def __init__(self, bot):
        self.bot = bot  

    @commands.command()
    async def sike(self, ctx):
        await ctx.send("SikeCogs Has been loaded. Good luck!")


    @checks.mod_or_permissions(manage_messages=True)
    @commands.guild_only()
    @commands.command()
    async def pinmsg(self, bot, channel_id: int, message_id: int):
        channel =  self.bot.get_channel(channel_id)
        message = channel.get_partial_message(message_id)
        await message.pin()
        