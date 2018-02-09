from requests import get 
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
from warnings import warn
from IPython.core.display import clear_output
from time import time

def main():
    
    names = []
    game_score = []
    genre = []
    requests = 0
    j = '25'
    start_time = time()
 
    for i in range(1,4):
        print('iteration', '', j)
        header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = get('http://www.ign.com/reviews/games?startIndex='+j, headers=header)
        print(response)
        j = int(j)+25
        print(type(j), 'is it int?')
        j = str(j)
        print(type(j))
        sleep(randint(8,15))
        requests+=1
        elapsed_time = time() - start_time
        print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))    
        if requests > 3:
            warn('Number of requests was greater than expected.')  
            break
        html_soup = BeautifulSoup(response.text, 'html.parser')
        game_info = html_soup.find_all('div', class_='clear itemList-item')
        
        for container in game_info:
            name = container.h3.a.text.replace('\n','').encode('utf-8').strip()
            names.append(name)
            rating = container.find('span', class_='scoreBox-score')
            rating = float(rating.text.encode('utf-8').strip())
            game_score.append(rating)
            game_type = container.find('span', class_='item-genre').text.replace('\n','').encode('utf-8').strip()
            genre.append(game_type)
    
    game_store = pd.DataFrame({'name': names,
                               'score': game_score,
                               'genres': genre})
    print(game_store.info())
    #print(game_store.values)
    #print(game_store.head(50))
    game_store.to_csv('test2.csv')    
main()