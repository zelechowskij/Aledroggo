import DefaultSettings
import cx_Oracle

username = DefaultSettings.DEFAULT_ALLEGRO_OWNER_USERNAME
password = DefaultSettings.DEFAULT_ALLEGRO_OWNER_PASSWORD
connType = DefaultSettings.DEFAULT_DB_CONNECTION_TYPE_HIGH

def make_connection(username, password, connType):
    con = cx_Oracle.connect(username, password, connType)
    return con


def update_search_table(search_params_list):
    connection = make_connection(username, password, connType)
    cursor = connection.cursor()
    params = search_params_list[0]
    email = search_params_list[1]
    status = 'Active'

    statement = 'INSERT INTO ALLEGRO_OWNER.SEARCH(SETID, SEARCH_STRING, EMAIL, STATUS, UPLOADED)' \
                ' SELECT ALLEGRO_OWNER.SEARCH_SQ.NEXTVAL, :params, :email, :status, SYSDATE FROM DUAL'

    cursor.execute(statement, params = str(params), email = email, status = status)

    connection.commit()
    connection.close()