def asd():
    print("#"*30)


asd()
asd()


def a():
    return "asds"


print(a())

asd()


def b():
    return "asd"


asas = b()
print(asas)
asd()
d, e, f = "sasa", "dada", "fafa"
print(f"hello {d}")
print(f"hello {e}")
print(f"hello {f}")

asd()


def waw(saw):
    print(f"hello {saw}")


waw("sasa")
asd()


def add(n1, n2):
    print(n1+n2)


add(12, 12)
asd()


def dsa(*peo):
    for name in peo:
        print(f"hi {name}")


dsa("gf", "jhb")
# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------


def show_skills(*skills):

    print(type(skills))

    for skill in skills:

        print(f"{skill}")


show_skills("Html", "CSS", "JS")

mySkills = {
    'Html': "80%",
    'Css': "70%",
    'Js': "50%",
    'Python': "80%",
    "Go": "40%"
}


def show_skills(**skills):

    print(type(skills))

    for skill, value in skills.items():

        print(f"{skill} => {value}")


show_skills(**mySkills)


def skills(name, *skills):
    print(f"hi {name}")
    for skill in skills:
        print(f"{skill}")


skills("3obd", "js", "java", "py")
