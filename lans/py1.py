#!
print("file one ")


def hi():
    print("  fun from file one")


if 1 == 1:
    print("true ")

else:
    print("false")

if (__name__) == ("__main__"):
    print(" dirictally  from this file  ")  # يعني من الفايل اللي الفانكشن فيه
else:
    print("not dirictally")
hi()
