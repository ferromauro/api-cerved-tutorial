#! usr/env/bin python3
import unittest
import requests
import json
from api_cerved.main import Api_Cerved
from api_cerved import settings 

api = Api_Cerved()

class TestSearch(unittest.TestCase):
    def test_entity(self):
        """Test della funzione di ricerca delle entità per ricerca libera: cod. fiscale/partita iva o ragione sociale."""
        data = api.query(settings.PRODUCTS['entity'], settings.TEST_ENTITY)       
        self.assertEqual(data['companies'][0]['dati_anagrafici']['partita_iva'], settings.TEST_ENTITY )
    
    #def test_profile(self):
    #    """Test della funzione di ricerca del profilo per ricerca con id_soggetto."""
    #    data = api.query(PRODUCTS['profile'], TEST_ID_PROFILE)       
    #    self.assertEqual(data['dati_anagrafici']['partita_iva'], TEST_ENTITY )
    #

if __name__ == "__main__":
    unittest.main()