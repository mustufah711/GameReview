from requests import get 
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
from warnings import warn
from IPython.core.display import clear_output
from time import time

def main():
    #Get url
    url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
    response = get(url)
    
    #Convert to BS object and parser indicates we will parse html DOM
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    
    #Find all classes with div for certain objects
    movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
    print(type(movie_containers))
    print(len(movie_containers))
    
    #Get first movie object and name
    first_movie = movie_containers[0]
    first_name = first_movie.h3.a.text
    print(first_name)
    
    #Get first movie year. [1:-1] strips first and last character
    first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
    first_year = first_year.text[1:-1]
    print(first_year)
    
    #Get rating of movie
    first_rating = float(first_movie.strong.text)
    print(first_rating)
    
    #Metascore rating
    meta_score = first_movie.find('span', class_='metascore favorable')
    meta_score = int(meta_score.text)
    print(meta_score)
    
    #Number of votes
    first_votes = first_movie.find('span', attrs={'name':'nv'})
    first_votes = int(first_votes['data-value'])
    print(first_votes)
    
    #Object without metacritic score
    movie = movie_containers[19].find('div', class_='ratings-metascore')
    print(type(movie))
    
    #Writing script to extract from each movie
    names = []
    years = []
    imdb_ratings = []
    metascore = []
    votes = [] 
    #Going to get first 4 pages for each year of 2000-2017
    pages = [str(i) for i in range(1,5)]
    years_url = [str(i) for i in range(2000,2018)]
    
    start_time = time()
    requests = 0
    
    for year_url in years_url:
        for page in pages:
            # Make a get request
            response = get('http://www.imdb.com/search/title?release_date=' + year_url + 
                           '&sort=num_votes,desc&page=' + page)
            sleep(randint(5,9))
            requests+=1
            elapsed_time = time() - start_time
            print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
            clear_output(wait = True)
            
            if response.status_code != 200:
                warn('Request: {}; Status code: {}'.format(requests, response.status_code))
            
            if requests > 72:
                warn('Number of requests was greater than expected.')  
                break 
            
            page_html = BeautifulSoup(response.text, 'html.parser')
            mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')
            
            for container in mv_containers:
                if container.find('div', class_='ratings-metascore') is not None:
                    name = container.h3.a.text
                    names.append(name)
                    year = container.h3.find('span', class_='lister-item-year text-muted unbold')
                    years.append(year)
                    rating = float(container.strong.text)
                    imdb_ratings.append(rating)
                    score = container.find('span', class_='metascore')
                    score = int(score.text)
                    metascore.append(score)
                    vote = container.find('span', attrs={'name':'nv'})
                    vote = int(vote['data-value'])
                    votes.append(vote)
    
    #Store array in Panda data structure
    test_df = pd.DataFrame({'movie': names,
                            'year': years,
                            'imdb': imdb_ratings,
                            'score': metascore,
                            'vote': votes})
    #print all values in Panda
    print(test_df.info())
    print(test_df.head(10))
    """
    test_df = test_df[['movie','year','imdb','score','vote']]
    test_df.head()
    test_df['years'].unique()
    """
    
main()
#print(response.text[:500])