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
    platforms = first_game.find('div', class_='gplatforms').find_all('a')
    #print(platforms[1].text)
    a = 0
    pal = ''
    for i in platforms:
        if(a==len(platforms)-1):
            pal = pal + i.text
        else:
            pal = pal + i.text + ','
        a+=1
    
    print(pal)
    game = []
    score = []
    #platform = []
    requests = 0
    j = '0'
    start_time = time()
    """
    for i in range(1,5):
        print('iteration', '', i)
        header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = get('https://www.destructoid.com/products-index.phtml?filt=reviews&date_s=desc&category=&nonce=1518737806537&start='+j, headers = header)
        print(response)
        j = int(j)+25
        j = str(j)
        sleep(randint(5,7))
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
        game_platform = html_soup.find('div', class_='gplatforms')
        
        for container in game_info:
            if container.find('div', class_='gplatforms').text != 'Film or TV':
                game_title = container.h1.a.text
                game.append(game_title)
                game_score = container.find('div', class_='gscore').text
                score.append(game_score)
                for s in game_platform:
                    
    """     
    info = pd.DataFrame({'game': game,
                         'score': score})
    #print(info.values)    
        
main()