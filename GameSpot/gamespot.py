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
score = []
platforms = []
release_dates = []
reviewed_dates = []
devlopers = []
publishers = []
genres = []
rating = []
user_score = []
reviews = []

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://www.gamespot.com'

result = r.get((url + '/reviews/'), headers=header)
print(result.status_code)


soup = BeautifulSoup(result.content, 'html.parser')

articles = soup.find_all('article', class_='media media-game media-game')

print(len(articles))


for article in articles:
    game = r.get((url + article.a.get('href')), headers=header)
    soup2 = BeautifulSoup(game.content, 'html.parser')
    print((soup2.find('dt', class_='pod-objectStats-info__title').a.text.strip())[:-9].strip())
    print(soup2.find('span', itemprop='datePublished').text)
    print(soup2.find('span', itemprop='ratingValue'))
    print(soup2.find('ul', class_='system-list').text)
    sleep(randint(1, 3))