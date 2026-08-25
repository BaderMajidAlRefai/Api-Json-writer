from objects.category import Movies, Shows, Anime, Games, Books

movies, shows, anime, games, books = Movies(), Shows(), Anime(), Games(), Books()

categories = [movies, shows, anime, games, books]

while True:
    for category in categories:
        category.toggle_prompt()

    selected = [category for category in categories if category.toggle]

    selected_text = "\nSELECTED CATAGORIES:\n"
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
for category in selected:
    response = category.api()
