import requests
import Auth
from pprint import pprint

# TO DO:
# prettyprint for json
# print for fetched data

def searchStart():
    DEFAULT_SEARCH_URL = Auth.DEFAULT_API_URL + "/offers/listing"

    headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
               "Authorization": "Bearer {}".format(Auth.access_token)}
    phrase = "xiaomi redmi note 8 pro"
    category = "300525"
    params = {"phrase": phrase, 'category.id': category}

    with requests.Session() as session:
        session.headers.update(headers)
        data = {'categories': {'subcategories': [{'id': 'temp'}, {'id': 'temp2'}]}}

        while len(data['categories']['subcategories']) != 1:
            response = session.get(DEFAULT_SEARCH_URL, params=params)
            data = response.json()

            for categorie in data["categories"]["subcategories"]:
                pprint(categorie["name"] + ' ' + categorie["id"])

            temp_category = input()
            params["category.id"] = temp_category

        # when displaying filters add count parameter
        # important to distinct filter type e.g. multi or text type!

        filters = {}
        for filter in data['filters']:
            print(filter)
            print(filter['name'])
            for value in filter['values']:
                print(str(list(value.values())[1]) + ' ' + str(list(value.values())[0]))




searchStart()
