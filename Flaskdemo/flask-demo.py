from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# ----------------
# HTML Escaping
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#html-escaping

# @app.route("/name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# ---------------
# Routing
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing

# Sätter index page
# @app.route("/")
# def index():
#     return "Index page"

# Sätter sub-path, tex url.com/hello/everyone
# @app.route("/hello/everyone")
# def hello():
#     return "Hello, my World"

# ----------------
# Variable Rules
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#variable-rules

# Ersätter tex <username> med namnet i url, <int:post_id> med nmmer och <path:subpath> med subpath efter /path/

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'


# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# -----------------
# Unique URLs / Redirection Behavior
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#unique-urls-redirection-behavior

# Lägger man till / i slutet kan man nå även om man skriver /projects.
# Lägger man inte till / i slutet kan man inte nå /about/
# Har med indexing i search engines att göra

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# ----------------
# URL Building
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#url-building

# Hjälper till att strukturera , underhållsbar och säker

# @app.route('/')
# def index():
#     return 'index'


# @app.route('/login')
# def login():
#     return 'login'


# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'


# with app.test_request_context():
#     print(url_for('index'))  # Genererar URL:en för funktionen 'index'
#     print(url_for('login'))  # Genererar URL:en för funktionen 'login'
#     print(url_for('login', next='/'))  # Genererar URL:en för funktionen 'login' med en query-parameter 'next'
#     print(
#         url_for('profile', username='John Doe'))  # Genererar URL:en för funktionen 'profile' med en parameter 'username

# ------------------
# HTTP Methods
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#http-methods

# När någon försöker komma åt '/login', kontrolleras det om det är en GET- eller POST-förfrågan. Om det är en
# POST-förfrågan, hanteras inloggningen, och om det är en GET-förfrågan, visas inloggningsformuläret. Detta är en
# vanlig struktur för hantering av inloggningssidan i webapplikationer där användare kan logga in med sina uppgifter.

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# Kan även skrivas som följande:

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

# ----------------
# Static Files
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#static-files

# Kräver att man sparar filen på static/style.css
# url_for('static', filename='style.css')

# ---------------
# Rendering Templates
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


