import discord
from discord.ext import commands
import datetime
import random
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

# @bot.command()
# async def status(ctx):
#     embed = discord.Embed(title=f'{ctx.guild.name}', 
#     description="Alguma descrição", 
#     timestamp=datetime.datetime.utcnow(), 
#     color=discord.Color.blue())
#     embed.add_field(name="Debug", value=discord.ClientUser.avatar)
#     await ctx.send(embed=embed)

@bot.command()
async def patentes(ctx):
    content = []
    content.append('Valor  :  Patente')
    for item in list(options.items()):
        content.append(str(str(item[0] + '  :  ' + str(item[1]))))
    
    embed = discord.Embed(title='Patentes', 
    description=('\n'.join(content)),
    color=discord.Color.magenta())
    await ctx.send(embed=embed)

@bot.command()
async def add(ctx, name, weight: int):
    server = ctx.guild

    if weight < 0 or weight > 18:
        embed = discord.Embed(title="MixCS", 
        description="Valor fora dos pesos das patentes.",
        color=discord.Color.magenta())
        return await ctx.send(embed=embed)

    if server.id in players:
        if len(players[server.id]) < 10:
            players[server.id].append((name,weight))
        else:
            embed = discord.Embed(title="MixCS", 
            description="Não há espaço para mais jogadores.",
            color=discord.Color.magenta())
            return await ctx.send(embed=embed)
    else:
        players[server.id] = [(name,weight)]
    embed = discord.Embed(title="MixCS", 
    description=f'{name} adicionado.',
    color=discord.Color.magenta())
    await ctx.send(embed=embed)

@bot.command()
async def queue(ctx):
    server = ctx.guild
    response = []

    if server.id in players and len(players[server.id]) > 0:
        for index,name in enumerate(players[server.id]):
            response.append("{}. {}".format(index+1,name[0]))

        embed = discord.Embed(title="MixCS", 
        description=('\n'.join(response)),
        color=discord.Color.magenta())
        return await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="MixCS", 
        description="Não há nenhum jogador na fila.",
        color=discord.Color.magenta())
        return await ctx.send(embed=embed)

@bot.command()
async def remove(ctx, pos: int):
    server = ctx.guild
    response = ""
    pos = pos - 1
    if server.id in players:
        if len(players[server.id]) > int(pos):
            name = players[server.id].pop(int(pos))
            embed = discord.Embed(title="MixCS", 
            description="{} removido da fila.".format(name[0]),
            color=discord.Color.magenta())
            return await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="MixCS", 
            description="Esta posição não exite na fila.",
            color=discord.Color.magenta())
            return await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="MixCS", 
        description="Não há jogadores na fila.",
        color=discord.Color.magenta())
        return await ctx.send(embed=embed)

@bot.command()
async def clear(ctx):
    server = ctx.guild

    if server.id in players:
        players[server.id] = []
        embed = discord.Embed(title="MixCS", 
        description="Todos os jogadores foram removidos.",
        color=discord.Color.magenta())
        return await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="MixCS", 
        description="Não há jogadores na fila.",
        color=discord.Color.magenta())
        return await ctx.send(embed=embed)

@bot.command()
async def run(ctx):
    server = ctx.guild

    if server.id in players:# and len(players[server.id]) == 10:
        jogadores = players[server.id]
        jogadores = sorted(jogadores, reverse=True, key=lambda elem: elem[1])

        t1 = []
        t2 = []
        tier1 = jogadores[:2]
        tier2 = jogadores[2:6]
        tier3 = jogadores[6:]

        t1.append(tier1.pop(tier1.index(random.choice(tier1))))
        t2.append(tier1.pop(tier1.index(random.choice(tier1))))

        while len(t1) < 5 and len(t2) < 5:
            t1.append(tier2.pop(tier2.index(random.choice(tier2))))
            t2.append(tier2.pop(tier2.index(random.choice(tier2))))
            t1.append(tier3.pop(tier3.index(random.choice(tier3))))
            t2.append(tier3.pop(tier3.index(random.choice(tier3))))
        
        response1 = []
        response2 = []
        for index in range(5):
            response1.append("{}. {}".format(index+1,t1[index][0]))
            response2.append("{}. {}".format(index+1,t2[index][0]))
        
        embed = discord.Embed(title="MixCS", 
        description="Times sorteados",
        color=discord.Color.magenta())
        embed.add_field(name="Time A", value="\n".join(response1))
        embed.add_field(name="Time B", value="\n".join(response2))
        return await ctx.send(embed=embed)
        # await ctx.send(t1)
        # await ctx.send(t2)
    else:
        embed = discord.Embed(title="MixCS", 
        description="Não há jogadores suficientes para formar os times.",
        color=discord.Color.magenta())
        return await ctx.send(embed=embed)

# Events
@bot.event
async def on_ready():
    print("The bot is ready!")

a = Auth()

bot.run(a.TOKEN)