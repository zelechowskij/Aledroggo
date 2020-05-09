import cx_Oracle


con = cx_Oracle.connect("ALLEGRO_OWNER", "Password_001", "db202004242112_high")
print(con.version)
cur = con.cursor()
statement = 'select * from ALLEGRO_OWNER.SEARCH '
cur.execute(statement)
for row in cur:
    print(row[0].read())

con.close()