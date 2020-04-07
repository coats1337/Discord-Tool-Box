import requests, time

from colorama import Fore

print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook link ")
link = input(" > ")
print(f"[{Fore.GREEN}>{Fore.RESET}] Message to send ")
message = input(" > ")
print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook name ")
name = input(" > ")

payload = {
  'content': message,
  'username': name
}

while True:
  try:
    time.sleep(0.5)
    r = requests.post(link, json=payload)
    f = open('log.txt', 'a+') 
    if 'You are being rate limited.' in r.text:
      f.write('Ratelimited\n')
    else:
      f.write(f"Spammed {message}\n")  
    f.close()
    if r.status_code == 204:
      print(f"[{Fore.GREEN}+{Fore.RESET}] Sent message!")
    else:
      print(f"[{Fore.RED}-{Fore.RESET}] Ratelimit/Error")
  except requests.exceptions.MissingSchema:
    print(f"[{Fore.RED}-{Fore.RESET}] Not a real url");break
