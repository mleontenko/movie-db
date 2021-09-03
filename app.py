import requests
import json
import psycopg2
from getcredits import get_credits
from getgenres import get_genres
from getreviews import get_reviews
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sentiment analysis
sid = SentimentIntensityAnalyzer()

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
    movie['scores'] = []
    for review in movie['reviews']:
        score = sid.polarity_scores(review)
        movie['scores'].append(score["compound"])        
    movies.append(movie) 

#print(movies)


# ispis u txt datoteku
with open('output.txt', 'w') as json_file:
  json.dump(movies, json_file)


# spremanje u bazu podataka
conn = psycopg2.connect(
        host="localhost",
        database="moviedb",
        user="root",
        password="root",
        port=5432)

dbCursor = conn.cursor()

for movie in movies:

    moviedb_id = movie["moviedb_id"]
    original_title =movie["original_title"]
    release_date = movie["release_date"]
    director = movie["director"]
    # escape za navodnik (dogodio se slucaj da redatlj ima navodnik u imenu npr. Ettore D'Alessandro)
    director = director.replace("'", "''")
    cast = movie["cast"]
    genres = movie["genres"]
    reviews = movie["reviews"]
    scores = movie["scores"]

    movieinsert = f"INSERT INTO public.movies(moviedb_id, original_title, release_date, director) VALUES ({moviedb_id}, '{original_title}', '{release_date}', '{director}') RETURNING id;"
    #print(movieinsert)
    dbCursor.execute(movieinsert)
    movies_id = dbCursor.fetchone()[0]
    for actor in cast:
        # escape za navodnik (dogodio se slucaj da glumac ima navodnik u imenu npr. Katy O'Brian)
        actor_clean = actor.replace("'", "''")
        actorinsert = f"INSERT INTO public.actors(movie_id, name) VALUES ({movies_id}, '{actor_clean}');"
        dbCursor.execute(actorinsert)
    for genre in genres:
        genreinsert = f"INSERT INTO public.genres(movie_id, name) VALUES ({movies_id}, '{genre}');"
        dbCursor.execute(genreinsert)
    #print(movies_id)
    conn.commit()

conn.close()