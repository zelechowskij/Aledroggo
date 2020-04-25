import requests
import Auth
import DefineSearch
import DefaultSettings


def test():
    DEFAULT_SEARCH_URL = Auth.DEFAULT_API_URL + "/offers/listing"

    headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
               "Authorization": "Bearer {}".format(Auth.get_access_token)}
    phrase = "xiaomi redmi note 8 pro"
    category = "300525"
    params = DefineSearch.search_start()

    with requests.Session() as session:
        session.headers.update(headers)
        response = session.get(DefaultSettings.DEFAULT_API_URL, params=params)
        data = response.json()
        print(data)

test()