name = "abdo"
age = 19
rank = 2
print("my n is :" + name)
print("my n is : %s" % "abdo")
print("my n is : %s" % name)
print("my n is : %s and my age is: %d" % (name, age))
print("my n is : %s and my age is: %d and my rank is: %.2f " % (name, age, rank))

# rearrange items
a, b, c = "emaa", "eman", "emy"
print("love u {} {} {} ".format(a, b, c))
print("love u {1} {2} {0} ".format(a, b, c))
print("love u {2} {1} {0} ".format(a, b, c))
