from requests import get 
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
from warnings import warn
from IPython.core.display import clear_output
from time import time

def main():
    
    #Arrays to store the name, gamescore and genre for each game
    names = []
    game_score = []
    genre = []
    platform = []
    requests = 0
    #Starting index for website
    j = '0'
    start_time = time()
    
    #Run through each page and retrieve data for each game based on tag
    for i in range(1,251):
        print('iteration', '', j)
        header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        #Retrieve website url 
        response = get('http://www.ign.com/reviews/games?startIndex='+j, headers=header)
        print(response)
        #Increment each value and then type cast to be parsed for next iteration
        j = int(j)+25
        j = str(j)
        #Between each request, go to sleep between 8 to 15 seconds to not overload server
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
        if requests > 250:
            warn('Number of requests was greater than expected.')  
            break
        
        #Receive the response from website url and create an html parse
        html_soup = BeautifulSoup(response.text, 'html.parser')
        #Find the ultimate div for each game info and start parsing
        game_info = html_soup.find_all('div', class_='clear itemList-item')
        
        #Now we individually parse each name, rating and genre based on div
        for container in game_info:
            name = container.h3.a.text.replace('\n','').encode('utf-8').strip()
            names.append(name)
            rating = container.find('span', class_='scoreBox-score')
            rating = float(rating.text.encode('utf-8').strip())
            game_score.append(rating)
            game_type = container.find('span', class_='item-genre').text.replace('\n','').encode('utf-8').strip()
            genre.append(game_type)
            platforms = container.find('span', class_='item-platform')
            platform.append(platforms.text.encode('utf-8').strip())
    
    #Store each entry into a panda DS and save it to CSV file since data deletes after every new request
    game_store = pd.DataFrame({'name': names,
                               'score': game_score,
                               'genres': genre,
                               'platform': platform})
    #See if entry stroage was successful by viewing how many entries were saved
    print(game_store.info())
    #Save to CSV
    game_store.to_csv('ign.csv')    
main()