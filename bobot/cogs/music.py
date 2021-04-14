import discord
from discord.ext import commands


class Music(commands.Cog, name="Music"):
    def __init__(self, bot):
        self.bot = bot
