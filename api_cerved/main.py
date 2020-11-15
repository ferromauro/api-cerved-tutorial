import requests
import argparse
import json
from settings import CONSUMER_KEY
from pprint import pprint

def search_entity():
    """Imposta l'url ed effettua la ricerca di una entità in base a codice fiscale, partita Iva o ragione sociale."""
    if args.entity:
        url = '/v1/entitySearch/live?testoricerca='+args.entity
        try:
            data = query(url)
            return data
        except Exception as e:
            print(e)

    else:
        print('Per questo tipo di ricerca è necessario inserire il parametro -e [--entity].')
        parser.print_help()

def search_profile():
    """Imposta l'url ed effettua la ricerca di un profilo in base all'id del soggetto."""
    if args.id_soggetto:
        url = '/v1/entityProfile/live?id_soggetto='+args.id_soggetto
        try:
            data = query(url)
            return data
        except Exception as e:
            print(e)
    else:
        print('Per questo tipo di ricerca è necessario inserire il parametro -i [--id_soggetto].')
        parser.print_help()

def search_contacts():
    """Imposta l'url ed effettua la ricerca dei contatti di una entità in base all'id del soggetto."""
    if args.id_soggetto:
        url = '/v1/entityProfile/contacts?id_soggetto='+args.id_soggetto
        try:
            data = query(url)
            return data
        except Exception as e:
            print(e)
    else:
        print('Per questo tipo di ricerca è necessario inserire il parametro -i [--id_soggetto].')
        parser.print_help()

def search_pec():
    """Imposta l'url ed effettua la ricerca della pec di una entità in base all'id del soggetto."""
    if args.id_soggetto:
        url = '/v1/entityProfile/pec?id_soggetto='+args.id_soggetto
        try:
            data = query(url)
            return data
        except Exception as e:
            print(e)
    else:
        print('Per questo tipo di ricerca è necessario inserire il parametro -i [--id_soggetto].')
        parser.print_help()

def query(url):
    """Viene impostato l'header con la API Key ed effettua la query in base all'url passato come parametro. Vengono restituiti i dati."""
    headers = { 'accept':'application/json',
                'apikey': CONSUMER_KEY 
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
    products = ['entity', 'profile', 'contacts', 'pec']
    parser = argparse.ArgumentParser(description="API Cerved Tutorial")
    parser.add_argument(  '-p', '--product', 
                        help = 'Seleziona un prodotto per la ricerca tra quelli compresi nell\'elenco.',
                        required = True,
                        dest = 'product',
                        choices = products
                        )
    parser.add_argument('-e', '--entity',
                        help = 'Testo libero per la ricerca del codice id, accetta: codice fiscale, partita iva, ragione sociale.', 
                        )
    parser.add_argument('-i', '--id_soggetto',
                        help = 'Testo libero per la ricerca del codice id, accetta: codice fiscale, partita iva, ragione sociale.', 
                        type = str
                        )
    
    args = parser.parse_args()
    if args.product == 'profile':
        data = search_profile()
    if args.product == 'entity':
        data = search_entity()
    if args.product == 'contacts':
        data = search_contacts()
    if args.product == 'pec':
        data = search_pec() 
    if data:
        pprint(data)   
    else:
        args.print_help()