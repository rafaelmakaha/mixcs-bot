import discord
from discord.ext import commands
import datetime
from mytoken import Auth

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

    if server.id in players and len(players[server.id]) > 0:
        for index,name in enumerate(players[server.id]):
            response.append("{}. {}".format(index,name[0]))

        await ctx.send('\n'.join(response))
    else:
        await ctx.send("Não há nenhum jogador na fila.")

@bot.command()
async def remove(ctx, pos):
    server = ctx.guild
    response = ""

    if server.id in players:
        if len(players[server.id]) > int(pos):
            name = players[server.id].pop(int(pos))
            await ctx.send('{} removido da fila.'.format(name[0]))
        else:
            await ctx.send("Esta posição não exite na fila.")
    else:
        await ctx.send("Não há jogadores na fila.")

@bot.command()
async def clear(ctx):
    server = ctx.guild

    if server.id in players:
        players[server.id] = []
        await ctx.send("Todos os jogadores foram removidos.")
    else:
        await ctx.send("Não há jogadores na fila.")

# Events
@bot.event
async def on_ready():
    print("The bot is ready!")

a = Auth()

bot.run(a.TOKEN)