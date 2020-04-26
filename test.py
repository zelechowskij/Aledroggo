import requests
import Auth
import DefineSearch
import DefaultSettings
import pprint
import json


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
    print('1')
    params = {'phrase': 'xiaomi redmi note 8 pro', 'category.id': '300525', 'parameter.11323': '11323_1',
              'sellingMode.format': 'BUY_NOW', 'price.to': '1200', 'shippingFromPoland': '1', 'sort': 'price'}
    print('2')
    print(params)
    DEFAULT_SEARCH_URL = DefaultSettings.DEFAULT_API_URL + "/offers/listing"
    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(DEFAULT_SEARCH_URL, params=params)
        print(response)
        data = response.json()
        print(data)
        result = json.dumps(data)
        print(len(result))
        pp = pprint.PrettyPrinter(indent=3)
        pp.pprint(data['items'])
        for product in data['items']['regular']:
            print(product['sellingMode']['price'])
        for product in data['items']['promoted']:
            print(product['sellingMode']['price'])

    print('3')


test()
print('4')
