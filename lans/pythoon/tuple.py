tup = ("ema", "eman", 'emy')
tup1 = "ema", "eman", 'emy'
print(tup)
print(tup1)
print(type(tup))
print(type(tup1))
print(tup[0])
print(tup1[-1])
# +value
tup2 = ("ema", "eman", 'emy')
# tup2[0] = "eman"
# print(tup2) 'tuple' object does not support item assigment

# tuple concatenation
a = (1, 2, 3, 4, 5, 6)
b = (7, 8, 9)
c = a+b
d = a+(10, 11, 12, "asd") + b
print(c)
print(d)
