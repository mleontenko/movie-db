import requests

def get_genres(movie_id):
    genres_response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=67a6e1aeb9867e7d066045334c59e0a9&language=en-US")
    genres_fetched = genres_response.json()

    # dictionary koji će se vratiti kao response
    genres = []

    for genre in genres_fetched["genres"]:
        genres.append(genre["name"])

    return genres
    