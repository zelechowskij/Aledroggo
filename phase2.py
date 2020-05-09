import DbConnectionHandler
import json
import Auth
import DefaultSettings
import requests
import math


def data_harvest(data, list):

    for item in data['promoted']:
        temporary_dict = {'id': item['id'], 'name': item['name'], 'amount': item['sellingMode']['price']['amount']}
        list.append(temporary_dict)
    for item in data['regular']:
        temporary_dict = {'id': item['id'], 'name': item['name'], 'amount': item['sellingMode']['price']['amount']}
        list.append(temporary_dict)


access_token = Auth.get_access_token()
DEFAULT_SEARCH_URL = DefaultSettings.DEFAULT_SEARCH_URL
headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
           "Accept": 'application/vnd.allegro.public.v1+json',
           "Authorization": "Bearer {}".format(access_token)}

active_tasks_list = DbConnectionHandler.get_active_tasks()


with requests.Session() as session:
    session.headers.update(headers)
    for task in active_tasks_list:
        set_ID = task[0]
        params = task[1]
        params = params.replace("'", "\"")
        params = json.loads(params)
        price_threshold = params['price_threshold']
        del params['price_threshold']
        email = task[2]

        response = session.get(DEFAULT_SEARCH_URL, params=params)
        data = response.json()
        print(data['searchMeta'])
        data_list = []
        data_harvest(data['items'], data_list)
        iterations = math.ceil(data['searchMeta']['availableCount']/100)
        for i in range(1, iterations + 1):
            offset = 100 * i
            params['offset'] = offset
            response = session.get(DEFAULT_SEARCH_URL, params=params)
            data = response.json()
            data_harvest(data['items'], data_list)

        print(data_list)
        print(len(data_list))