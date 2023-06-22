mylist = ["eman", "emmy", "emaa", "amoo", "em", "m"]
print(mylist)
print(mylist[1])
print(mylist[-1])
print(mylist[-5])
print(mylist[0:4])

# append()
mylist.append("mmom")
print(mylist)

# extand()
a = [1, 2, 3, 4]
b = ["h", "s", "f", "d"]
a.extend(b)
print(a)

# remove
x = [1, 2, 3, 4, 'h', 's', 'f', 'd']
x.remove(4)
print(x)

# sort()
y = [1, 2, 3, 4, 89, 66, 33, 11, -1]
y.sort()
print(y)
y.sort(reverse=True)
print(y)

# reverse()
z = [1, 2, 3, 4, 89, 66, 33, 11, -1]
z.reverse()
print(z)

# clear
i = [1, 2, 3, 4, 89, 66, 33, 11, -1]
i.clear()
print(i)

# insert()
o = [1, 2, 3, 4, 'h', 's', 'f', 'd']
o.insert(0, "eman")
print(o)
