import base64
import requests
import json
import pandas as pd
from application import spot_info as sp
import urllib.request
import ssl


def get_token():
    """
    Skapar en token med hjälp av api-nyckalr client_id och client_secret
    Denna token är en bearer till övrig kod som Spotify behöver vid varje hämtning av API
    Hämtar detta token och gör om till string samt tilldelar till token och returnerar det
    Med hjälp av: https://www.youtube.com/watch?v=WAmEZBEeNmg (28/10-2023)
    """

    # Hämtar dessa värden från en fil spot_info.py som inte skickas till github via .gitignore
    client_id = sp.client_id
    client_secret = sp.client_secret

    # Med hjälp av client_id och client_secret kan man ta fram token som behövs i övrig kod
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = result.json()
    token = json_result["access_token"]
    return token


def search_for_artist(token, artist_name):
    """
    Då artister inte sparas i klartext behöver vi ta fram ID för den artist vi söker fram och spara ID:t
    Spotify har en search-funktion där man kan söka efter items, och vi är just nu bara intresserade av artist-id
    Arg vi hämtar är artist_name som skrivs i formulär under index.html samt token från get_token()
    https://developer.spotify.com/documentation/web-api/reference/search
    """

    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    result = requests.get(url, headers=headers, params=params)

    json_result = result.json()
    artists = json_result.get("artists")

    items = artists.get("items")

    # Returnera det första artist-ID:et som en sträng
    return items[0]['id']


def get_songs_by_artist(token, artist_id, country_code):
    """
    Här hämtar vi top 10 låtar från en artist vi söker fram
    Vi tar även med country_code som vi hämtar från en annan API då artisten kan vara olika populär i olika länder.
    https://developer.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks
    """

    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country={country_code}"
    headers = {"Authorization": f"Bearer {token}"}
    result = requests.get(url, headers=headers)
    json_result = result.json()
    return json_result


def ta_fram_top10(artist_name, country_code):
    """
    Här kombinerar vi allt och skapar en pandas-dataframe med information vi fått fram.
    """

    token = get_token()
    artist_id = search_for_artist(token, artist_name)
    json_result = get_songs_by_artist(token, artist_id, country_code)

    tracks_df = create_tracks_dataframe(json_result)

    df = pd.DataFrame(tracks_df)
    table_data = df.to_html(columns=["name", "popularity"], classes="table p-5", justify="left")

    return table_data


def create_tracks_dataframe(json_data):
    tracks = json_data.get("tracks")
    df = pd.DataFrame(tracks)
    return df


# Hämtar alla country codes då vi vill veta top10 i specifikt land
def countrycode_form():
    """
    Hämtar alla countrycodes och returnerar dessa till data_form som vi sedan loopar i index.html med Jinja2
    """
    context = ssl._create_unverified_context()
    data_form_url = "https://date.nager.at/api/v3/AvailableCountries"
    json_data = urllib.request.urlopen(data_form_url, context=context).read()
    data_form = json.loads(json_data)

    return data_form
