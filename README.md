# API-CERVED TUTORIAL
Questo package ha l'intento di mostrare le varie funzionalità offerte dall'API prodotta da Cerved.
Il sito ufficiale dell'API è: **https://apps-developer.cerved.com/** di proprietà della *Cerved Group S.p.a.*.

L'intenzione del codice contenuto inquesto repository e solo quello di mostrare come implementare le chiamate all'API.

Per poter utilizzare il servizio offerto dalla *Cerved Group S.p.a.* sarà necessario effettuare la registrazione sul loro sito per ottenere le credenziali ed in particolare una **CONSUMER_KEY** che dovrete inserire nel file settings.py.

*Nota: fate attenzione a non pubblicare o diffondere erroneamente la vostra CONSUMER_KEY!*

In questo tutorial vengono implementati solo alcuni dei servizi offerti dall'API:

- **Entity Search**: permette di effettuare una ricerca libera in base al codice fiscale per le presone fisiche oppure in base alla partita iva o alla ragione sociale per le imprese. Utile per ricercare il codice **id_soggetto** che viene richiesto per le altre ricerche.
    
*Utilizzo: main.py -p entity -e 'CHIAVE DI RICERCA'*

- **Entity Profile**: permette di avere i dati relativi ad un profilo in base alla ricerca per id_soggetto.

*Utilizzo: main.py -p profile -i 'ID_SOGGETTO'*

- **Entity Contacts**: permette di avere i dati relativi ai contatti di un profilo in base alla ricerca per id_soggetto.
    main.py -p contacts -i 'ID_SOGGETTO'

- **Entity PEC**: permette di avere la PEC di un profilo in base alla ricerca per id_soggetto.
    main.py -p pec -i 'ID_SOGGETTO


