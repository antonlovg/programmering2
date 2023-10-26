# Den här filen innehåller saker som har med Flask-servern att göra, det vill säga endpoints, routing, HTTP-metoder etc.
# Flask innehåller all funktionalitet för att skapa en server och hantera trafik till och från den servern, men inte funktionalitet
# för att skicka requests till andra servrar. Till detta använder vi i func.py istället urllib vilket är ett av pythons standardbibliotek.
import ssl
# Termer: Bibliotek, standardbilbliotek, ramverk och moduler refererar ofta till samma sak, dvs. förbyggd kod som du kan importera.
# Ett standardbibliotek är ett som levereras som en del av Pyhton, och de är ofta 'native python' el. med andra ord skrivna helt i python
# Andra bibliotek kan vara skrivna med en annan miljö i bakgrunden, t.ex med C. Dessa bibliotek kan vara plattformsberoende (win, linux, mac osv)
# medan bibliotek i native python är platformsoberoende och kan användas överallt där bythonkod kan köras. 

import urllib.request
import json
from markupsafe import escape
from application import func
from flask import Flask
from quart import Quart, make_response, render_template, request

# Skapa ett Flask server-objekt. Det är denna som ni sedan startar med 'flask run' från terminalen.
app = Quart(__name__)


@app.route("/")
async def index():
    '''Denna funktion körs när man går till servern utan endpoint. 
       På en statisk webbsida skulle detta t.ex motsvara filen index.html'''

    context = ssl._create_unverified_context()
    ip_loc = "https://1.1.1.1/cdn-cgi/trace"
    json_data = urllib.request.urlopen(ip_loc, context=context).read()

    response = await make_response(await render_template('index.html'))
    response.set_cookie("name", "value")

    # Hämta index.html och uppdatera den med hjälp av Jinja, skicka den sedan till klienten (browsern)
    return response


@app.route("/form")
async def form():
    '''Denna funktion körs när man går till servern med  endpoint '/form'. 
       På en statisk webbsida skulle detta t.ex kunna motsvara filen mappen /form med filen index.htm'''

    context = ssl._create_unverified_context()
    data_form_url = "https://date.nager.at/api/v3/AvailableCountries"
    json_data = urllib.request.urlopen(data_form_url, context=context).read()
    data_form = json.loads(json_data)

    response = await make_response(await render_template('form.html', data_form=data_form))
    response.set_cookie("name", "value")

    return response


@app.route("/hello")
async def hello():
    response = await make_response(await render_template('hello.html'))
    response.set_cookie("name", "value")
    return response


@app.route("/api", methods=["POST"])
async def api_post():
    '''Denna funktion körs när man går till servern med  endpoint '/api'. 
       Den tar endast emot trafik med HTTP method post.
       Försöker man med en annan metod, t.ex get, så körs den alltså inte.'''

    ##### Under lektion_4 skapade vi kod här för att göra göra om json från ett externt API, till en HTML-tabell med Pandas #####
    ##### Här har anropet till API:et samt omvandlingen flyttats ut till en egen funktion i filen func.py                   #####

    # Flask-kod sparar vi i app.py. Objectet request från flask innehåller den HTTP request som i det här fallet skickades till /api 
    # Läs innehållet från request som motsvarar <input> med name= 'year' samt 'countrycode' i HTML-formuläret <form> (form.html)
    year = request.form["year"]
    country_code = request.form["countrycode"]

    # Skapa URL för det API vi skall använda, med en formaterad sträng och injecera variablerna year, samt country_code
    data_url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"

    # Använd nu den kod vi brutit ut och lagt till i func.py för att utföra arbetet
    data = func.json_url_to_html_table(data_url)

    response = await make_response(await render_template('index.html', data=data))
    response.set_cookie("name", "value")

    # Skicka tillbaka resultatet till browsern med Jinja, dvs uppdatera mallen index.html med innehållet i variabeln data
    return response


@app.route("/api/xml")
async def xml():
    '''Denna funktion körs när man går till servern med  endpoint '/api/xml'. 
       Den tar endast emot trafik med alla HTTP methods.
       Den gör samma sak som funktionen ovan (api_post()) men med XML istället för JSON.'''

    # I det här exemplet har vi inga argument att lägga in i API:ets URL, så vi använder en vanlig sträng.
    # XPath är ett sätt att navigera i XML. Raden nedan väljer ut alla taggar med namn <item>
    data_url = "https://polisen.se/aktuellt/rss/stockholms-lan/handelser-rss---stockholms-lan/"
    data = func.xml_url_to_html_table(data_url, xpath="//item")

    response = await make_response(await render_template('index.html', data=data))
    response.set_cookie("name", "value")

    # Skicka tillbaka resultatet till browsern med Jinja, dvs uppdatera mallen index.html med innehållet i variabeln data
    return response
