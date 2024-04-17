from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd


class Movies:
    'This class was created for data analysis'

    def __init__(self, movies_soup):
        self.movies_soup = movies_soup

    
    def get_movies_list(self, tag, class_=None) -> list:
        """
        This function will return the top most popular movies of the decade

        :param tag:
        :param class_:
        :return movie_list:
        """

        movie_list = []
        movies = list(self.movies_soup.find_all(tag, class_))
        for movie in movies:
            movie_list.append(movie.get_text())
        return movie_list

    
    def get_genres_stat(self, tag, class_=None) -> dict:
        """
        This function will return the top genres of the most popular movies

        :param tag:
        :param class_:
        :return all_genre:
        """

        genre_list = []
        genre_dict = {}
        genres = list(self.movies_soup.find_all(tag, class_))
        for genre in genres:
            if not genre.get_text()[0].isdigit():
                genre_list.append(genre.get_text())
                continue
            genre_list.append(genre.get_text()[6:])
        
        genre_set = set(genre_list)
        
        for genre in genre_set:
            genre_dict[genre] = genre_list.count(genre)
        all_genre = {k: v for k, v in sorted(genre_dict.items(), key=lambda item: item[1])}
        return all_genre


    def get_rating_plot(self, tag, class_=None) -> None: 
        """
        This function will plot the rating of the most popular movies

        :param tag:
        :param class_:
        :return None:
        """

        rating_list = []
        ratings = list(self.movies_soup.find_all(tag, class_))
        for rating in ratings:
            rating_list.append(rating.get_text())
        rating_list = sorted(map(float, rating_list))

        df = pd.DataFrame(rating_list)
        plt.plot(df)
        plt.title('Рейтинги самых популярных фильмов')
        plt.show()


    def get_release_years_plot(self, tag, class_=None) -> None:
        """
        This function will plot a bar chart in which the number of popular movies corresponds to the years of the decade
        
        :param tag:
        :param class_:
        :return None:
        """

        year_list = []
        year_dict = {}
        years = list(self.movies_soup.find_all(tag, class_))
        for year in years:
            try:
                year_list.append(int(year.get_text()[:4]))
            except ValueError:
                continue
        
        year_set = set(year_list)
        for year in year_set:
            year_dict[year] = year_list.count(year)

        plt.bar(x=year_dict.keys(), height=year_dict.values())
        plt.title('Количество лучших фильмов в каждом году десятилетия')
        plt.show()
    



        



