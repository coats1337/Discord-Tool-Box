import discord, os, keep_alive, asyncio, datetime, pytz

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)

@tasks.loop(seconds=3)
async def stream():
  while True:
    date = datetime.datetime.now(pytz.timezone('Europe/Amsterdam')).strftime("%H:%M %p") # Replace this with ur timezone
    await asyncio.sleep(3)
    stream = discord.Streaming(
      name=date,
      url='https://www.twitch.tv/search?term=please+sex+me+daddy', 
    )
    await client.change_presence(activity=stream)

@client.event
async def on_connect():
  stream.start()

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
