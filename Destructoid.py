from requests import get 
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
from warnings import warn
from IPython.core.display import clear_output
from time import time

def main():
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url = 'https://www.destructoid.com/products-index.phtml?date_s=desc&filt=reviews&category=&display=&name_s=&alpha='
    response = get(url, headers=header)
    print(response)
    
    html_soup = BeautifulSoup(response.text, 'html.parser')
    
    game_container = html_soup.find_all('div', class_='mod-4col')
    print(len(game_container))
    first_game = game_container[0]
    #print(first_game)
    
    game_title = first_game.h1.a.text
    print(game_title)
    game_score = float(first_game.find('div', class_='gscore').text)
    print(game_score)
    #review_date = first_game.find('span', class_='datePublished').text
    #print(review_date)
    platforms = first_game.find('div', class_='gplatforms')
    print(platforms)
    
    game = []
    score = []
    requests = 0
    start_time = time()
    
    for i in range(1,5):
        print('iteration', '', i)
        header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = get('https://www.destructoid.com/products-index.phtml?filt=reviews&date_s=desc&category=')
        print(response)
        sleep(randint(8,15))
        requests+=1
        elapsed_time = time() - start_time
        #Print how long each request takes
        print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)
        
        #If request is not 200, print current request code
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))    
            
        #Make sure request do not exceed certain limit
        if requests > 4:
            warn('Number of requests was greater than expected.')  
            break
        
        #Receive the response from website url and create an html parse
        html_soup = BeautifulSoup(response.text, 'html.parser')
        #Find the ultimate div for each game info and start parsing
        game_info = html_soup.find_all('div', class_='mod-4col')
        
        for container in game_info:
            if container.find('div', class_='gplatforms').text is not 'Film or TV':
                game_title = container.h1.a.text
                game.append(game_title)
                game_score = float(container.find('div', class_='gscore').text)
                score.append(game_score)
            
    info = pd.DataFrame({'game': game,
                         'score': score})
    print(info.values)    
        
main()