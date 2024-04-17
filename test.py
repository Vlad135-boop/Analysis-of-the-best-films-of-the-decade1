from bs4 import BeautifulSoup
import requests
from main import Movies

URL_MOVIES = 'https://www.afisha.ru/selection/75-luchshih-filmov-desyatiletiya--po-versii-zapadnyh-kinokritikov/'

response_films = requests.get(url=URL_MOVIES)


movies_soup = BeautifulSoup(response_films.text, 'html.parser')
movie = Movies(movies_soup=movies_soup)


print(movie.get_movies_list('a', "CjnHd y8A5E nbCNS yknrM"))
print(movie.get_genres_stat('div', 'S_wwn'))
print(movie.get_rating_plot('div', 'IrSqF KDBPA BNjPz k96pX'))
print(movie.get_release_years_plot('div', 'S_wwn'))