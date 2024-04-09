import asyncio
import discord
from discord.ext import commands
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
    async def pinmsg(self, bot, ctx, channel_id: int, message_id: int):
        channel = bot.channel.get_partial_message(channel_id)
        message = await channel.fetch_message(message_id)
        message = await channel.get_partial_message(message_id)
        await message.pin(message_id)
        