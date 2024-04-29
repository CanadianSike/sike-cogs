import asyncio
import discord
from discord.ext import commands
from redbot.core import Config, commands, checks
from redbot.core.bot import Red

from redbot.core import commands

class PinCog(commands.Cog):
    """Custom Pinning Cog"""

    roles = { None }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sike(self, ctx):
        await ctx.send("SikeCogs Has been loaded. Good luck!")

    @commands.command()
    async def roleset(self, ctx, roles):
        """Please submit role IDs for pinmsg permissions."""
        if roles == None:
             await ctx.send("Roles have been set")
             await ctx.send(roles)
        else:
             await ctx.send("Error, am fucked")
        


    @commands.guild_only()
    @commands.command()
    @commands.has_role(roles)
    async def pinmsg(self, ctx, channel_id: int, message_id: int):
            channel =  self.bot.get_channel(channel_id)
            message = channel.get_partial_message(message_id)
            await message.pin() 
            await ctx.send("Message has been pinned!")