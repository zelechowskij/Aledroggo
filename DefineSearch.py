import requests
import Auth


# TO DO:
# prettyprint for json
# print for fetched data

def searchStart():
    DEFAULT_SEARCH_URL = Auth.DEFAULT_API_URL + "/offers/listing"

    headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
               "Authorization": "Bearer {}".format(Auth.access_token)}
    phrase = "xiaomi redmi note 8 pro"
    params = {"phrase": phrase}

    with requests.Session() as session:
        session.headers.update(headers)
        data = {'categories': {'subcategories': [{'id': 'cos'}, {'id': 'cos2'}]}}

        print(len(data['categories']["subcategories"]))

        while len(data['categories']['subcategories']) != 1:
            response = session.get(DEFAULT_SEARCH_URL, params=params)
            data = response.json()
            for categorie in data["categories"]["subcategories"]:
                print(categorie["name"] + ' ' + categorie["id"])

            temp_category = input()
            params["category.id"] = temp_category


searchStart()
