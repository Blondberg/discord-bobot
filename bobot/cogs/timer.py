import discord
from discord.channel import CategoryChannel
from discord.ext import commands


class Timer(commands.Cog, name="timer"):
    def __init__(self, bot):
        self.bot = bot

        self.time_left = 0

        self.flags = {
            "start": start,
            "stop": stop,
            "set": set,
            "help": help,
        }

    @commands.command(name="timer", description="Various timer functions")
    async def timer(self, ctx, flag="", *modifier):
        try:
            self.flags[flag](modifier)
        except KeyError:
            print(
                "The flag '{}' could not be found, sending help information instead".format(
                    flag
                )
            )
            help()


def start(modifier):
    print(modifier)


def stop(modifier):
    print("stop")


def set(modifier):
    print("set")


def help(modifier):
    print("help")


def setup(bot: commands.Bot):
    bot.add_cog(Timer(bot))
