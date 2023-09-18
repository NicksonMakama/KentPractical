import sqlite3

con = sqlite3.connect("myDB.db")
cursor = con.cursor()

res = cursor.execute("SELECT * from pet")

myData = res.fetchall()

theName = [item[0] for item in list(res.description)]

toPrint = [dict(zip(theName, item)) for item in myData]

print(toPrint)



