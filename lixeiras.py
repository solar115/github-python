import discord
from discord.ext import commands
import random

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.event
async def on_message(message):

    if message.content.startswith('oi'):
        await message.channel.send("escolha um das cores de lixeira: vermelho, azul, verde, amarelo, marrom")
    
    if message.content.startswith('vermelho'):
        await message.channel.send("plásticos")

    elif message.content.startswith('azul'):
        await message.channel.send("papel/papelão")

    elif message.content.startswith('verde'):
        await message.channel.send("vidros")

    elif message.content.startswith('amarelo'):
        await message.channel.send("metal")

    elif message.content.startswith('marrom'):
        await message.channel.send("organicos")

    elif message.content.startswith('tchau'):
        await message.channel.send("\U0001f642")
