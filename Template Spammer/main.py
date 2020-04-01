import requests

errors = {
  1: 'Unauthorized'
}

def spamServers(token, template):
  with requests.Session() as session:
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
      'Authorization': token,
      'Content-Type': 'application/json'
    }
    payload = {
      'name': 'F',
      'icon': None
    }
    r = session.post('https://discordapp.com/api/v6/guilds/templates/{template}', headers=headers, json=payload)
    if errors[1] in r.text:
      print("[-] Invalid token")
    print(r.json())

if __name__ == '__main__':
  token = input("User token: ")
  template = input("Template ID: ")
  spamServers(token, template)
