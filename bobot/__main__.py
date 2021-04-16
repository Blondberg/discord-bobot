from logging import exception
import os
import discord
from discord.ext import commands
from discord.flags import Intents
from dotenv import load_dotenv

from .core import decorators
from .cogs import leagueoflegends as lol
from .cogs import voice
from .core import messageformatter as mf
from .cogs import random

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("BOT_PREFIX")
CHANNEL_NAME = os.getenv("CHANNEL_NAME")
GENIUS_TOKEN = os.getenv("GENIUS_TOKEN")

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX))


@bot.event
async def on_ready():
    print("I am ready!")


def chunkstring(string, length):
    return (string[0 + i : length + i] for i in range(0, len(string), length))


voice.setup(bot)

random.setup(bot)

lol.setup(bot)

bot.run(TOKEN)


"""
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send(
            'Psst, {0}. Use the prefix "!" instead of mentioning me to save time!'
            .format(message.author.mention))

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    return

@bot.command(name='god')
@commands.has_role('admin')
async def god_command(ctx):
    if not ctx.channel.name == CHANNEL_NAME:
        channel = discord.utils.find(lambda c: CHANNEL_NAME in c.name, ctx.guild.channels)
        await ctx.send(
            'Please use the text-channel <#{0}> instead to prevent spam!'
            .format(channel.id))
        return
    await ctx.send('God is speaking!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.event
async def on_error(event, *args):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write('Unhandled message: {0}\n'.format(args[0]))
            """