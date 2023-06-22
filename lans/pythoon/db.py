import sqlite3
db = sqlite3.connect("app.db")
cr = db.cursor()

cr.execute(
    "create table  if not exists skills (name text ,progress integer ,user_id integer )")
cr.execute("create table if not exists users (user_id integer , name text)")

ml = ["ahmed", "khaled", "m3wdd", "sayda", "om m7mood", "fthaiaa"]
for key, user in enumerate(ml):
    cr.execute(f"insert into users(user_id  , name) values({key},'{user}')")
# #دي وي اللي فوقها بالظبط
# cr.execute("insert into users(user_id  , name) values(1,'ahmed')")
# cr.execute("insert into users(user_id  , name) values(2,'sayed')")
# cr.execute("insert into users(user_id  , name) values(3,'abdo')")
cr.execute("select name from users")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
print(cr.fetchall())
print("s"*20)
cr.execute("select name ,user_id from users")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
print(cr.fetchall())
print("s"*20)
# دي غير اللي فوقها عشان الترتيب بتاع الكلام
cr.execute("select * from users ")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
print(cr.fetchall())


cr.execute("select * from users ")
print(cr.fetchmany())
print(cr.fetchmany(3))
db.commit()
db.close()
