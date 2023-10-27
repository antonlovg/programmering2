# Problem som uppstod

### Första
Att få en dropdown med länder men då vår API ej var lämpat för att hämta språkkoder så behövdes nytt dict skapas.

### Andra
Att veta var post skulle skickas när man väl fick ut språkkod (samt att jag satt och hade problem med detta pga fel struktur på mina mappar då templates låg "över" application så fick aldrig render_template att fungera)

### Tredje
Att få till previous/next-knappar då POST skickar en gång och det ej går att uppdatera. Skickar jag tex:
    <a class="btn btn-primary" href="{{ url }}?languages={{ valt_languages }}&search={{ valt_search }}&page=1">Previous Page</a>
    <a class="btn btn-primary" href="{{ url }}?languages={{ valt_languages }}&search={{ valt_search }}&page=2">Next Page</a>
Så länkar url direkt till hemsidan för api och det blir helt fel.

### Fjärde
Att kombinera två APIer när de postar olika värden, men löste det genom att kolla i POST i firefox för att se hur de postades samt ändrade namn på den nya APIn (film-genres) för att posta den som subject istället då books hanterar det så. 

