from category import Category

class Anime(Category):
    def __init__(self):
        super().__init__("Anime", "Anilist")
    def api(self):
        return