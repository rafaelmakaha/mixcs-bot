import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix=">", description="This is a helper bot!")

options = {
  '00' : 'Unranked',
  '01' : 'Prata 1',
  '02' : 'Prata 2',
  '03' : 'Prata 3',
  '04' : 'Prata 4',
  '05' : 'Prata elite',
  '06' : 'Prata elite mestre',
  '07' : 'Ouro 1',
  '08' : 'Ouro 2',
  '09' : 'Ouro 3',
  '10' : 'Ouro 4',
  '11' : 'AK 1',
  '12' : 'AK 2',
  '13' : 'AK X',
  '14' : 'Xerife',
  '15' : 'Águia 1',
  '16' : 'Águia 2',
  '17' : 'Supremo',
  '18' : 'Global',
}

players = {}

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

@bot.command()
async def patentes(ctx):
    content = []
    content.append('Valor  :  Patente')
    for item in list(options.items()):
        content.append(str(str(item[0] + '  :  ' + str(item[1]))))
    
    embed = discord.Embed(title='Patentes', description=('\n'.join(content)))
    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, name, weight):
    server = ctx.guild

    if server.id in players:
        players[server.id].append((name,weight))
    else:
        players[server.id] = [(name,weight)]
    
    await ctx.send(name + " adicionado.")

@bot.command()
async def queue(ctx):
    server = ctx.guild
    response = []

    if server.id in players:
        for index,name in enumerate(players[server.id]):
            response.append("{}. {}".format(index,name[0]))

        await ctx.send('\n'.join(response))
    else:
        await ctx.send("Não há nenhum jogador na fila.")

# Events
@bot.event
async def on_ready():
    print("The bot is ready!")

bot.run('Njk4OTQ1ODYzMzA5MDY2Mzgx.XpNPMw.hp3_VCNgqxI13JA7NW7mbDc_2Es')