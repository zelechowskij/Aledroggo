import requests
import Auth
import DefineSearch
import DefaultSettings
import pprint
import json
import DbConnectionHandler


def test():
    DEFAULT_SEARCH_URL = Auth.DEFAULT_API_URL + "/offers/listing"
    print('0')
    token = Auth.get_access_token()
    print(token)
    headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
               "Authorization": "Bearer {}".format(token)}
    phrase = "xiaomi redmi note 8 pro"
    category = "300525"

    params = {'phrase': phrase, 'category.id': category, 'parameter.11323': '11323_1',
              'sellingMode.format': 'BUY_NOW', 'price.to': '1200', 'shippingFromPoland': '1', 'sort': 'price','limit': '100'}
    print(params)

    search_string = DefineSearch.finalize_search(params)
    DbConnectionHandler.update_search_table(search_string)


test()

