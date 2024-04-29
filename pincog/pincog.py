import asyncio
import discord
from discord.ext import commands
from redbot.core import Config, commands, checks

from redbot.core import commands

class PinCog(commands.Cog):
    """Custom Pinning Cog"""


    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=195470, force_registration=True)
        self.config.register_global(roles=[int])

   
    @commands.command()
    async def sike(self, ctx):
        await ctx.send("SikeCogs Has been loaded. Good luck!")

    @commands.command()
    async def roleset(self, ctx, roles: int):
        """Please submit role IDs for pinmsg permissions."""
        if roles == int:
             await ctx.send("Roles have been set")
             await ctx.send(roles)
        else:
             await ctx.send("Error, am fucked")
        


    @commands.guild_only()
    @commands.command()
    #@commands.has_role(roles)
    async def pinmsg(self, ctx, channel_id: int, message_id: int):
            channel =  self.bot.get_channel(channel_id)
            message = channel.get_partial_message(message_id)
            await message.pin() 
            await ctx.send("Message has been pinned!")