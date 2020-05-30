#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import modules
from requests import get
from bs4 import BeautifulSoup
from colorama import Fore
from prettytable import PrettyTable

# Request headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36",
    "Connection": "keep-alive",
    "Host": "iknowwhatyoudownload.com",
    "Referer": "https://iknowwhatyoudownload.com"
}

print(rf"""{Fore.LIGHTGREEN_EX}
  _____                                        _       ____                  _                  
 |_   _|   ___    _ __   _ __    ___   _ __   | |_    / ___|    ___    ___  | | __   ___   _ __ 
   | |    / _ \  | '__| | '__|  / _ \ | '_ \  | __|   \___ \   / _ \  / _ \ | |/ /  / _ \ | '__|
   | |   | (_) | | |    | |    |  __/ | | | | | |_     ___) | |  __/ |  __/ |   <  |  __/ | |   
   |_|    \___/  |_|    |_|     \___| |_| |_|  \__|   |____/   \___|  \___| |_|\_\  \___| |_|   
                                                                           {Fore.LIGHTYELLOW_EX} > Created by LimerBoy
{Fore.RESET}
""")

# Get user input
ip = input(f" {Fore.LIGHTCYAN_EX}TorrentSeeker@target_ip : {Fore.LIGHTMAGENTA_EX}")

# Get request
page = get("https://iknowwhatyoudownload.com/en/peer/?ip=" + ip,
           headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find(class_="table").find("tbody")
torrents = table.find_all("tr")
output = PrettyTable(["Name", "Category", "Size", "First seen", "Last seen"])

# Show torrents table
for torrent in torrents:
    first, last = torrent.find_all(class_="date-column")
    first, last = first.text, last.text
    category = torrent.find(class_="category-column").text
    name = torrent.find(class_="name-column").text.replace("\n", '')
    size = torrent.find(class_="size-column").text
    output.add_row([name, category, size, first, last])

print(f" {Fore.YELLOW}Found {len(torrents)} torrents... \n{Fore.LIGHTGREEN_EX}{output}{Fore.RESET}")
