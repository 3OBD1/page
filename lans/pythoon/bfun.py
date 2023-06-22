x = [1, 2, 3, 4]
if all(x):
    print("all is true")
else:
    print("1 or less is false")
print("-"*20)
y = [1, 2, 3, []]
if all(y):
    print("all is true")
else:
    print("1 or less is false")
print("-"*20)
z = [1, [], 0]
if any(z):
    print("1 or less is true")
else:
    print(" all false")
print("-"*20)
print(bin(100))
print("-"*20)
v = 1
m = 2
print(id(v))
print(id(m))
print("-"*20)


print(sum(x))  # x = [1, 2, 3, 4]
print(sum(x, 4))  # x+4
print("-"*20)
print(150.2324567643)
print(round(150.2324567643, 3))
print("-"*20)
print("hi emy i still love u")
print("hi", "emy", "i", "still", "love", "u", sep="|")
print("-"*20)
print("hi emy i still love u ", end="love u ")
print("again")
print("-"*20)
print(abs(100))
print(abs(-100))
print("-"*20)
print(pow(4, 3, 4))  # = (4*4*4)%4
print(pow(4, 3, 3))  # = (4*4*4)%4 باقي القسمه
print("-"*20)
print(min(1, 10, 9, 0))
print(min("a", "b", "x", "y", "z"))
print(min(x))
print("-"*20)
print(max(1, 10, 9, 0))
print(max("a", "b", "x", "y", "z"))
print(max(x))
