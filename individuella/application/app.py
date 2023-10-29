from flask import Flask, render_template, request
from application import func

app = Flask(__name__)


@app.route("/")
def index():
    """
    Framsida, ska också via IP ta fram användarens loc och visa nya låtar via spotifys API.
    """

    # Hämtar funktionen från func och skickar det vidare till index.html för att skapa en dropdown med flera länder
    data_form = func.countrycode_form()

    return render_template('index.html', title="Home", data_form=data_form)


@app.route("/top10", methods=['POST'])
def top10():
    """
    Listar en artists top10 låtar just nu
    """
    artist_name = request.form["formArtist"]
    country_code = request.form["countrycode"]
    artist_data = func.ta_fram_top10(artist_name, country_code)

    return render_template('top10.html', data=artist_data, title="Top 10", artist_name=artist_name)


@app.route("/recommendations")
def rec():
    """
    Denna route hämtar rekommenderade låtar via spotifys API.
    """

    return render_template('recommendations.html', title="Recommendations")


@app.route("/new")
def new():
    """
    Denna route hämtar nya album via spotifys API.
    """

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
