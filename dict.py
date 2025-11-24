import discord
from discord.ext import commands

user_dictionary = {}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def add(ctx, word: str, *, definition: str):
    user_dictionary[word.lower()] = definition
    await ctx.send(f"Added '{word}': {definition}")

@bot.command()
async def define(ctx, word: str):
    definition = user_dictionary.get(word.lower())
    if definition:
        await ctx.send(f"{word}: {definition}")
    else:
        await ctx.send(f"'{word}' not found in the dictionary.")

@bot.command()
async def listwords(ctx):
    if not user_dictionary:
        await ctx.send("No words stored yet.")
    else:
        words = ", ".join(user_dictionary.keys())
        await ctx.send(f"Stored words: {words}")

bot.run("YOUR_BOT_TOKEN")
