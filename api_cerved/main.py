import requests
import argparse
import json
from settings import API_KEY

from pprint import pprint
def search_entity(free_text):
    """Imposta l'url per la ricerca di una entità in base a codice fiscale, partita Iva o ragione sociale."""
    url = '/v1/entitySearch/live?testoricerca='+free_text
    return url
        
def query(url):
    """Viene impostato l'header con la API Key ed effettua la query in base all'url passato come parametro. Vengono restituiti i dati."""
    headers = { 'accept':'application/json',
                'apikey': API_KEY 
              }
    try :
        query_url = 'https://api.cerved.com/cervedApi'+url
        print(query_url)
        r = requests.get(query_url, headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            print('La richiesta non è andata a buon fine: risposta del server codice: ' + str(r.status_code))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    """API-CERVED-TUTORIAL"""
    products = ['profile','contacts','pec', 'entity']
    parser = argparse.ArgumentParser(description="API Cerved Tutorial")
    parser.add_argument(  '-p', '--product', 
                        help = 'seleziona un prodotto per la ricerca.',
                        required = True,
                        dest = 'product',
                        choices = products
                        )
    parser.add_argument('-e', '--entity',
                        help = 'Testo libero per la ricerca del codice id, accetta: codice fiscale, partita iva, ragione sociale.', 
                        dest = 'entity')
    
    parser.add_argument('-t', '--tax_number',
                        help = 'inserisci un codice fiscale o una partita IVA.',
                        dest = 'tax_number'
                        )

    args = parser.parse_args()
    if args.product == 'profile':
        search_profile(args.tax_number)
    if args.product == 'entity':
        data = query(search_entity(args.entity))
        pprint(data)   
