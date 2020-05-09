import DefaultSettings
import cx_Oracle


def update_search_table(search_params_list):
    connection = cx_Oracle.connect(DefaultSettings.DEFAULT_ALLEGRO_OWNER_USERNAME,
                                   DefaultSettings.DEFAULT_ALLEGRO_OWNER_PASSWORD,
                                   DefaultSettings.DEFAULT_DB_CONNECTION_TYPE_HIGH)
    cursor = connection.cursor()

    params = search_params_list[0]
    email = search_params_list[1]
    status = 'Active'

    statement = 'INSERT INTO ALLEGRO_OWNER.SEARCH(SETID, SEARCH_STRING, EMAIL, STATUS, UPLOADED)' \
                ' SELECT ALLEGRO_OWNER.SEARCH_SQ.NEXTVAL, :params, :email, :status, SYSDATE FROM DUAL'

    cursor.execute(statement, params = str(params), email = email, status = status)

    connection.commit()
    connection.close()


def get_active_tasks():
    connection = cx_Oracle.connect(DefaultSettings.DEFAULT_ALLEGRO_USER_USERNAME,
                                   DefaultSettings.DEFAULT_ALLEGRO_USER_PASSWORD,
                                   DefaultSettings.DEFAULT_DB_CONNECTION_TYPE_HIGH)

    cursor = connection.cursor()
    status = 'Active'
    statement = 'SELECT SETID, SEARCH_STRING, EMAIL FROM ALLEGRO_OWNER.SEARCH WHERE STATUS = :status'

    cursor.execute(statement,status = status)

    active_tasks_list = []

    for row in cursor:
        temp_list = [row[0], row[1].read(), row[2]]

        active_tasks_list.append(temp_list)



    connection.close()

    return active_tasks_list


get_active_tasks()
