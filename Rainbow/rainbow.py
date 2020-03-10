import discord, json, random

from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
is_bot = config.get('is_bot')

Rainbow = discord.Client()
if is_bot == True:
    bot = True
else:
    bot = False 

Rainbow = commands.Bot(
    command_prefix=prefix,
    self_bot=bot
)

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@Rainbow.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

Rainbow.run(token)
