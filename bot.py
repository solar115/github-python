import discord
from senha import gen_pass

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    if message.content.startswith('senha'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

@bot.command()
async def dado(ctx, min, max)
    resultado = random.randit(int(min)), (int(max)
    await ctx.send(resultado)
     
client.run("t")
