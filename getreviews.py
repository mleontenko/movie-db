import requests

def get_reviews(movie_id):
    reviews_response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key=67a6e1aeb9867e7d066045334c59e0a9&language=en-US&page=1")
    reviews_fetched = reviews_response.json()

    # dictionary koji će se vratiti kao response
    reviews = []

    for review in reviews_fetched["results"]:
        reviews.append(review["content"])

    return reviews
    