# -*- coding: UTF-8 -*-
# ToolName   : BetterTool
# Author     : R0b327
# License    : MIT
# Language   : Python
# Env        : #!/usr/bin/env python3

import sys, socket, ctypes
from time		import sleep
from random		import choice
from sys		import argv
from os			import system, getcwd, makedirs
from datetime		import datetime
from urllib.parse	import urlparse
from getpass		import getpass
from threading		import Thread
from shutil		import which
from platform			import system as reset
from Crash.crash import CriticalError
try:
	import speedtest
	import httpx
	from bs4	import BeautifulSoup
except Exception as err:
	exit(err)

try:makedirs("screenshot")
except:pass

# Set date
SetDate = f"{datetime.now().month}-{datetime.now().day}-{datetime.now().year}" 
headers = {
      'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) BC3 iOS/3.12.7 (build 538; iPhone 11 Pro Max; iOS 14.7.1)'
}

# CMD clear and Settitle
def cmdClear():
	if reset().upper() == "WINDOWS":
		ctypes.windll.kernel32.SetConsoleTitleW(f"[+] BetterTool ~ [+] DEVELOPER: R0b327 ~ [+] DATE: {SetDate}")
		system('cls')
	else:
		system(f'echo -ne  "\033][+] BetterTool ~ [+] DEVELOPER: R0b327 ~ [+] DATE: {SetDate}\007"')
		system('clear')

cmdClear()

# Colors
class Color: 
	VIOLET = '\033[95m' 
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	RESET = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	

class BetterToolStart: 
	@staticmethod
	def connection_check():
		try:
			BetterToolHome.AnimationText("[*] Checking the connection... ")
			resp = httpx.get("https://www.google.com/", headers=headers)
			print(f"{Color.YELLOW}OK {round(resp.elapsed.total_seconds(), 3)} Seconds{Color.RESET}")
			sleep(2)
		except httpx.ReadTimeout:
			exit(f"{Color.RED}Connection Error{Color.RESET}")
		except httpx.ConnectError:
			exit(f"{Color.RED}Connection Error{Color.RESET}")
		except httpx.ConnectTimeout:
			exit(f"{Color.RED}Connection Error{Color.RESET}")
		except KeyboardInterrupt:
			exit()

	@staticmethod
	def lookup(target):
		resp = httpx.get(f"http://ip-api.com/json/{target}?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy,query,asname", headers=headers, timeout=30).json()
		print(f"""{Color.RED}╔═════════════════════════════════════════════════════╗
    {Color.CYAN}IP Address{Color.RED}:{Color.CYAN} {resp['query']}
    Country{Color.RED}:{Color.CYAN} {resp['continent']} {resp['country']} ({resp['countryCode']})
    Region{Color.RED}:{Color.CYAN} {resp['region']} ({resp['regionName']})
    City{Color.RED}:{Color.CYAN} {resp['city']}
    Zipcode{Color.RED}:{Color.CYAN} {resp['zip']}
    Timezone{Color.RED}:{Color.CYAN} {resp['timezone']}

    ISP{Color.RED}:{Color.CYAN} {resp['isp']}
    ASN{Color.RED}:{Color.CYAN} {resp['as']} {resp['asname']}

    Mobile{Color.RED}:{Color.CYAN} {resp['mobile']}
    VPN{Color.RED}:{Color.CYAN} {resp['proxy']}{Color.RED}
╚═════════════════════════════════════════════════════╝""")

	@staticmethod
	def screenshot(target):
		if urlparse(target).scheme == "":
			target =  f"https://{target}"
		print(f"{Color.GREEN}[*] Requests sent to website...")
		url = httpx.get(f"https://api.screenshotmachine.com/?key=d035cc&url={target}&device=desktop&dimension=1024xfull&cacheLimit=0&delay=10000&user-agent={headers}", timeout=30)
		if url.status_code == 200:
			with open(f"screenshot/{urlparse(target).netloc}.jpg", "wb") as img:
				img.write(url.content)
			print(f"""{Color.RED}
    ╔═════════════════════════════════════════════════════╗

    {Color.CYAN}  Title{Color.RED}: {Color.VIOLET}{httpx.get(target).text[httpx.get(target).text.find('<title>') +7: httpx.get(target).text.find('</title>')]}
    {Color.CYAN}  Website{Color.RED}: {Color.VIOLET}{target}
    {Color.CYAN}  Time of processing{Color.RED}: {Color.VIOLET}{Color.UNDERLINE}{round(url.elapsed.total_seconds(), 3)}{Color.RESET}{Color.VIOLET} Seconds
    {Color.CYAN}  Image saved to{Color.RED}: {Color.VIOLET}screenshot/{urlparse(target).netloc}.jpg
    {Color.RED}
╚═════════════════════════════════════════════════════╝""")

	@staticmethod
	def ipinfo(target):
		print(f"""{Color.RED}╔═════════════════════════════════════════════════════╗
    {Color.GREEN}
    {httpx.get(f"https://ipinfo.io/{target}/json?token=5c55b33f306004", headers=headers, timeout=30).text}
    {Color.RED}
╚═════════════════════════════════════════════════════╝""")

	def speedtest():
		try:
			spdt = speedtest.Speedtest()

			print(f"{Color.GREEN}[*] Loading Server List...")
			spdt.get_servers()
			sleep(0.1)

			print(f"{Color.GREEN}[*] Choosing Best Server...")
			get = spdt.get_best_server()
			sleep(0.1)

			print(f"{Color.GREEN}[+] Host: {Color.YELLOW}{get['host']}")
			sleep(0.1)
			print(f"{Color.GREEN}[+] Location: {Color.YELLOW}{get['name']}")

			print(f"{Color.GREEN}[*] Performing Download Test...")
			download_result = spdt.download()

			print(f"{Color.GREEN}[*] Performing Upload Test...")
			upload_result = spdt.upload()
			ping_result = spdt.results.ping

			sleep(0.1)
			print(f"{Color.YELLOW}[+] Your Network Speed Results:")
			sleep(0.1)
			print(f"{Color.GREEN}[+] Download Speed: {Color.YELLOW} {download_result / 1024 / 1024:.2f} mbps")
			sleep(0.1)
			print(f"{Color.GREEN}[+] Upload Speed: {Color.YELLOW} {upload_result / 1024 / 1024:.2f} mbps")
			sleep(0.1)
			print(f"{Color.GREEN}[+] Ping: {Color.YELLOW} {ping_result:.2f} ms")
		except Exception:
			print(f"{Color.RED}Error: Check your Internet Connection.\n\n")



