import discord
from discord.ext import commands
import random
from ..apis import riotapi
from ..core import messageformatter as mf
from gtts import gTTS
from discord.utils import get


class League(commands.Cog, name="League of Legends"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="lolrand",
        description="Get a random league of legends champion. Write a number afterwards to set number of rolls (1 by default)",
    )
    async def random_champion(self, ctx: commands.Context, number_of_rolls=1):
        champion_list = riotapi.get_champions()
        rolls = (
            number_of_rolls
            if number_of_rolls <= len(champion_list)
            else len(champion_list)
        )
        random.shuffle(champion_list)
        response = ", ".join([champion_list.pop() for i in range(rolls)])

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        await ctx.send(mf.format(response))

        speech = gTTS(text=response, lang="en", slow=False)
        speech.save("./temp.mp3")

        voice.play(discord.FFmpegPCMAudio("./temp.mp3"))


def setup(bot: commands.Bot):
    bot.add_cog(League(bot))
