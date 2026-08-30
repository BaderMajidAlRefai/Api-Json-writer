class Normalized():
    def __init__(self, id, category, title, creator, yor, genres, img):
        self.id = id
        self.category = category
        self.title = title
        self.creator = creator
        self.yor = yor
        self.genres = genres
        self.img = img
        self.rating = 0
        self.review = ""

    def __str__(self):
         return f"""
                {self.title}, {self.creator}, {self.yor}
                {self.genres}
                Rating: {self.rating}
                Review: {self.review}
                """

    def turn_to_object(self):
        return {
            "id" : self.id,
            "category" : self.category,
            "title" : self.title,
            "creator" : self.creator,
            "yor" : self.yor,
            "genres" : self.genres,
            "img" : self.img,
            "rating" : self.rating,
            "review" : self.review,
        }

    def rate(self):
        while True:
            try:
                response = int(input(f"\nRate {self.title} from 0 to 5:\n> "))
            except ValueError:
                 print("Please only insert numbers")
                 continue
            if response < 0 or response > 5:
                 print("Please insert a valid rating.")
            else:
                 self.rating = response
                 break

    def write_review(self):
            self.review = input(f"\nWrite your review for {self.title}:\n> ")
