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
    url = 'https://www.gamespot.com/reviews/?page=1'
    response = get(url, headers=header)
    print(response)
    
    html_soup = BeautifulSoup(response.text, 'html.parser')
    game_container = html_soup.find_all('article', class_='media media-game media-game')
    print(len(game_container))
    first_game = game_container[0]
    #print(first_game)
    
    game_name = first_game.h3.find('div', class_='media-body')
    print(game_name)

main()