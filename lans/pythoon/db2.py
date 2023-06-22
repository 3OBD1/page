import sqlite3
db = sqlite3.connect("apw.db")
cr = db.cursor()

cr.execute(
    "create table  if not exists skills (name text ,progress integer ,user_id integer )")
cr.execute("create table if not exists users (user_id integer , name text)")

cr.execute("select * from users")

cr.execute(f"insert into users(user_id  , name) values(1,'ahmed')")
cr.execute(f"insert into users(user_id  , name) values(2,'ahuh')")
cr.execute(f"insert into users(user_id  , name) values(3,'hjhj')")
# update
# cr.execute("update users set name ='gamal' where user_id = 1")
# cr.execute("update users set name ='gama' where user_id = 2")
# cr.execute("update users set name ='amal' where user_id = 3")
# #delete
# cr.execute("delete from users where user_id =1 ")

db.commit()

db.close()
