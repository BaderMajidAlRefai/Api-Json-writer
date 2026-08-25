from .category import Category

class Books(Category):
    def __init__(self):
        super().__init__("Books", "Open Library")
    def api(self):
        return
