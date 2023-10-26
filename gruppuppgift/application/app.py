from flask import Flask, render_template, request
from application import func
import pandas as pd

"""
Att göra:
1. Loopa igenom package.json (språkkoder)
2. Lägga in språkkoder i dropdown tex. Svenska = sv
3. Funktioner för search och författare

.

"""

app = Flask(__name__)


# Skapar index och hämtar funktion för att hämta alla sprakkoder (ISO 639-1)
@app.route('/')
def index():
    sprakkod_data = func.sprakkod('language_code.json')
    return render_template('index.html', språkdata=sprakkod_data)


# Skickar POST till /resultat men går man dit utan post så blir det felmeddelande
@app.route('/resultat', methods=['POST'])
def visa_resultat():
    # Tilldelar det man väljer i form till valt_languages och valt_search
    valt_languages = request.form['languages']
    valt_search = request.form['search']

    # URL så som API är uppbyggd
    url = f"https://gutendex.com/books/?languages={valt_languages}&search={valt_search}"

    # Använder Pandas för att hämta datan
    df = pd.read_json(url)

    # Expandera JSON-objekt i kolumnen "results"
    df = df['results'].apply(pd.Series)

    # Välj önskade kolumner
    df = df[['title', 'authors', 'subjects', 'languages']]

    return render_template("resultat.html", df=df.to_html(), valt_languages=valt_languages, valt_search=valt_search, url=url)
