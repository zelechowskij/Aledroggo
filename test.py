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

con = cx_Oracle.connect("ALLEGRO_OWNER", "Password_001", "db202004242112_high")
print(con.version)
cur = con.cursor()
statement = 'select SETID, SEARCH_STRING from ALLEGRO_OWNER.SEARCH '
cur.execute(statement)
for row in cur:
    print(row)

con.close()