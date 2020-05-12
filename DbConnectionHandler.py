import DefaultSettings
import cx_Oracle


def establish_db_connection(user):

    if user == 'owner':
        username = DefaultSettings.DEFAULT_ALLEGRO_OWNER_USERNAME
        password = DefaultSettings.DEFAULT_ALLEGRO_OWNER_PASSWORD
        type = DefaultSettings.DEFAULT_DB_CONNECTION_TYPE_HIGH

    if user == 'user':
        username = DefaultSettings.DEFAULT_ALLEGRO_USER_USERNAME
        password = DefaultSettings.DEFAULT_ALLEGRO_USER_PASSWORD
        type = DefaultSettings.DEFAULT_DB_CONNECTION_TYPE_HIGH

    connection = cx_Oracle.connect(username, password, type)

    return connection


def update_search_table(search_params_list):
    connection = establish_db_connection('owner')
    cursor = connection.cursor()

    params = search_params_list[0]
    email = search_params_list[1]
    status = 'Active'
    params = str(params)
    statement = 'INSERT INTO ALLEGRO_OWNER.SEARCH(SETID, SEARCH_STRING, EMAIL, STATUS, UPLOADED)' \
                ' SELECT ALLEGRO_OWNER.SEARCH_SQ.NEXTVAL, :params, :email, :status, SYSDATE FROM DUAL'

    cursor.execute(statement, params = params, email = email, status = status)

    connection.commit()
    connection.close()


def get_active_tasks():
    connection = establish_db_connection('user')

    cursor = connection.cursor()

    status = 'Active'
    statement = 'SELECT SETID, SEARCH_STRING, EMAIL FROM ALLEGRO_OWNER.SEARCH WHERE STATUS = :status'

    cursor.execute(statement, status = status)

    active_tasks_list = []

    for row in cursor:
        temp_list = [row[0], row[1].read(), row[2]]

        active_tasks_list.append(temp_list)

    connection.close()

    return active_tasks_list


def update_data_table(item_list, setid):
    connection = establish_db_connection('owner')
    pass
