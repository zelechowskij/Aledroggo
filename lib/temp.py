import cx_Oracle
con = cx_Oracle.connect("admin", "Temporary1234", "db202004242112_high")
print(con.version)
cur = con.cursor()
statement = 'select * from CUSTOMERS'
cur.execute(statement)
res = cur.fetchall()
print(res)
con.close()