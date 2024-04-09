
from redbot.core.bot import Red
from .pincog import PinCog
import asyncio


async def setup(bot):
    cog = PinCog(bot)
    await bot.add_cog(cog)
     # await cog.initialize()
