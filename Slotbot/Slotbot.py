import discord, json

from colorama import Fore, init

init(convert=True)

client = discord.Client()

with open('config.json) as f:
  config = json.load(f)

token = config.get('token')

@client.event
async def on_message(message):
    if 'Someone just dropped' in message.content:
       if message.author.id == 346353957029019648:
          await ctx.channel.send('~grab')
       print(f"Stole some slotbot currency in: {Fore.GREEN}{message.channel}{Fore.RESET}  | {Fore.MAGENTA}{message.guild}{Fore.RESET}")
       
client.run(token)       
