import requests
import os

from dotenv import load_dotenv
from .category import Category
from .normalized import Normalized

class Shows(Category):
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
                f"https://api.themoviedb.org/3/tv/{query}",
                headers = {
                    "accept" : "application/json",
                    "Authorization" : f"Bearer {api_key}"
                }
            )
            if response.ok:
                responses.append(response.json())

            else: 
                print(
                    f"\nFailed to fetch {query}: "
                    f"{response.status_code}\n"
                )
                failed_responses.append(query)

        return responses, failed_responses

    def normalize(self, responses):
        normalized_objects = []

        for response in responses:
            show_object = Normalized(
                id = response["id"],
                title = response["name"],
                creator = response["production_companies"][0]["name"] if response["production_companies"] else "Unknown",
                yor = response["first_air_date"][:4],
                genres = [genre["name"] for genre in response["genres"]],
                img = f"https://image.tmdb.org/t/p/w500{response['poster_path']}"
            )
            normalized_objects.append(show_object)

        return normalized_objects
