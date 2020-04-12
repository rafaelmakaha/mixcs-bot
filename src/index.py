import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix=">", description="This is a helper bot!")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def sum(ctx, n1: int, n2: int):
    await ctx.send(n1 + n2)

@bot.command()
async def status(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}', 
    description="Alguma descrição", 
    timestamp=datetime.datetime.utcnow(), 
    color=discord.Color.blue())
    embed.add_field(name="Debug", value=discord.ClientUser.avatar)
    await ctx.send(embed=embed)


    

# Events
@bot.event
async def on_ready():
    print("The bot is ready!")

bot.run('')