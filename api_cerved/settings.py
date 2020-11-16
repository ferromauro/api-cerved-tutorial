CONSUMER_KEY = '' # PUT HERE YOUR API KEY

TEST_ENTITY = '03629080049'
TEST_ID_PROFILE = '370699071' 

PRODUCTS = {'entity':'/v1/entitySearch/live?testoricerca=',
            'profile':'/v1/entityProfile/live?id_soggetto=',
            'contacts':'/v1/entityProfile/contacts?id_soggetto=',
            'pec':'/v1/entityProfile/pec?id_soggetto=',
            'connections':'/v1/entityProfile/connections?id_soggetto=',
            'business_partners' : '/v1/entityProfile/businesspartners?id_soggetto=',
            'balance_sheet_list': '/v1/entityProfile/balancesheetslist?id_soggetto=',
            'beneficial_owner' : '/v1/entityProfile/beneficialowner?id_soggetto=',
            'beneficial_owner_plus' : '/v1/entityProfile/beneficialownerplus?id_soggetto=',
            'positions' : '/v1/entityProfile/positions?id_soggetto=',
            'shares' : '/v1/entityProfile/shares?id_soggetto=',
            'local_branches' : '/v1/entityProfile/localbranches?id_soggetto=',
            'negative_events' : '/v1/rischi/negative/events/'
            }