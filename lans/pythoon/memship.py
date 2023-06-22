name = "eman"
print("e" in name)
print("A" in name)
print('@'*20)
# list
frinds = ["ahmed", "sayed", "khaled"]
print("ahmed" in frinds)
print("sds" in frinds)
print('@'*20)
coun1 = ["eg", "sua", "kata", "bahr"]
coun2 = ["israil", "usa", "franca"]
mcoun = "usa"
if mcoun in coun1:
    print("hi pro in heaven i love u and your country")
elif mcoun in coun2:
    print("fuck u pitch get off")
la = input("do u love plastin ?")
if la == 'yes' or la == "y" or la == "yep":
    print("hello pro")
else:
    print("fuck u")

# not in زي اللي فةق بالظبط
admins = ["ahmed", "sayed", "khaled", "sasa", "emy"]
yourname = input("your name?")
if yourname in admins:
    print(f"hi {yourname} u r admin")

    option = input("delete or update?")
    if option == "update" or option == "u":
        newname = input("your new name?")
        admins[admins.index(yourname)] = newname
        print("updated.")
        print(admins)
    elif option == "delete" or option == "d":
        admins.remove(yourname)
        print("name deleted")
        print(admins)
    else:
        print("wrong option")


else:
    print("u r not admin")
