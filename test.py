import requests
import Auth

def search_start():
    # Main function, will determine set of products, that interest user params=params
    DEFAULT_SEARCH_URL = Auth.DEFAULT_API_URL + "/offers/listing"

    headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
               "Authorization": "Bearer {}".format(Auth.access_token)}
    phrase = "xiaomi redmi note 8 pro"
    category = "300525"
    filter_temp = '?parameter.11323=11323_1sellingMode.format=BUY_NOWshippingFromPoland=1parameter.127448=127448_1'
    params = {'phrase': phrase, 'category.id': category, 'parameter.11323': '11323_2', 'sellingMode.format': 'BUY_NOW'}

    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(DEFAULT_SEARCH_URL+filter_temp, params=params)
        data = response.json()
        print(data['searchMeta'])


search_start()