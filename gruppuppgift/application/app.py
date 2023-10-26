from flask import Flask, render_template

"""
Att göra:
1. Loopa igenom package.json (språkkoder)
2. Lägga in språkkoder i dropdown tex. Svenska = sv
3. Funktioner för search och författare

.

"""

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
