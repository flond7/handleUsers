# AGGIUNGERE UFFICI / SIMIL UFFICI
- entrare come amministratore nel backend di django
- selezionare la categoria in cui si vuole aggiungere l'item (es: mail degli uffici)
- aggiungere l'elemento



# INSTALLAZIONE

## AMMINISTRATORE SMANETTONE

### Aggiungere uffici / simil uffici (si modifica il codice)
- Nei file andare in api/modelsConstants.py e individuare dove si vuole aggiungere qualcosa
- Inserire l'elemento nell'array
- Nella pagina views controllare se i nuovi uffici vanno aggiunti per essere visualizzati anche nella pagina profilo del singolo utente. 
  Nel caso, scorrere alla view profile e aggiungere i nuovi elmenti all'oggetto MY_MODEL_CONST

### Creare una nuova pagina
- In handleUsers/api/templates creare la nuova pagina nomePagina.html

## AMMINISTRATORE NON SMANETTONE
- interfaccia da backend