import requests
import colorama
import os
import sys
import time
import socks
import socket
from colorama import Fore
#Proxy info
socks.set_default_proxy(socks.SOCKS4, "1.1.1.1", 9999)
socket.socket = socks.socksocket
 
def lgin():
# Login creditentials
    url = "https://www.example.com/login" # Change the Webiste Here
    data = {"username": "myusername", "password": "mypassword"} # Go on the html login page and if the login input has another name then change it by this name (same for password)
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Elusive@Root> Login successful!")
    else:
        print("Elusive@Root> Login failed.")
 
def check_proxy(proxy_url):
    proxy = {'http': 'http://' + proxy_url, 'https': 'https://' + proxy_url}
 
    try:
        response = requests.get('https://www.google.com', proxies=proxy, timeout=5)
        if response.status_code == 200:
            print("Proxy is online")
        else:
            print("Proxy is offline")
    except:
        print("Proxy is offline")
 
def main():
    print(f"""
    {Fore.RED}
███████╗██╗     ██╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
██╔════╝██║     ██║   ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
█████╗  ██║     ██║   ██║███████╗ ╚███╔╝ ██║   ██║█████╗  
██╔══╝  ██║     ██║   ██║╚════██║ ██╔██╗ ╚██╗ ██╔╝██╔══╝  
███████╗███████╗╚██████╔╝███████║██╔╝ ██╗ ╚████╔╝ ███████╗
╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
 
[1] Start Script    [3] Help
[2] Proxy Status    [4] Exit
 
""")
    command = input("Elusive@User>")
 
    if command == "1":
        print("Starting Script")
        lgin()
 
    if command == "2":
        print("Enter your proxy ip : X.X.X.X:XXXX")
        proxy_url = input(">")
        check_proxy(proxy_url)
 
    if command == "3":
        print("""
    Go the Html login page you're trying to log into
    Press F12 or Right Click into Inspect
    Search for the Username / Login and Password Input
    replace with the ones in the script, data variable (username and password)
    put the site you want to login in url variable
    change the proxy info with yours
 
    now everything is setup for anonymous login
    /!\ Does not bypass Captcha for the moment
        """)
    if command == "4":
        sys.exit()
 
 
 
def onstart():
    cmd = '128,28'
    os.system(cmd)
    os.system('title Elusive - Public && cls')
    main()

onstart()