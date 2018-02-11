# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 23:06:04 2018

@author: HARSHA
"""

import requests as r
import pandas as pd
from time import sleep
from time import time
from random import randint
from bs4 import BeautifulSoup

#where everything will be stored
name = []
score = []
platforms = []
release = []
publisher = []
developer = []
reviewed = []

#for keeping track of scraper and finding issues
request = 0
start_time = time()
log_file = open('PolygonLog.txt', 'w')
totaltime = 0
#header to avoid issues with websites not connecting 
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#number of pages scrapped
pages = 0
while (pages < 831):
    #connecting to the website and getting a response
    pages += 1
    url = 'https://www.polygon.com/games/reviewed/' + str(pages)
    result = r.get(url, headers=header)
    request += 1
    
    if(result.status_code != 200):
        print('Request: ' + str(request) + '; Failed.\n')
        log_file.write('Request: ' + str(request) + '; Failed.\n')
    else:   
        sleep(randint(5,10))      
        elapsed_time = time() - start_time
        totaltime += elapsed_time
        print('Request: ' + str(request) + '; Frequency: ' + str(elapsed_time / request) + ' sec/request\n')
        log_file.write('Request: ' + str(request) + '; Frequency: ' + str(elapsed_time / request) + ' sec/request\n')
        #get the list of all games on the page
        page = BeautifulSoup(result.content, 'html.parser')
        temp = page.find('ul', class_ = 'm-game--index__list')
        
        #get the score of the game
        s = temp.find_all('em')
        for i in s:
            score.append(float(i.text))
        
        #get the name of the game 
        n = temp.find_all('h3')
        for i in n:
            name.append(i.a.text.strip())
         
        #get the game data like publisher, dveloper, review dates etc...
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
    
db.to_csv('ploygon.csv')
log_file.write('AVG Time: ' + str(totaltime / request))
log_file.close()