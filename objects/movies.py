import requests
import os

from dotenv import load_dotenv
from category import Category
from generate import generate_object

class Movies(Category):
    def __init__(self):
        super().__init__("Shows", "TMDB")

    def api(self):
        load_dotenv()
        api_key = os.getenv("TMDB_API_KEY")
        queries = self.list
        responses = []
        failed_responses = []
        for query in queries:
            response = requests.get(
                f"https://api.themoviedb.org/3/movie/{query}",
                headers = {
                    "accept" : "application/json",
                    "Authorization" : f"Bearer {api_key}"
                }
            )
            if response.ok:
                responses.append(response.json())

            else: 
                print(
                    f"Failed to fetch {query}: "
                    f"{response.status_code}"
                )
                failed_responses.append(query)

        return responses, failed_responses

    def normalize(self, responses):
        category_dict = {}

        for response in responses:
            movie_dict = generate_object(
                id = response["id"],
                title = response["original_title"],
                creator = response["production_companies"][0]["name"] if response["production_companies"] else "Unknown",
                yor = response["release_date"][:4],
                genres = [genre["name"] for genre in response["genres"]],
                img = f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
            )
            category_dict[response["id"]] = movie_dict

        return category_dict