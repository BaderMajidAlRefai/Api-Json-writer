import requests
from category import Category

class Movies(Category):
    def __init__(self):
        super().__init__("Shows", "TMDB")

    def api(self):
        queries = self.list
        responses = []
        for query in queries:
            response = requests.get(
                f"https://api.themoviedb.org/3/movie/{query}"
            ), headers = {
                "accept" : "application/json",
                "Authorization" : "Bearer TOKEN"
            }
        
        return