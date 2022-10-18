
#sqlite3 is a pre-installed database in python
import sqlite3


#create db file then establish connection
conn = sqlite3.connect('new.db')

#now creating cursor class object
#for executing sql queries
c=conn.cursor()


#call execute() method for running sql query
c.execute("CREATE TABLE if not exists record(name text,age int)")

for i in range(3):
    a=input('enter name:')
    b=int(input('enter age:'))


    c.execute("INSERT INTO record VALUES (?,?)",(a,b))
    
#c.execute("insert into record values ('xyz',13)")

#to save changes in database,call commit() method
conn.commit()

conn.close()
