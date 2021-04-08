import discord
from discord.ext import commands
from discord.ext.commands import context
import random
from ..apis import riotapi

class League(commands.Cog, name="League of Legends"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='lolrand')
    async def random_champion(self, ctx: commands.Context, number_of_rolls = 1):
        response = ', '.join([random.choice(riotapi.get_champions()) for i in range(number_of_rolls)])
        await ctx.send(f'{response}')




def setup(bot: commands.Bot):
    bot.add_cog(League(bot))