#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import modules
from requests import get
from bs4 import BeautifulSoup
from translate import durka as launage


# Getting launage
input_string=launage['Input_string']
launage_str=launage['launage_string']
first_use=launage['First']
last_use=launage['Last']
torrent_category=launage['Category']
name_torrent=launage['Name']
size_torrent=launage['Size']
savechoice=launage['Savechoice']


# Request headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36",
    "Connection": "keep-alive",
    "Host": "iknowwhatyoudownload.com",
    "Referer": "https://iknowwhatyoudownload.com"
}

print(r"""
  _____                                        _       ____                  _                  
 |_   _|   ___    _ __   _ __    ___   _ __   | |_    / ___|    ___    ___  | | __   ___   _ __ 
   | |    / _ \  | '__| | '__|  / _ \ | '_ \  | __|   \___ \   / _ \  / _ \ | |/ /  / _ \ | '__|
   | |   | (_) | | |    | |    |  __/ | | | | | |_     ___) | |  __/ |  __/ |   <  |  __/ | |   
   |_|    \___/  |_|    |_|     \___| |_| |_|  \__|   |____/   \___|  \___| |_|\_\  \___| |_|   
                                                                            > Created by LimerBoy,

                                                                           Forked by AnonimQwerty
                                                                           My blog: @anonims_blog
""")

# Get user input
ip = input(f"{input_string}: ")
save=input(f'{savechoice}').lower()
print('\n')

# Get request
page = get(f"https://iknowwhatyoudownload.com/{launage_str}/peer/?ip=" + ip,
           headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find(class_="table").find("tbody")
torrents = table.find_all("tr")
results=[]

# Show torrents table
for torrent in torrents:
    first, last = torrent.find_all(class_="date-column")
    first, last = first.text, last.text
    category = torrent.find(class_="category-column").text
    name = torrent.find(class_="name-column").text.replace("\n", '').replace('    ', '')
    size = torrent.find(class_="size-column").text
    result=f'{first_use}{first}, {last_use}{last}, {torrent_category}{category}, {name_torrent}{name}, {size_torrent}{size}\n\n'
    results.append(result)
    print(f'{first_use}{first}, {last_use}{last}, {torrent_category}{category}, {name_torrent}{name}, {size_torrent}{size}\n')

if save=='y':
  with open('result.txt', 'a', encoding='utf-8') as f:
    f.write(f'==========={ip}==========\n\n')
    for i in results:
      f.write(i)
