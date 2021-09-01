import requests
import json
from getcredits import get_credits
from getgenres import get_genres
from getreviews import get_reviews

response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=67a6e1aeb9867e7d066045334c59e0a9&language=en-US&page=1")

movies_fetched = response.json()

# prazna lista u koju će se spremati podatci o filmovima
movies = []

for movie_fetched in movies_fetched["results"]:
    movie = {}
    movie['moviedb_id'] = movie_fetched["id"]
    movie['original_title'] = movie_fetched["original_title"]
    movie['release_date'] = movie_fetched["release_date"]
    allcredits = get_credits(movie['moviedb_id'])
    movie['director'] = allcredits["director"]
    movie['cast'] = allcredits["cast"]
    movie['genres'] = get_genres(movie['moviedb_id'])
    movie['reviews'] = get_reviews(movie['moviedb_id'])
    movies.append(movie) 

print(movies)

with open('output.txt', 'w') as json_file:
  json.dump(movies, json_file)