class BetterToolHome:
    @staticmethod
    def AnimationText(text):
        try:
            for animated in text:
                sys.stdout.write(animated)
                sys.stdout.flush()
                if animated != ".": sleep(0.01)
                else:
                    sleep(0.1)
        except KeyboardInterrupt:
            exit()

    @staticmethod
    def Banner():
        cmdClear()
        return f"""{Color.GREEN}{Color.BOLD}
         ______     ______     ______   ______   ______     ______     ______   ______     ______     __        
        /\  == \   /\  ___\   /\__  _\ /\__  _\ /\  ___\   /\  == \   /\__  _\ /\  __ \   /\  __ \   /\ \       
        \ \  __<   \ \  __\   \/_/\ \/ \/_/\ \/ \ \  __\   \ \  __<   \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  
         \ \_____\  \ \_____\    \ \_\    \ \_\  \ \_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_____\  \ \_____\ 
          \/_____/   \/_____/     \/_/     \/_/   \/_____/   \/_/ /_/     \/_/   \/_____/   \/_____/   \/_____/ 

                                                    WELCOME HERE
            PLEASE READ:
            USING THIS PROJECT FOR ILLEGAL ACTIVITIES IS AT YOUR OWN RISK!
	    I'M NOT RESPONSIBLE FOR ANY OF YOUR TAKEN ACTIONS!
		
		Type "help" To get Started!                     Contact Dev: https://m.me/R0b327

{Color.RESET}"""

    def showhelp():
        print(f"""{Color.RED}                         ╔═════════════════════════════════════════════════════╗
                         ║{Color.CYAN}    BetterTool Available Tools/Commands & Methods{Color.RED}    ║
                         ║   <═══════════════════════════════════════════>     ║
                         ║                                                     ║
                         ║  {Color.CYAN}{Color.UNDERLINE}help{Color.RESET}{Color.RED} - {Color.VIOLET}Show All Commands, Tool & Methods{Color.RED}           ║
                         ║  {Color.RED}!{Color.CYAN}ipinfo{Color.RED} - {Color.VIOLET}Get Information from IP address [ip] {Color.RED}    ║
                         ║  {Color.RED}!{Color.CYAN}lookup{Color.RED} - {Color.VIOLET}Get Details of Your Target [url, domain]{Color.RED} ║
                         ║  {Color.RED}!{Color.CYAN}screenshot{Color.RED} - {Color.VIOLET}Make Screenshot of any Websites{Color.RED}      ║
                         ║  {Color.CYAN}speedtest{Color.RED} - {Color.VIOLET}Connection Speedtest{Color.RED}                   ║
                         ║  {Color.CYAN}exit{Color.RED} - {Color.VIOLET}Exit/Quit the Program{Color.RED}                       ║
                         ║                                                     ║
                         ╚═════════════════════════════════════════════════════╝
""")


    @staticmethod
    def Command():
        print(BetterToolHome.Banner())
        try:
            while True:
                sys.stdout.write(f"{Color.BOLD}{Color.VIOLET}╔═══{Color.CYAN}[{Color.VIOLET}root@{socket.gethostbyname(socket.gethostname())}{Color.CYAN}]{Color.RED}-{Color.CYAN}[{Color.VIOLET}{getcwd()}/{argv[0]}{Color.CYAN}]{Color.VIOLET}\n╚══>{Color.RESET} ")
                cmd = input()
                args = cmd.split(' ')
                data = args[0].upper()
                if cmd in ["help", "HELP"]:
                    BetterToolHome.showhelp()
                elif cmd in ["sysinfo", "osinfo"]:
                      CriticalError()
                elif cmd in ['clear', 'cls', 'CLEAR', 'CLS']:
                    cmdClear()
                    print(BetterToolHome.Banner())
                elif cmd in ['speedtest', 'SPEEDTEST']:
                      BetterToolStart.speedtest()
                elif cmd in ["exit", "quit"]:
                    option = input(f"{Color.RED}[!] Are you sure you want to exit?(Y/N){Color.RED}: {Color.RESET}")
                    if option in ["y", "Y", "Yes", "YES"]:
                        exit(f"{Color.GREEN}Thanks for using!{Color.RESET}")
                    elif option in ["n", "N", "no", "No", "NO"]:
                        pass
                try:
                    if data in ["!LOOKUP"]:
                        if args[1] == '':
                            print(f"{Color.BOLD}{Color.CYAN}EXAMPLE{Color.RED} - !{Color.CYAN}lookup {Color.CYAN}({Color.VIOLET}https://www.google.com{Color.CYAN})")
                        else:
                            BetterToolStart.lookup(urlparse(args[1]).netloc)
                except IndexError:
                    print(f"{Color.BOLD}{Color.CYAN}EXAMPLE{Color.RED} - !{Color.CYAN}lookup {Color.CYAN}({Color.VIOLET}https://www.google.com{Color.CYAN})")
                try:
                    if data in ["!SCREENSHOT"]:
                        if args[1] == '':
                            print(f"{Color.BOLD}{Color.CYAN}EXAMPLE{Color.RED} - !{Color.CYAN}screenshot {Color.CYAN}({Color.VIOLET}https://www.google.com{Color.CYAN})")
                        else:
                            BetterToolStart.screenshot(args[1])  
                except IndexError:
                      print(f"{Color.BOLD}{Color.CYAN}EXAMPLE{Color.RED} - !{Color.CYAN}screenshot {Color.CYAN}({Color.VIOLET}https://www.google.com{Color.CYAN})")
                try:
                    if data in ["!IPINFO"]:
                        if args[1] == '':
                            print(f"{Color.BOLD}{Color.CYAN}EXAMPLE{Color.RED} - !{Color.CYAN}ipinfo {Color.CYAN}({Color.VIOLET}8.8.8.8{Color.CYAN})")
                        else:
                            BetterToolStart.ipinfo(args[1])  
                except IndexError:
                      print(f"{Color.BOLD}{Color.CYAN}EXAMPLE{Color.RED} - !{Color.CYAN}ipinfo {Color.CYAN}({Color.VIOLET}8.8.8.8{Color.CYAN})")

        except KeyboardInterrupt:
            exit()


if __name__ == "__main__":
    BetterToolStart.connection_check()
    BetterToolHome.Command()
