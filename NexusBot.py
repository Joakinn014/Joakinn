import discord
import random
import asyncio
from discord.ext import commands 
import os
import requests

TOKEN = "Tu Token Aquí"

intents = discord.Intents.default()
intents.message_content = True #Lee y responde con mensajes

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)

class MyClient(discord.Client):
    @client.event
    async def on_ready(self):
        print(f"Bot conectado como {client.user}")

    @client.event
    async def on_message(self, message):
        saludos = ["Hola", "¿Cómo estás?", "¿Qué tal?", "¡Ey!", "¡Hey!", "¡Qué onda!", "¡Pura vida!"]
        if message.author == client.user:
            return #Evitar que el bot se responda a si mismo
            
        if message.content in saludos:
            await message.channel.send(f"{random.choice(saludos)} {message.author.name}")   

        if message.content.startswith('$Adivina'):
            await message.channel.send('Adivina un numero del 1 al 10')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Lo siento, te demoraste mucho, era el {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('Estas en lo correcto!')
            else:
                await message.channel.send(f'Oops. Era el número {answer}.')


@bot.command()
async def meme(ctx):
    img_meme = random.choice(os.listdir("images"))
    with open(f"images/{img_meme}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

client = MyClient(intents=intents)
bot.run(TOKEN)#Esto siempre va de ultimo en el codigo