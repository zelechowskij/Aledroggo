import requests
import Auth
import DefineSearch
import DefaultSettings
import pprint
import json
import DbConnectionHandler
import cx_Oracle

search_list = DefineSearch.search_start()
print(search_list)
DbConnectionHandler.update_search_table(search_list)

