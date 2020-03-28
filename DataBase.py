import mysql.connector



DEFAULT_DB_SERVER = "remotemysql.com"
DEFAULT_DB_PORT = "3306"


mydb = mysql.connector.connect(
    host = DEFAULT_DB_SERVER,

    user = DEFAULT_DB_USERNAME,
    password = DEFAULT_DB_PASSWORD,
    port = DEFAULT_DB_PORT,
    database = DEFAULT_DB_NAME)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

sql = "CREATE TABLE MyGuests (firstname VARCHAR(30) PRIMARY KEY)"

sql = "INSERT INTO MyGuests SELECT concat(firstname ,'ab3') FROM MyGuests"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
