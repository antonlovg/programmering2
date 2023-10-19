from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import requests

app = Flask(__name__)

API_KEY = "P56lgPDrmRuinArO1ubksg==A0OfMd46O71uIjAv"

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/get_time", methods=["POST"])
def get_time():
    user_input = request.form.get("city")  # Hämta stad från formuläret
    if user_input:
        city = user_input
        api_url = f'https://api.api-ninjas.com/v1/worldtime?city={city}'
        response = requests.get(api_url, headers={'X-Api-Key': 'P56lgPDrmRuinArO1ubksg==A0OfMd46O71uIjAv'})

        return jsonify(response.json())
