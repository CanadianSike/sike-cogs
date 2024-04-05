from redbot.core import commands, checks, Config, commands
import discord

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
    async def pin_message(ctx, msg_id):
        msg_id = await ctx.fetch_message(msg_id)
        await ctx.message.pin(msg_id)
