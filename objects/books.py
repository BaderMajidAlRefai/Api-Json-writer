import requests, os

from dotenv import load_dotenv

from .category import Category
from .normalized import Normalized

class Books(Category):
    def __init__(self):
        super().__init__("books", "Google Books")
        
    def api(self):
        responses = []
        failed_responses = []

        load_dotenv()
        api_key = os.getenv("GOOGLE_BOOKS_API_KEY")
        for query in self.list:
            response = requests.get(
                f"https://www.googleapis.com/books/v1/volumes/{query}",
                params={
                    "key" : api_key
                }
            )

            if response.ok:
                responses.append(response.json())

            else: 
                print(
                    f"\nFailed to fetch {query}: "
                    f"{response.status_code}\n"
                    f"{response.text}\n"
                )
                failed_responses.append(query)

        return responses, failed_responses

    def normalize(self, responses):
        normalized_objects = []
        for response in responses:
            response["volumeInfo"]["imageLinks"]["thumbnail"] = response["volumeInfo"]["imageLinks"]["thumbnail"].replace(
                "http://",
                "https://"
            )
            book_object = Normalized(
                id = response["id"],
                category = self.name,
                title = response["volumeInfo"]["title"],
                creator = response["volumeInfo"]["authors"][0],
                yor = response["volumeInfo"]["publishedDate"][:4],
                genres = response["volumeInfo"]["categories"],
                img = response["volumeInfo"]["imageLinks"]["thumbnail"]
            )
            normalized_objects.append(book_object)

        return normalized_objects
