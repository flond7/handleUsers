# AGGIUNGERE UFFICI / SIMIL UFFICI
- entrare come amministratore nel backend di django
- selezionare la categoria in cui si vuole aggiungere l'item (es: mail degli uffici)
- aggiungere l'elemento


# AGGIUNGERE UNA PAGINA PER APPLICATIVI
- creare una pagina html in api/templates (es: adweb.html)
- aggiungere la voce della pagina in api/templates/includes/sidebar.html modificando il nome del segment e href
- aggiungere l'url in api/urls.py
- aggiungere la funzione per visualizzare la pagina in api/view.py (ricordarsi sdi passare eventuali parametri nella funzione)


# CREARE GLI ACCOUNT PER L'ACCESSO
- Creare almeno un account amministratore
- Creare un gruppo (es: P.O.) a cui dare i permessi per visualizzare customUser, aggiungere e visualizzare askUser
- Creare tanti utenti quante sono le PO dell'ente e assegnarle al gruppo PO
Il gestionale è pensato perchè le PO inviino la richiesta di attivazione quando una nuova persona arriva nel loro ufficio. Possono visualizzare le pagine:
---- Chiedi utenze (create askUser)
---- Elenco utenti di tutto l'ente

# INSTALLAZIONE

## AMMINISTRATORE SMANETTONE

### Aggiungere uffici / simil uffici (si modifica il codice)
- Nei file andare in api/modelsConstants.py e individuare dove si vuole aggiungere qualcosa
- Inserire l'elemento nell'array
- Nella pagina views controllare se i nuovi uffici vanno aggiunti per essere visualizzati anche nella pagina profilo del singolo utente. 
  Nel caso, scorrere alla view profile e aggiungere i nuovi elmenti all'oggetto MY_MODEL_CONST

### Creare una nuova pagina
- In handleUsers/api/templates creare la nuova pagina nomePagina.html

### Impostare l'invio di email quando viene richiesto un nuovo utente
- In handleUsers/api/modelConstants e modificare i dati in NOTIFICATION
- in handleusers/handleusers creare un file .env all'interno del quale copiare
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=YourEmail@address
EMAIL_HOST_PASSWORD=YourAppPassword
RECIPIENT_ADDRESS=TheRecieverOfTheMails


## AMMINISTRATORE NON SMANETTONE
- interfaccia da backend




## SIGNIFICATO DELLE VOCI
# Employed (in models)
Indica se l'utente è ancora dipendente dell'ente (o legato all'ente comunque). Se ho una dipendente della Comunità montana che deve agire su aviano questa è un utente paragonabile a una dipendente fino a che deve operare sui nostri sistemi. 
E' un parametro manuale, nel senso che bisogna manualmente segnare che il dipendente è o non è ancora impiegato. Quando non lo è più compare in grigio e semitrasparente.
In caso non sia più dipendente ma certi account risultino ancora attivi (non disabilitati o non "mai assegnati") compare un warning con fantasmino (sarebbe meglio zombie però...)
# Active (in models)
Indica se l'utente ha ancora account attivi o se è completamente disabilitato. Se disabilitato non deve comparire più
