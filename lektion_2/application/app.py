from flask import Flask
from flask import render_template

app = Flask(__name__)

calc = 1 + 2

page = f"""
<html>
    <head>
        <title>Hello from Flask</title>
    </head>

    <body>
    <h1>Hello, World!</h1>
    <p>{calc}</p>
    </body>
</html>
"""
"""
@app.route("/")
def index():
    return page"""

@app.route("/about")
def index():
    return render_template("about.html")