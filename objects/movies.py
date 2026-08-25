import requests
import os

from dotenv import load_dotenv
from category import Category


class Movies(Category):
    def __init__(self):
        super().__init__("Screen", "TMDB")

    def api(self):
        queries = self.list
        responses = []
        for query in queries:
            response = requests.get("")
        
        return