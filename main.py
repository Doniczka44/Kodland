import discord
import os, random
import requests
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def word(ctx, slowo):
    slowo = slowo.upper()
    slownik = {'LOL': 'odpowiedź na coś zabawnego',
               'CRINGE': 'coś dziwnego lub wstydliwego',
               'ROFL': 'odpowiedź na żart',
               'SHEESH': 'lekka dezaprobata',
               'CREEPY': 'straszny, złowieszczy',
               'AGGRO': 'stać się agresywnym/zły'}

    if slowo in slownik:
        await ctx.send(slownik[slowo])
    else:
        await ctx.send('Słowo nierozpoznane')


@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    with open('images/program_meme.jpg', 'rb') as g:
        picture = discord.File(g)
        await ctx.send(file=picture)

recykling_lista = {
    'plastik' : ['butelka plastikowa'],
    'metal' : ['puszka'],
    'szkło' : ['butelka szklana'],
    'papier' : ['karton'],
    'bio' : ['cebula']
}

rozklad_lista = {
    'szkło' : 'nie rozkłada się',
    'papier' : 'pół roku',
    'metal' : '50-100 lat',
    'plastik' : '300-1000 lat',
    'bio' : '2-5 tygodni'
}

pomysly_rekodzielo = [
    'odlew gipsowy',
    'rzeźba drewniana',
    'dzban gliniany'
]

szkodliwe = ['plastik', 'spaliny', 'klej']
nieszkodliwe = ['metal','bio', 'papier']
@bot.command()
async def recykling(ctx, obiekt):
    obiekt = obiekt.lower()
    for i in recykling_lista:
        if obiekt in recykling_lista[i]:
            await ctx.send(i)
            break

@bot.command()
async def rozklad(ctx, obiekt):
    obiekt = obiekt.lower()
    if obiekt in rozklad_lista:
        await ctx.send(rozklad_lista[obiekt])
    else:
        await ctx.send('Nie wiem jak długo rozkłada się ten przedmiot')

@bot.command()
async def pomysl(ctx):
    await ctx.send(random.choice(pomysly_rekodzielo))

@bot.command()
async def szkodliwosc(ctx, obiekt):
    obiekt = obiekt.lower()
    if obiekt in szkodliwe:
        await ctx.send('szkodliwe')
    elif obiekt in nieszkodliwe:
        await ctx.send('nieszkodliwe')
    else:
        await ctx.send('nie wiem')

