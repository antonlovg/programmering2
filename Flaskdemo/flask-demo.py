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

# HÄmtar från templates/hello.html

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

# ----------------
# Accessing Request Data
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#accessing-request-data
# ----------------
# Context Locals
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#context-locals

# with app.test_request_context('/hello', method='POST'):
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello'
#     assert request.method == 'POST'

# -----------------
# The Request Object
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#the-request-object

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
# the code below is executed if the request method
# was GET or the credentials were invalid
#     return render_template('login.html', error=error)

# searchword = request.args.get('key', '')

# -----------------
# File Uploads
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#file-uploads
# Finns mer här: https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')

# Använda filename från användaren:

# from werkzeug.utils import secure_filename
#
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['the_file']
#         file.save(f"/var/www/uploads/{secure_filename(file.filename)}")

# ----------------
# Cookies
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#cookies

# Läsa cookies
# @app.route('/')
# def index():
#    username = request.cookies.get('username')
     # use cookies.get(key) instead of cookies[key] to not get a
     # KeyError if the cookie is missing.

# Lagra cookies
# from flask import make_response

# @app.route('/')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp

# ----------------
# Redirects and Errors
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#redirects-and-errors

# To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function:
# from flask import abort, redirect, url_for
#
# @app.route('/')
# def index():
#     return redirect(url_for('login'))
#
# @app.route('/login')
# def login():
#     abort(401)
#     this_is_never_executed()

# Error page (standard är svart och vit error page för varje error code men om man vill ha en customized:
# from flask import render_template
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

# --------------------
# About Responses
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#about-responses

# from flask import render_template
#
# Från:
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('error.html'), 404

# Till:
# from flask import make_response
#
# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp

# --------------------
# APIs with JSON
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#apis-with-json

# @app.route("/me")
# def me_api():
#     user = get_current_user()
#     return {
#         "username": user.username,
#         "theme": user.theme,
#         "image": url_for("user_image", filename=user.image),
#     }
#
# @app.route("/users")
# def users_api():
#     users = get_all_users()
#     return [user.to_json() for user in users]

# ------------------
# Sessions
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#sessions

# Användare kan kolla på inneållet av en cookie men inte ändra ( om man inte vet secret key)
# from flask import session
#
# # Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
#
# @app.route('/')
# def index():
#     if 'username' in session:
#         return f'Logged in as {session["username"]}'
#     return 'You are not logged in'
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('index'))
#     return '''
#         <form method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''
#
# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))

# ------------------- Message Flashing (User feedback for user friendly ui)
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#message-flashing
# To flash a message use the flash() method,
# to get hold of the messages you can use get_flashed_messages() which is also available in the templates. See
# Message Flashing for a full example.

# -------------------
# Logging
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#logging

# app.logger.debug('A value for debugging')
# app.logger.warning('A warning occurred (%d apples)', 42)
# app.logger.error('An error occurred')

# ------------------
# Hooking in WSGI Middleware
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#hooking-in-wsgi-middleware

# from werkzeug.middleware.proxy_fix import ProxyFix
# app.wsgi_app = ProxyFix(app.wsgi_app)

# -------------------
#
