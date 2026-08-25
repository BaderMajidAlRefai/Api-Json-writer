import requests

from .category import Category
from .normalized import Normalized

class Games(Category):
    def __init__(self):
        super().__init__("Games", "Steam")

    def api(self):
        responses = []
        failed_responses = []

        for query in self.list:
            response = requests.get(
                "https://store.steampowered.com/api/appdetails",
                params={
                    "appids" : query
                }
            )

            if response.ok:
                result = response.json()[str(query)]
                if result["success"]:
                    responses.append(result["data"])

                else: 
                    print(
                        f"Failed to fetch {query}: "
                        f"{response.status_code}"
                    )
                    failed_responses.append(query)
            else:
                print(
                        f"Failed to fetch {query}: "
                        f"{response.status_code}"
                    )
                failed_responses.append(query)

        return responses, failed_responses

    def normalize(self, responses):
        normalized_objects = []

        for response in responses:
            game_object = Normalized(
                id = response["steam_appid"],
                title = response["name"],
                creator = response["developers"][0],
                yor = response["release_date"]["date"],
                genres = [genre["description"] for genre in response["genres"]],
                img = response["header_image"]
            )
            normalized_objects.append(game_object)

        return normalized_objects
