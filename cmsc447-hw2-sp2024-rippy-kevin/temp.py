import sqlite3
con = sqlite3.connect("database.db")

with open("temp.sql") as f:
    con.executescript(f.read())

cur = con.cursor()
con.commit()
con.close()
