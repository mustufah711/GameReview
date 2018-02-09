# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 23:06:04 2018

@author: HARSHA
"""

import requests as r
import pandas as pd
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://www.polygon.com/games/reviewed'
result = r.get(url, headers=header)
print(result.status_code)

page = BeautifulSoup(result.content, 'html.parser')

name = []
score = []
platforms = []
release = []
publisher = []
developer = []
reviewed = []

temp = page.find('ul', class_ = 'm-game--index__list')

#get the score of the game
s = temp.find_all('em')
for i in s:
    score.append(float(i.text))

#get the name of the game 
n = temp.find_all('h3')
for i in n:
    name.append(i.a.text.strip())
 
info = page.find_all('div', class_ = 'm-game--index__game__meta meta')
for i in info:
    temp = i.ul.find_all('li')
    platforms.append(temp[0].text.strip())
    release.append(temp[1].strong.text)
    publisher.append(temp[2].strong.text)
    developer.append(temp[3].strong.text)
    reviewed.append(temp[4].strong.text)
        

db = pd.DataFrame({'name': name,
                   'score': score,
                   'platforms': platforms,
                   'release': release,
                   'publisher': publisher,
                   'developer': developer,
                   'reviewed': reviewed})
    
print(db)