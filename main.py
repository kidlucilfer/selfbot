import discord
import asyncio
import json
import sys
import time
import colorama
from colorama import Fore

client = discord.Client()

with open('config.json') as handle:
    soylindo = json.load(handle)
    token = (soylindo["token"])
    if token == "token":
        print ("Introduce un token en la config.json")
        time.sleep(5)
        sys.exit()

@client.event
async def on_ready():
    print(f'''{Fore.RED}
      ,ad8PPPP88b,     ,d88PPPP8ba,
 d8P"      "Y8b, ,d8P"      "Y8b
dP'           "8a8"           `Yd
8(              "              )8
I8                             8I
 Yb,                         ,dP
  "8a,                     ,a8"
    "8a,                 ,a8"
      "Yba             adP"
        `Y8a         a8P'
          `88,     ,88'
            "8b   d8"  Nike
             "8b d8"   Selfbot <3
              `888'
        '''+Fore.RESET)
    print (f"{Fore.BLACK}Logeado en el token: " + str(token))
    print (f'{Fore.YELLOW}--------------------')
    print (f'{Fore.BLUE}Usuario:')
    print (client.user.name)
    print (client.user.id)
    print (f'{Fore.YELLOW}--------------------')
    print (f"{Fore.MAGENTA}Prefijos: %%, $, #, ##, &&")

@client.event
async def k(message):
    if message.content == '%%':
        await message.delete()
        async for message in message.channel.history(limit=100000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    if message.content == '$':
        await message.delete()
        async for message in message.channel.history(limit=100000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    if message.content == '##':
        await message.delete()
        async for message in message.channel.history(limit=100000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    if message.content == '&&':
        await message.delete()
        async for message in message.channel.history(limit=100000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    if message.content == '#':
        await message.delete()
        async for message in message.channel.history(limit=100000).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
                    
client.run(token, bot=False)
