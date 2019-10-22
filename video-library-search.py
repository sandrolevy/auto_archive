import os
import re
import msvcrt
import imdb
from similarity.damerau import Damerau


folder = r'D:\Users\Levy\Downloads\Movies'
ia = imdb.IMDb()
damerau = Damerau()
movie_list = [
    files for files in os.listdir(folder)
]
deg = []
for movie in movie_list:
    try:
        search_movie = ia.search_movie(movie[0:15])
        deg.append(damerau.distance(movie[0:15], search_movie))
        print(deg)
        indd = int(deg.index(min(deg)))
        print(indd)
        mostapt = search_movie[indd]
        print(mostapt)
    except IndexError:
        pass

# Need remove spaces and special symbols, besides that  find a better way to search with more precision.

ia = imdb.IMDb()
movies = ia.search_movie('matrix')
print(movies)