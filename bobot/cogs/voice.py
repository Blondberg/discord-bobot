from discord.ext import commands
from ..core import messageformatter as mf


class Voice(commands.Cog, name="Voice"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join", description="Make Bobot join your current channel")
    async def join(self, ctx: commands.Context):
        if not ctx.author.voice:
            await ctx.send(mf.format("You are not in a voice channel...."))
            return
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command(name="leave", description="Make Bobot leave your current channel")
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()


def setup(bot: commands.Bot):
    bot.add_cog(Voice(bot))
