import sqlite3
conn = sqlite3.connect('vinnew.db')

c=conn.cursor()

#c.execute('''CREATE TABLE emp4 (name text, age int,salary real)''')

#c.execute("INSERT INTO emp VALUES ('Ravi',23,12300.50)")
c.execute("INSERT INTO info7 VALUES ('John',24)")
c.execute("INSERT INTO info7 VALUES ('kavi',30)")
#c.execute("INSERT INTO info VALUES ('hari',63,12500)")
#c.execute("INSERT INTO info VALUES ('rohan',40,17500)")
#c.execute("INSERT INTO info VALUES ('sohan',45,15500)")
#c.execute("insert into info values ('mohan',40,25500)")
#c.execute('''insert into info values ('abcd',49,25500)''')

conn.commit()

conn.close()
