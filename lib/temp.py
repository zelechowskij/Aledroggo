import cx_Oracle


con = cx_Oracle.connect("ALLEGRO_OWNER", "Password_001", "db202004242112_high")
print(con.version)
cur = con.cursor()
statement = 'select * from ALLEGRO_OWNER.TEST '
cur.execute(statement)
for row in cur:
    print(row[0], type(row[1].read()), row[2])
    print(row[1].read())

con.close()