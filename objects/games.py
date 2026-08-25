from .category import Category

class Games(Category):
    def __init__(self):
        super().__init__("Games", "Steam")
    def api(self):
        return
