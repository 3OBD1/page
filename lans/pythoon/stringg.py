import string
import random


def mser(count):
    allc = string.ascii_letters + string.digits
    # print(allc)
    charscount = len(allc)
   # print(charscount)
    emptylist = []
    while count > 0:
        random_num = random.randint(0, charscount-1)
        random_charactor = allc[random_num]
       # print(random_charactor)
        emptylist.append(random_charactor)
        count -= 1
    print("".join(emptylist))


mser(20)



# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
