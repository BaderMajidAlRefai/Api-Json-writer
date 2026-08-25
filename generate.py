def generate_json(id, title, creator, yor, genres, rating, review):
    return {
        "id" : id,
        "title" : title,
        "creator" : creator,
        "yor" : yor,
        "genres" : genres,
        "rating" : rating,
        "review" : review,
    }