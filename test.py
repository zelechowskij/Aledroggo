import requests
import Auth
import DefineSearch
import DefaultSettings
import pprint
import json
import DbConnectionHandler
import cx_Oracle
import random


random_list = []

for i in range(30):
    n = random.randint(1, 300)
    random_list.append(n)

print(random_list)

best_deal = random_list[0]
for item in random_list:

    if item < best_deal:
        print(best_deal)
        best_deal = item
        print(best_deal)

print(best_deal)

# search_list = DefineSearch.search_start()
# print(search_list)
# DbConnectionHandler.update_search_table(search_list)

