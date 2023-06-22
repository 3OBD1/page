import sqlite3
db = sqlite3.connect("awp.db")
cr = db.cursor()

cr.execute(
    "create table  if not exists skills (name text ,user_id integer ,progress integer )")
cr.execute("create table if not exists users ( name text ,user_id integer)")


def commitandclose():
    db.commit()
    db.close()
    print("connection closed")


im = """"
what do u want to  do?
"s"=> show skills
"a"=> add anew skill
"d"=> delete skill
"u"=> update skill
"q"=> quit all
choose option:
"""
ui = input(im).strip().lower()
# user id
uid = 1

command_list = ["s", "a", "d", "u", "q"]


def show_skills():
    cr.execute(f"select * from skills where user_id = '{uid}'")
    res = cr.fetchall()
    print(f"num of sk {len(res)}")

    if len(res) > 0:
        print("the show--->>---->>")

    for row in res:
        print(f" skill=> {row[0]} ", end=" ")
        print(f" progress=> {row[1]}")  # =(' '))

    commitandclose()


def add_skill():
    sn = input("skill name? ").strip()
    cr.execute(
        f"select name from skills where name = '{sn}' and user_id ={uid} ")
    res = cr.fetchone()
    if res != None:
        print(f"skill is exist , you cannot add it again ")

    else:
        print(" skill is not exist ")
    pro = input(" your progress is ").strip()
    cr.execute(
        f"insert into skills (name ,progress , user_id) values ('{sn}','{pro}','{uid}') ")

    commitandclose()


def delete_skill():
    sn = input(" skill name u want delete ?")
    cr.execute(f" delete from skills where name ='{sn}' and user_id = '{uid}'")

    commitandclose()


def update_skills():
    sk = input("write skill name :")
    prog = input("write the new skill progress:")
    cr.execute(
        f"update skills set progress ='{prog}' where name = '{sk}' and user_id ='{uid}'  ")
    commitandclose()


if ui in command_list:
    # print(f"good u choose lettter ({ui})")
    if ui == "s":
        show_skills()

    elif ui == "a":
        add_skill()

    elif ui == "d":
        delete_skill()

    elif ui == "u":
        update_skills()

    else:
        print("app closed ")
        commitandclose()


else:
    print(f"  command not founded ")
