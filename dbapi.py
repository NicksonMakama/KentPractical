import sqlite3

con = sqlite3.connect("myDB.db")
cursor = con.cursor()

res = cursor.execute("SELECT * from pet")

