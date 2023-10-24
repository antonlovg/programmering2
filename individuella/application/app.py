from flask import Flask, render_template
import ssl

app = Flask(__name__)


@app.route("/")
def index():
    """
    Framsida, ska via IP ta fram användarens loc och visa nya låtar via spotifys API.
    """

    return render_template('index.html')


@app.route("/recommendations")
def rec():
    """
    Denna route hämtar rekommenderade låtar via spotifys API.
    """

    context = ssl._create_unverified_context()
    return render_template('recommendations.html')


@app.route("/new")
def new():
    """
    Denna route hämtar nya album via spotifys API.
    """

    context = ssl._create_unverified_context()

    return render_template('new.html')

@app.route("/api")
def api():
