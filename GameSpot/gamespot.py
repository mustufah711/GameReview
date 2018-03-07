# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:34:48 2018

@author: HARSHA
"""

import requests as r
import pandas as pd
from time import sleep
from time import time
from random import randint
from bs4 import BeautifulSoup

names = []
release_dates = []
reviewed_dates = []
score = []
platforms = []
devlopers = []
publishers = []
genres = []
user_score = []


header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://www.gamespot.com'
start_time = time()
request = 0
for page_num in range(501, 601):
    result = r.get((url + '/reviews/?page=' + str(page_num)), headers=header)
    #print(result.status_code)
    request += 1
    print('Request: ' + str(request))
    soup = BeautifulSoup(result.content, 'html.parser')
    
    articles = soup.find_all('article', class_='media media-game media-game')
    
    #print(len(articles))
    
    for article in articles:
        game = r.get((url + article.a.get('href')), headers=header)
        soup2 = BeautifulSoup(game.content, 'html.parser')
        
        if(soup2.find('title').text.strip() != 'Busted - GameSpot'):
            #name
            names.append(str((soup2.find('dt', class_='pod-objectStats-info__title').text.strip())[:-9].strip()))
            #print(str((soup2.find('dt', class_='pod-objectStats-info__title').text.strip())[:-9].strip()))
            #release date
            release_dates.append(soup2.find('dd', class_='pod-objectStats-info__release').li.span.text.strip())
            
            #review date
            reviewed_dates.append(soup2.find('h3', class_='news-byline').time.text.strip()[:12])
            
            #publiser rateing
            score.append(float(soup2.find('div', class_='gs-score__cell').text.strip()))
            
            #platforms
            plat_list = soup2.find('dd', class_='pod-objectStats-info__systems').find_all('li')
            plat = ''
            for i in range(len(plat_list)):
                #print(plat_list[i].get('class')[2])
                if(plat_list[i].get('class')[2] != 'js-unhide-list'):
                    if (i == 0):
                        plat = plat + plat_list[i].text.strip()
                    else:
                        plat = plat + ',' + plat_list[i].text.strip()
            platforms.append(str(plat))
                        
            #user rateing
            user_rate = soup2.find('dl', class_='breakdown-reviewScores__userAvg align-vertical--child')
            if user_rate is not None:
                user_score.append(float(soup2.find('dl', class_='breakdown-reviewScores__userAvg align-vertical--child').a.text.strip()))
            else:
                user_score.append(None)
            
            #container for info (devs, pubs, ganres)
            info_list = soup2.find('dl', class_='pod-objectStats-additional').find_all('dd')
            if len(info_list) >= 3:           
                #devs
                dev = info_list[0].text.strip()
                devlopers.append(str(dev))
                
                #pubs
                pub = info_list[1].text.strip()
                publishers.append(str(pub))
                
                #gens
                gen = info_list[2].text.strip()
                genres.append(str(gen))
                
            else:
                devlopers.append(None)
                publishers.append(None)
                genres.append(None)
            
            sleep(randint(1, 3))

total_time = time()-start_time
print(total_time)    
db = pd.DataFrame({'name': names,
                   'score': score,
                   'platforms': platforms,
                   'release_date': release_dates,
                   'review_date': reviewed_dates,
                   'publisher': publishers,
                   'developer': devlopers,
                   'genres': genres,
                   'user_score': user_score})

db.to_csv('gamespot6.csv')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    