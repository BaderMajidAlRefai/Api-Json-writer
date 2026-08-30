# Subipi

A small CLI tool for generating review JSON files for my personal website.
<img width="1289" height="1196" alt="subipi" src="https://github.com/user-attachments/assets/59585323-3765-49d6-9701-d3e11242a702" />

## What it does

Subipi takes media IDs, fetches metadata from various APIs, lets me optionally rate/review entries, and writes them into category JSON files.

Supported categories:
- Movies (TMDB)
- Shows (TMDB)
- Anime (AniList)
- Games (Steam)
- Books (Google Books)

## Installation

- Clone the project.
- Open the project directory in your terminal.
- Install it with:

```bash
pipx install -e .
```

## Usage and use cases
### My use case
This project was made for a very specific use case of mine.

For a website I'm currently developing, I want the site to remain static for reasons related to that project. Unless I wanted to manually write out and find every piece of metadata for each review entry, I needed some way to generate and store that data in the frontend.

I ultimately decided on storing JSON files directly in the frontend.

I initially tried requesting data from the APIs directly in the website, but that would involve maintaining several different API implementations in a language I frankly hate writing, so I made this instead. Subipi handles the requests, normalizes the results, and pumps out the JSON files for me.

### Your potential use case
I don't know how many scenarios outside of mine this is useful for, but if you want to generate your own JSON bank of reviews and ratings for several kinds of media, it may be useful.

Keep in mind that if you want to use different APIs, add or remove fields, or change the output structure, you'll need to edit the respective category/object files yourself.
