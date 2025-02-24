import discord
import random
import asyncio

TOKEN = "Tu token aquí"

intents = discord.Intents.default()
intents.message_content = True #Lee y responde con mensajes

client = discord.Client(intents=intents)

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


client = MyClient(intents=intents)
client.run(TOKEN)#Esto siempre va de ultimo en el codigo