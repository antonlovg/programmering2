import base64
import requests
import json
import pandas as pd
from application import spot_info as sp

client_id = sp.client_id
client_secret = sp.client_secret


def get_token():
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
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    result = requests.get(url, headers=headers, params=params)

    if result.status_code == 200:
        json_result = result.json()
        artists = json_result.get("artists")

        if artists is not None:
            items = artists.get("items")

            if items is not None and len(items) > 0:
                # Returnera det första artist-ID:et som en sträng
                return items[0]['id']

    return None  # Returnera None om det inte finns några resultat eller om det uppstod ett fel


def get_songs_by_artist(token, artist_id, country_code):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country={country_code}"
    headers = {"Authorization": f"Bearer {token}"}
    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        json_result = result.json()
        return json_result
    else:
        print("Fel vid hämtning av låtar. Statuskod:", result.status_code)
        return None


# Skapa en Pandas DataFrame för att lagra låtdata
def create_tracks_dataframe(json_data):
    tracks = json_data.get("tracks")
    if tracks:
        df = pd.DataFrame(tracks)
        return df
    return None
