import requests

from .category import Category

class Books(Category):
    def __init__(self):
        super().__init__("Books", "Open Library")
        
    def api(self):
        responses = []
        failed_responses = []

        for query in self.list:
            response = requests.get(
                f"https://openlibrary.org/works/{query}.json",
            )

            if response.ok:
                response = response.json()

            else:
                print(
                    f"Failed to fetch {query}: "
                    f"{response.status_code}"
                    )
                failed_responses.append(query)
                continue

            if response.get("authors"):
                author_key = response["authors"][0]["author"]["key"]
            else:
                response["author_name"] = "unknown"
                responses.append(response)
                continue

            author_response = requests.get(
                f"https://openlibrary.org{author_key}.json"
            )
        

            if author_response.ok:
                response["author_name"] = author_response.json()["name"]
                responses.append(response)

            else: 
                print(
                    f"Failed to fetch {query}: "
                    f"{author_response.status_code}"
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
