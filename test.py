import requests
import Auth
import DefineSearch
import DefaultSettings
import pprint
import json
import DbConnectionHandler
import cx_Oracle
import random


search_list = DefineSearch.search_start()
print(search_list)
DbConnectionHandler.update_search_table(search_list)
# DEFAULT_SEARCH_URL = DefaultSettings.DEFAULT_SEARCH_URL
# params = {'phrase': 'telewizor', 'category.id': '257732', 'parameter.11323': '11323_1', 'sellingMode.format': 'BUY_NOW', 'price.from': '1500', 'price.to': '2500', 'parameter.211398': ['211398_488701', '211398_488541', '211398_249494'], 'parameter.211486': '211486_250138', 'parameter.194.from': '45', 'parameter.194.to': '50', 'sort': '+price', 'limit': 100}
#
# headers = Auth.load_default_headers()
# with requests.Session() as session:
#     session.headers.update(headers)
#     response = session.get(DEFAULT_SEARCH_URL, params=params)
#     data = response.json()
#     print(data['items'])