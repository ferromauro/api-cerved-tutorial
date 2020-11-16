import requests
import json
import argparse
from pprint import pprint
from settings import CONSUMER_KEY, PRODUCTS


class Api_Cerved():
    def __init__(self):
        pass

    def query(self, url, search_term):
        """Viene impostato l'header con la API Key ed effettua la query in base all'url passato come parametro. Vengono restituiti i dati."""
        headers = { 'accept':'application/json',
                    'apikey': CONSUMER_KEY 
                  }
        try :
            query_url = 'https://api.cerved.com/cervedApi'+url+search_term
            r = requests.get(query_url, headers=headers)
            if r.status_code == 200:
                return r.json()
            else:
                print('La richiesta non è andata a buon fine: risposta del server codice: ' + str(r.status_code))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    """API-CERVED-TUTORIAL"""
    api = Api_Cerved()
    products = PRODUCTS.keys()
    parser = argparse.ArgumentParser(description="API Cerved Tutorial")
    parser.add_argument( '-p', '--product', 
                        help = 'Seleziona un prodotto per la ricerca tra quelli compresi nell\'elenco.',
                        required = True,
                        dest = 'product',
                        choices = products
                        )
    parser.add_argument('-e', '--entity',
                        help = 'Testo libero per la ricerca del codice id, accetta: codice fiscale, partita iva, ragione sociale.', 
                        )
    parser.add_argument('-i', '--id_soggetto',
                        help = 'Id identificativo del soggetto per effettuare le query.', 
                        type = str
                        )
    args = parser.parse_args()
    
    # Iterazione della chiave products per generare la chiamata al servizio corretto.
    if args.product in PRODUCTS.keys():
        if args.product == 'entity':
        # Gestione della ricerca 'entity' che accetta testo libero.
            if args.entity:
                try:
                    data = api.query(PRODUCTS['entity'], args.entity)
                    pprint(data)   
                except Exception as e:
                    print(e)
            else: 
                print('Per il prodotto selezionato è necessario impostare il parametro -e [--entity].')
        else:
        # Gestione degli altri casi che accettano 'id_soggetto' per le ricerche.
            if args.id_soggetto:
                try:
                    data = api.query(PRODUCTS[args.product], args.id_soggetto)
                    pprint(data)   
                except Exception as e:
                    print(e)
            else: 
                print('Per il prodotto selezionato è necessario impostare il parametro -i [--id_soggetto].')
