import random, string, time

from colorama import Fore, init

init(convert=True)

def Nitro(fileName):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    with open(fileName, 'a+') as f:
        f.write(code+'\n')

def Menu(fileName):
    print(f"[{Fore.GREEN}>{Fore.RESET}] How many codes do you want to generate?")
    amount = int(input(" > "))
    for _i in range(amount):
        Nitro(fileName)

def FormatedNitro(fileName):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    with open(fileName, 'a+') as f:
        f.write('https://discord.gift/'+code+'\n')

def FormatedMenu(fileName):
    print(f"[{Fore.GREEN}>{Fore.RESET}] How many codes do you want to generate?")
    amount = int(input(" > "))
    for _i in range(amount):
        FormatedNitro(fileName)

if __name__ == '__main__':
    print(f"[{Fore.GREEN}>{Fore.RESET}] Name of the file where to deposit the codes")
    fileName = input(" > ")
    print(f"[{Fore.GREEN}>{Fore.RESET}] How do you want the codes to look like?")
    print(f"""
        [{Fore.GREEN}1{Fore.RESET}] - https://discord.gift/KuqU5Hbuz4r4vthb
        [{Fore.GREEN}2{Fore.RESET}] - KuqU5Hbuz4r4vthb
    """)
    choice = int(input(" > "))  
    if choice == 1:
        FormatedMenu(fileName)
    elif choice == 2:
        Menu(fileName)
    else:
        print(f"[{Fore.RED}-{Fore.RESET}] Not a valid option!")
        time.sleep(5)
        exit(0)
