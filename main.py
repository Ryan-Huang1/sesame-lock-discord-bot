import discord
from discord.ext import commands
import os
import requests
import json
from keep_alive import keep_alive

client = commands.Bot(command_prefix = '!')

statusUrl = "https://api.candyhouse.co/public/sesame/"

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name='Sesame Bot | !help'))
  print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client. latency * 1000)}ms')

@client.command()
async def test(ctx, *, question):
    print('command called')
    await ctx.send(question)

keep_alive()
client.run(os.getenv('TOKEN'))