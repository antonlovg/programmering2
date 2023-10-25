from flask import Flask, render_template
import ssl
import pandas as pd
from application import func



app = Flask(__name__)


@app.route("/")
def index():
    """
    Framsida, ska via IP ta fram användarens loc och visa nya låtar via spotifys API.
    """

    def create_tracks_dataframe(json_data):
        tracks = json_data.get("tracks")
        if tracks:
            df = pd.DataFrame(tracks)
            return df
        return None

    token = func.get_token()
    artist_name = "Jimin"
    country_code = "US"
    artist_id = func.search_for_artist(token, artist_name)
    json_result = func.get_songs_by_artist(token, artist_id, country_code)

    if artist_id is not None:
        tracks_df = create_tracks_dataframe(json_result)

        if tracks_df is not None:

            df = pd.DataFrame(tracks_df)
            table_data = df.to_html(columns=["name", "popularity"], classes="table p-5", justify="left")

    return render_template('index.html', title="Home", data=table_data, artist_name=artist_name)


@app.route("/recommendations")
def rec():
    """
    Denna route hämtar rekommenderade låtar via spotifys API.
    """

    context = ssl._create_unverified_context()
    return render_template('recommendations.html', title="Recommendations")


@app.route("/new")
def new():
    """
    Denna route hämtar nya album via spotifys API.
    """

    context = ssl._create_unverified_context()

    return render_template('new.html', title="New releases")


@app.route("/api")
def api():




    return render_template('index.html', title="Home")


@app.errorhandler(404)
def page_not_found(e):
    """
    Hanterar errorkod 404
    """
    return render_template('404.html'), 404
