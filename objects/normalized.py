class Normalized():
    def __init__(self, id, title, creator, yor, genres, img):
        self.id = id
        self.title = title
        self.creator = creator
        self.yor = yor
        self.genres = genres
        self.img = img
        self.rating = 0
        self.review = ""

    def turn_to_object(self):
        return {
            "category" : self.category,
            "id" : self.id,
            "title" : self.title,
            "creator" : self.creator,
            "yor" : self.yor,
            "genres" : self.genres,
            "img" : self.img,
            "rating" : self.rating,
            "review" : self.review,
        }