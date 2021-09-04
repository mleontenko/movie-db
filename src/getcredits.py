import requests

def get_credits(movie_id):
    credits_response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=67a6e1aeb9867e7d066045334c59e0a9&language=en-US")
    credits_fetched = credits_response.json()

    # dictionary koji će se vratiti kao response
    allcredits = {}

    # prazna lista u koju će se spremati popis glumaca
    cast = []
    for actor in credits_fetched["cast"]:
        cast.append(actor["name"])
    allcredits["cast"] = cast
    
    # dohvat redatelja
    director = ""
    for member in credits_fetched["crew"]:        
        if member["job"] == "Director":
            director = member["name"]
    allcredits["director"] = director

    return allcredits