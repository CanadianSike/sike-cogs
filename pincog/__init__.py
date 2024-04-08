from .pincog import PinCog
import asyncio


async def setup(bot):
    obj = bot.add_cog(PinCog())
    if asyncio.iscoroutine(obj):
        await obj
