import requests
import json

def get_movie(search,s_type='movie'):
    
    #takes search keyword and type of search you want to perform as s_type = 'movie','series','episode'

    base_url_text = 'http://www.omdbapi.com/'
    PARAMS={'t':search,'apikey':'15e8a773','type':s_type,'plot':'full'}
    r = requests.get(url=base_url_text,params=PARAMS)
    data = r.json()
    return data

#print(data['Title'],data['Rated'],data['Released'],data['Genre'],data['Director'],data['Actors'],data['imdbRating'],data['Plot'])
def get_poster(url):
    
    # takes url of image and returns response of object of that image
    r = requests.get(url)
    return r

