# x = 1
# print(f"{x}")


def one():
    global x
    x = 2
    print(f"one is {x}")


def two():
    x = 4
    print(f"two is {x}")


def three():

    print(f"three is {x}")


one()
two()
three()  # will be the global
print(f"{x}")
