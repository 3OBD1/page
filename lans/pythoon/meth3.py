# find(substring,start,end)
a = "i love u emma"
print(a.find("a"))
print(a.find("e", 3, 12))
print(a.find("i", 6, 12))
# rjust(width,fill char)    ljust(width,fill char)
b = "eman"
print(b.rjust(10))
print(b.rjust(10, "@"))
print(b.ljust(10))
print(b.ljust(10, "@"))

# splitlines()
c = """i 
love u 
emaa"""
print(c.splitlines())
d = "i \nlove u\nemaa"
print(d.splitlines())

# expandtabs(arg)
e = "i\tlove\temaa"
print(e.expandtabs())
print(e.expandtabs(10))

# replace(old value,new...,count)
f = "i love u emma love u  and love u"
print(f.replace("love", "like", 2))

# join(iterable)
list1 = ["abdo", "emaa", "love"]
print(" ".join(list1))
print("## ".join(list1))
print(" !@#".join(list1))
