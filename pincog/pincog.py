import asyncio
import discord
from discord.ext import commands
from redbot.core import Config, commands, checks
from redbot.core.bot import Red
from discord.utils import get

from redbot.core import commands

class PinCog(commands.Cog):
    """Custom Pinning Cog"""

    #roles = {int}

    def __init__(self, bot):
        self.bot = bot
        self.config
        
    @commands.command()
    async def sike(self, ctx):
        await ctx.send("SikeCogs Has been loaded. Good luck!")

    @commands.command()
    async def roleset(self, ctx, roleid: int):
        """Please submit role IDs for pinmsg permissions."""
        roles = [roleid]
        await ctx.send(roles)

    @discord.app_commands.checks.has_role(roles)
    @commands.guild_only()
    @commands.command()
    async def pinmsg(self, ctx, channel_id: int, message_id: int): 
            channel =  self.bot.get_channel(channel_id)
            message = channel.get_partial_message(message_id)
            await message.pin() 
            await ctx.send("Message has been pinned!")

