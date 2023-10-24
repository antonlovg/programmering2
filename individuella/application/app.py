from flask import Flask, render_template
import ssl
import anton

app = Flask(__name__)

CLIENT_ID = f"{anton.client_id}"
CLIENT_SECRET = f"{anton.client_secret}"


@app.route("/")
def index():
    """
    Framsida, ska via IP ta fram användarens loc och visa nya låtar via spotifys API.
    """

    return render_template('index.html', title="Home")


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



    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    """
    Hanterar errorkod 404
    """
    return render_template('404.html'), 404
