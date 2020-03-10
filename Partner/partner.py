import discord, json

from discord.ext import commands
from colorama import Fore, init

init(convert=True)

with open('config.json') as f:
    config = json.load(f)

prefix = config.get('prefix')
token = config.get('token')

Partner = discord.Client()
Partner = commands.Bot(
    command_prefix=prefix
)
Partner.remove_command('help')

@Partner.event
async def on_ready():
    print(f"   [{Fore.GREEN}+{Fore.RESET}] Logged in:")
    print(f'''

   {Fore.GREEN}+{Fore.RESET} Username: {Partner.user.name}
   {Fore.GREEN}+{Fore.RESET} ID: {Partner.user.id}
   _______________________________________________________
    ''')

def CogLoader():
    cogs = [
        'cogs.partner'
    ]
    for e in cogs:
        Partner.load_extension(e)

@Partner.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention} | This command is on cooldown!")

@Partner.command()
async def help(ctx):
    em = discord.Embed(description="JustPartner Bot")
    em.add_field(
        name="`-partner (message)`", 
        value="\n| Usage: *-partner nitro giveaway in (discord invite) at 9pm, make sure to join!*\n | What this command does: Picks a random server and dms everyone in that random selected server with the specified message"
    )
    await ctx.send(embed=em)

if __name__ == '__main__':
    CogLoader()
    Partner.run(token)
