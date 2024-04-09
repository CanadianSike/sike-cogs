from .pincog import PinCog
import asyncio


async def setup(bot):
    await bot.add_cog(PinCog(bot))
