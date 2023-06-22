# split()
a = "i love python very much "
print(a.split())
b = "i-love-u-emaa"
print(b.split())
c = "i-love-u-emaa"
print(c.split("-"))
d = "i-love-u-emaa-very-much"
print(d.split("-", 2))
e = "i-love-u-emaa-very-much"
print(e.rsplit("-", 2))

# center()
f = "abdo"
print(f.center(10, "#"))  # 10-len(f)
g = "emaa"
print(g.center(10+len(g), "@"))

# count()
h = "i love emaa so much ,emaa is the best ,love u emaa"
print(h.count("emaa"))
i = "i love emaa so much ,emaa is the best ,love u emaa"
print(i.count("emaa", 13,))
j = "i love emaa so much ,emaa is the best ,love u emaa"
print(j.count("emaa", 25,))

# swapcase()
k = "I lOve EmAa"
l = "i LoVE eMaN"
print(k.swapcase())
print(l.swapcase())

# startswith()
m = "i love python"
print(m.startswith("i"))
n = "i love python"
print(m.startswith("p", 9))

# endswith()
o = "i love python"
print(o.endswith("e", 0, 6))
p = "i love python"
print(m.endswith("n", 0, 14))
