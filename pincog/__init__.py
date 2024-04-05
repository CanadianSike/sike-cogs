from .pincog import pincog
import asyncio


async def setup(bot):
    obj = bot.add_cog(pincog())
    if asyncio.iscoroutine(obj):
        await obj
