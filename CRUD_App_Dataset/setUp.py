import sqlite3

con = sqlite3.connect("myDb.db")

cursor = con.cursor()

try:
    cursor.execute("drop table toy")
except:
    pass

cursor.execute("create table toy(id integer primary key, toyName text, owner text)")

for item in ['Tarsan','Ninja','Spider Man']:
    cursor.execute(f"insert into toy(toyName, owner) values('{item}','No body')")

con.commit()