import discord, os, keep_alive, asyncio, datetime, pytz, re, requests

from colorama import Fore
from discord.ext import commands

class disClient(commands.Bot):
  def __init__(self):
    super().__init__(
      command_prefix=':',
      self_bot=True
    )
    self.session = requests.Session()
    self.token = os.getenv("TOKEN")
    self.remove_command('help')
    self.errors = {
      1: '{"message": "Unknown Gift Code", "code": 10038}',
      2: 'subscription_plan',
      3: 'You are being rate limited',
      4: 'Access denied'
    }

  async def stream(self):
    while True:
      date = datetime.datetime.now(pytz.timezone('Europe/Madrid')).strftime("%H:%M %p")  
      await asyncio.sleep(3)
      stream = discord.Streaming(
        name=date,
        url='https://www.twitch.tv/search?term=please+esex+me+daddy', 
      )
      await disClient.change_presence(self, activity=stream)

  async def on_connect(self):
    await self.stream()

  async def on_message(self, message):
    try:
      code = re.search(r'(discord.gift|discordapp.com/gifts)/\w{16,24}', message.content).group(0)
      if code:
        r = self.session.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code.replace("discord.gift/", "")}/redeem', headers=self.getHeaders())
        if self.errors[1] in r.text:
          self.returnData('INVALID CODE', code, message.guild, message.author)
          self.Save('logger.log', 'a+', f'[WARN] Invalid Code {code} | {message.guild} | {message.author}')
        elif self.errors[2] in r.text:
          self.returnData('CLAIMED', code, message.guild, message.author)
          self.Save('logger.log', 'a+', f'[INFO] Claimed Code {code} | {message.guild} | {message.author}')
        elif self.errors[3] in r.text:
          self.returnData('RATELMITED', code, message.guild, message.author)
          self.Save('logger.log', 'a+', '[WARN] Ratelimited')
        elif self.errors[4] in r.text:
          self.returnData('DENIED', code, message.guild, message.author)
          self.Save('logger.log', 'a+', '[WARN] Denied')
        else:
          self.returnData('UNKNOWN', code, message.guild, message.author)
          self.Save('logger.log', 'a+', f'[WARN] Unknown Code {code} | {message.guild} | {message.author}')
    except (AttributeError):
      pass

  def returnData(self, status, code, value1, value2):
    if status == 'INVALID CODE' or 'DENIED':
      perhaps = Fore.RED
    elif status == 'ALREADY REDEEMED' or 'RATELIMITED' or 'UNKNOWN':
      perhaps = Fore.YELLOW
    else:
      perhaps = Fore.GREEN
    data = print(f'[{perhaps}{status}{Fore.RESET}] - [{Fore.CYAN}{code}{Fore.RESET}] - [{Fore.YELLOW}{value1}{Fore.RESET}] - [{Fore.YELLOW}{value2}{Fore.RESET}]')
    return data

  def getHeaders(self):
    headers = {
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
      'Authorization': self.token
    }
    return headers

  def Save(self, fileName, mode, info):
    return open(fileName, mode).write(info+'\n')

  def run(self):
    super().run(self.token, bot=False)

if __name__ == '__main__':
  client = disClient()
  keep_alive.keep_alive()
  client.run()
