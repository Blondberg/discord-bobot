from discord.ext import commands
from ..core import messageformatter as mf


class Random(commands.Cog, name="Random"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="RAWR", description="Just... rawr")
    async def rawr(self, ctx):
        await ctx.send("RAWR baby :wink:")


def setup(bot: commands.Bot):
    bot.add_cog(Random(bot))
