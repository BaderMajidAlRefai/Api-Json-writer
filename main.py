from objects.movies import Movies
from objects.anime import Anime
from objects.books import Books
from objects.games import Games
from objects.shows import Shows

movies, shows, anime, games, books = Movies(), Shows(), Anime(), Games(), Books()

categories = [movies, shows, anime, games, books]

while True:
    for category in categories:
        category.toggle_prompt()

    selected = [category for category in categories if category.toggle]

    selected_text = "\nSELECTED CATEGORIES:\n"
    for category in selected:
        selected_text += f"-{category.name} \n"
    print(selected_text)

    response = input("\nWould you like to proceed? Yes: any No: n ") != "n"
    if response:
        break

while True:
    for category in selected:
        category.shopping_list()

    response = input("Would you like to review your options? Yes: y No: any ") == "y"

    if response:
        for category in selected:
            category.print_shopping_list()

        response = input("Would you like to proceed? Yes: any No: n") != "n"
        if response:
            break          
    else:
        break

print("PROCESSING")

failures = []
normalized = {}

for category in selected:
    successful, failed = category.api()
    failures.extend(failed)

    normalized[category.name] = category.normalize(successful)

print("DONE")

if failures:
    failed_text = ""

    for failure in failures:
        failed_text += f"\n- {failure}"

    response = input(
    f"""There were the following failed responses:
    {failed_text}
    Would you like to continue? Yes: y No: any
    """) == "y"
    if not response:
        print("Thank you, check the logs for error codes.")
        raise SystemExit()


print("Here are the following generated files")

for category, items in normalized.items():
    print(f"{category} results")

    for item in items:
        print(f"-{item.id}: Title: {item.title}, Creator: {item.creator}, Year of Release: {item.yor}, Genres: {item.genres}, Image: {item.img}")