import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE2ODg5MzAzMTI5MDc4NTg0Mw.GEM5RW.l-OoVJ2b7IdJx2s8f_DiYuq0n0vO6RyLtYgpsw")

@bot.command()
async def how_to_reduce_trash(ctx):
    await ctx.send(''' 
                   - throw the trash into the trash bin
                   - seperate the organic ones and the unorganic ones
                   - make muck (fertilizer) out of the organic trashes
                   - clean the place that has trash daily
                   - do not litter 
                   ''')
