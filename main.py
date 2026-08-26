#!/usr/bin/env python3
import pathlib

from helper_functions import (
    collect_category_items,
    confirm_failed_responses,
    display_results,
    fetch_and_normalize_categories,
    rate_entries,
    review_entries,
    select_categories,
    write_json
)

from objects.movies import Movies
from objects.anime import Anime
from objects.books import Books
from objects.games import Games
from objects.shows import Shows

movies, shows, anime, games, books = Movies(), Shows(), Anime(), Games(), Books()

categories = [movies, shows, anime, games, books]

selected = select_categories(categories)

collect_category_items(selected)

failures, normalized = fetch_and_normalize_categories(selected)

confirm_failed_responses(failures)

display_results(normalized)

rate_entries(normalized)

review_entries(normalized)

write_json(normalized)