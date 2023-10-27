import json
import requests
from flask import request
import pandas as pd
from application import api_key


# Läser arg (i vårat fall language_code.json) så som vi lärt oss i programmering 1
def sprakkod(filnamn):
    try:
        with open(filnamn, 'r') as fil:
            data_dictionary = json.load(fil)
        return data_dictionary

    # Returnerar tom lista ifall filnamnet saknas
    except FileNotFoundError:
        return {}


def genre_api():
    """
    Hämtar genres från filmer från https://api.themoviedb.org/3/genre/movie/list?language=en
    """

    # API
    url_genre_movie = f"https://api.themoviedb.org/3/genre/movie/list?language=en"

    # API-token
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + api_key.movie()
    }

    # Hämtar resultat
    response = requests.get(url_genre_movie, headers=headers)
    # Returnerar dictionary (json)
    return response.json()


def book_api(valt_genre):
    """
    Hämtar API-information från https://gutendex.com/books/? och skriver ut Title, Authors, Subjects samt Languages
    """
    # Tilldelar det man väljer i form till valt_languages och valt_search
    valt_languages = request.form['languages']
    valt_search = request.form['search']

    # URL så som API är uppbyggd (valt_genre hämtas från en dropdown från annan API, hämtar med arg)
    url_books = f"https://gutendex.com/books/?languages={valt_languages}&search={valt_search}&topic={valt_genre}"

    # Använder Pandas för att hämta datan
    df = pd.read_json(url_books)
    df = df['results'].apply(pd.Series)

    # Eftersom jag bara vill ha viss information ur JSON så hämtar jag detta
    df = df[['title', 'authors', 'subjects', 'languages']]

    # Omvandla listor till strängar för att göra det mer läsbart
    # https://stackoverflow.com/questions/45306988/column-of-lists-convert-list-to-string-as-a-new-column
    # svaret som funka: https://stackoverflow.com/a/60416031
    df['authors'] = df['authors'].apply(lambda authors: ', '.join([author['name'] for author in authors]))
    df['subjects'] = df['subjects'].apply(lambda subjects: ', '.join(subjects))
    df['languages'] = df['languages'].apply(lambda languages: ', '.join(languages))

    return df
