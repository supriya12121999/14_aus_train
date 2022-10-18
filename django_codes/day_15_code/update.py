import sqlite3
conn = sqlite3.connect('new.db')

c=conn.cursor()

c.execute("UPDATE record SET name = 'xy' where age>22")

conn.commit()

c.execute('SELECT * FROM record')



emp2 = c.fetchall()
for i in emp2:
    print(i)


conn.close()

