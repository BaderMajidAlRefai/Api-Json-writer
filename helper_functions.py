import json, os, subprocess
from pathlib import Path

def clear_terminal():
    subprocess.run(
                ["cls" if os.name == "nt" else "clear"],
                shell=os.name == "nt"
            )
    
def expanded_list(normalized):
    print("\nHere are the following generated files:\n")

    for category, items in normalized.items():
        print(f"{category.upper()} RESULTS:")

        for item in items:
            print(
                f"- {item.id}\n"
                f"  Title: {item.title}\n"
                f"  Creator: {item.creator}\n"
                f"  Year of Release: {item.yor}\n"
                f"  Genres: {item.genres}\n"
                f"  Image: {item.img}\n"
            )

def short_list(normalized):
    print("\nHere are the following generated files:\n")
    for category, items in normalized.items():
        print(f"{category.upper()} RESULTS:")

        for item in items:
            print(f"- {item.id}: {item.title}")
        print()

def select_item(normalized, purpose):
    clear_terminal()
    numbered_items = []
    for category, items in normalized.items():
        print(f"\n{category.upper()}:")

        for item in items:
            numbered_items.append(item)
            print(f"{len(numbered_items)}: {item.title}")

    while True:
        try:
            choice = int(input(f"\nWhat item would you like to {purpose}? "))
        except ValueError:
            print("Please only insert numbers")
            continue

        if choice < 1 or choice > len(numbered_items):
            print("\nInvalid entry. Please select a number from the list.")

        else:
            return numbered_items[choice - 1]


def select_categories(categories):
    while True:
        clear_terminal()
        selected_categories = [category for category in categories if category.selected]
        unselected_categories = [category for category in categories if not category.selected]
        indexes = unselected_categories + selected_categories

        print("\n--- Available Categories ---")
        for category in unselected_categories:
            index = indexes.index(category)
            print(f"  [ {index + 1} ] {category.name}")

        print("\n--- Selected Categories ---")
        for category in selected_categories:
            index = indexes.index(category)
            print(f"  [ {index + 1} ] {category.name}  ✓")

        response = input("\nWhat categories would you like to select? or enter 'DONE' if completed \n")

        if response == "DONE":
            if selected_categories:
                return selected_categories
            else:
                print("Please select a category")
                continue

        try:   
            response = int(response)
            indexes[response - 1].toggle()
        except ValueError, IndexError:
            print("Please enter a valid number.")
            continue


def collect_category_items(selected):
    while True:
        for category in selected:
            clear_terminal()
            category.shopping_list()

        response = input("\nWould you like to review your options?\nYes: y | No: any\n> ") == "y"

        if response:
            for category in selected:
                category.print_shopping_list()

            response = input("\nWould you like to proceed?\nYes: any | No: n\n> ") != "n"
            if response:
                break
        else:
            break


def fetch_and_normalize_categories(selected):
    print("\nPROCESSING...\n")

    failures = []
    normalized = {}

    for category in selected:
        successful, failed = category.api()
        failures.extend(failed)

        normalized[category.name] = category.normalize(successful)

    print("DONE\n")

    return failures, normalized


def confirm_failed_responses(failures):
    if failures:
        failed_text = ""

        for failure in failures:
            failed_text += f"\n- {failure}"

        response = input(
            f"There were the following failed responses:\n"
            f"{failed_text}\n\n"
            "Would you like to continue?\n"
            "Yes: y | No: any\n> "
        ) == "y"
        if not response:
            print("\nThank you. Check the logs for error codes.\n")
            raise SystemExit()


def display_results(normalized):
    response = input(
        "Would you like to view the results?\n"
        "[1] Expanded | [2] Short | [Any] Do not view\n> "
    )
    if response == "1":
        expanded_list(normalized)
    elif response == "2":
        short_list(normalized)


def rate_entries(normalized):
    response = input("\nWould you like to rate any entries?\nYes: y | No: any\n> ").lower() == "y"
    if response:
        while True:
            selected_object = select_item(normalized, "rate")
            selected_object.rate()
            response = input("\nAre you finished rating entries?\nYes: y | No: any\n> ").lower() == "y"
            if response:
                break


def review_entries(normalized):
    response = input("\nWould you like to review any entries?\nYes: y | No: any\n> ").lower() == "y"
    if response:
        while True:
            selected_object = select_item(normalized, "review")
            selected_object.write_review()
            response = input("\nAre you finished reviewing entries? This is the final step before execution\nYes: y | No: any\n> ").lower() == "y"
            if response:
                break

def write_json(normalized):
    working_directory = Path.cwd()
    for category, items in normalized.items():
        filename = f"{category.lower()}.json"
        path = working_directory / filename

        if path.exists():
            with path.open("r") as file:
                existing = json.load(file)

        else:
            existing = []

        new_items = [item.turn_to_object() for item in items]

        existing.extend(new_items)

        with path.open("w") as file:
            json.dump(existing, file, indent=4)

    print("Files Successfully Completed")
