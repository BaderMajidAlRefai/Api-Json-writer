import requests

from .category import Category
from .normalized import Normalized

class Anime(Category):
    def __init__(self):
        super().__init__("Anime", "Anilist")

    def api(self):
        responses = []
        failed_responses = []

        query = """
        query ($id: Int) {
        Media(id: $id, type: ANIME) {
                id

                title {
                    english
                    romaji
                }

                studios(isMain: true) {
                    nodes {
                        name
                    }
                }

                startDate {
                    year
                }

                genres

                coverImage {
                    large
                }
            }
        }
        """

        for anime_id in self.list:
            response = requests.post(
                "https://graphql.anilist.co",
                json={
                    "query" : query,
                    "variables" : {"id" : int(anime_id)}
                }
            )
            if response.ok:
                    responses.append(response.json()["data"]["Media"])

            else:
                print(
                    f"Failed to fetch {anime_id}:"
                    f"{response.status_code}")
                
                failed_responses.append(anime_id)

        return responses, failed_responses

    def normalize(self, responses):
        normalized_objects = []

        for response in responses:
            anime_object = Normalized(
                id = response["id"],
                title = response["title"]["english"] or response["title"]["romaji"],
                creator = response["studios"]["nodes"][0]["name"] if response["studios"]["nodes"] else "Unknown",
                yor = response["startDate"]["year"],
                genres = response["genres"],
                img = response["coverImage"]["large"]
            )
            normalized_objects.append(anime_object)

        return normalized_objects
