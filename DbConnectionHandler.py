import DefaultSettings
import cx_Oracle


def update_search_table(search_params_list):
    connection = cx_Oracle.connect(DefaultSettings.DEFAULT_ALLEGRO_OWNER_USERNAME,
                                   DefaultSettings.DEFAULT_ALLEGRO_OWNER_PASSWORD,
                                   DefaultSettings.DEFAULT_ALLEGRO_OWNER_PASSWORD)
    cursor = connection.cursor()

    params = search_params_list[0]
    email = search_params_list[1]
    status = 'Active'

    statement = 'INSERT INTO ALLEGRO_OWNER.SEARCH(SETID, SEARCH_STRING, EMAIL, STATUS, UPLOADED)' \
                ' SELECT ALLEGRO_OWNER.SEARCH_SQ.NEXTVAL, :params, :email, :status, SYSDATE FROM DUAL'

    cursor.execute(statement, params = str(params), email = email, status = status)

    connection.commit()
    connection.close()
