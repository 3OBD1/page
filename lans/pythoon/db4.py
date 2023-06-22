import sqlite3
db = sqlite3.connect("aww.db")
cr = db.cursor()
cr.execute(
    "create table  if not exists skills (name text ,user_id integer ,progress integer )")
cr.execute("create table if not exists users ( name text ,user_id integer)")

cr.execute(
    f"insert into skills (name ,progress , user_id) values ('go','2','1') ")
cr.execute("select * from skills")
