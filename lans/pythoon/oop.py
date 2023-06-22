# x = (input("what's your name ?"))


class member:
    def __init__(self):
        print("hi back")


member()


# class mo:
# def __init__(self):
#     print(f"hi {x}")


class mem:

    notallowednames = ["shahtoot", "3obd", "eman"]

    def __init__(self, fristname, secname, lastname):
        self.fn = fristname
        self.sn = secname
        self.ln = lastname


def fullname(self):

    if self.fn in mem.notallowednames:

        raise ValueError("name not allowed")

    else:
        return f"{ self.fn} { self.sn} { self.ln}"


def name(self):
    return f"hi mrs {self.fn}"


m1 = mem("shahtoot", "3obd", "eman")
m2 = mem("em", "an", "y")
m3 = mem("a", "ammo", "na")


print(m1.fn, m1.sn, m1.ln)
print(m2.fn, m2.ln, m2.fn, m2.sn, m2.fn, m3.fn)
print(m3.sn, m3.ln)
# mo()
