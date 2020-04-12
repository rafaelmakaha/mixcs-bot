import discord

from discord.txt import commands

commands.Bot(command_prefix=">", description="This is a helper bot!")

@bot.command()
def ping(ctx):
    ctx.send("pong")