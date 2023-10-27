from flask import Flask, render_template, request
from application import func


app = Flask(__name__)


# Skapar index och hämtar funktion för att hämta alla sprakkoder (ISO 639-1)
@app.route('/')
def index():
    sprakkod_data = func.sprakkod('language_code.json')
    genre_data = func.genre_api()
    return render_template('index.html', språkdata=sprakkod_data, genre_data=genre_data)


# Skickar POST till /resultat men går man dit utan post så blir det felmeddelande
@app.route('/resultat', methods=['POST'])
def visa_resultat():

    # Hämtar genre ur formuläret
    valt_genre = request.form['topic']

    # Hämtar funktionen för book_api och tilldelar till df samt skickar valt_genre-variabel som arg
    df = func.book_api(valt_genre)

    return render_template("resultat.html", df=df.to_html())
