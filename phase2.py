import DbConnectionHandler
import json
import Auth
import DefaultSettings
import requests
import math
import mail


def price_check(data, price_threshold, email):
    print(data)
    best_deal = data[0]
    for item in data:

        if float(item['amount']) < float(best_deal['amount']):

            best_deal = item

    if best_deal['amount'] <= price_threshold:
        mail.send_mail(best_deal, email, price_threshold)


def data_harvest(data, list):

    for item in data['promoted']:
        temporary_dict = {'id': item['id'], 'name': item['name'], 'amount': item['sellingMode']['price']['amount']}
        list.append(temporary_dict)
    for item in data['regular']:
        temporary_dict = {'id': item['id'], 'name': item['name'], 'amount': item['sellingMode']['price']['amount']}
        list.append(temporary_dict)


def check_allegro():
    DEFAULT_SEARCH_URL = DefaultSettings.DEFAULT_SEARCH_URL

    headers = Auth.load_default_headers()

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
            print(data['items'])
            data_harvest(data['items'], data_list)

            iterations = math.ceil(data['searchMeta']['availableCount']/100)

            for i in range(1, iterations + 1):
                offset = 100 * i
                params['offset'] = offset
                response = session.get(DEFAULT_SEARCH_URL, params=params)
                data = response.json()

                data_harvest(data['items'], data_list)
            print(params)
            price_check(data_list, price_threshold, email)

            DbConnectionHandler.update_data_table(data_list, set_ID)


check_allegro()