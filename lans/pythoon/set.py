# union
a = {'q', '2', '4'}
b = {'m', 'n', "g"}
print(a | b)
print(a.union(b))
# add
c = {1, 2, 3, 4, 5}
c.add(0)
print(c)
d = {1, 2, 3, 4, 5}
e = d.copy()
print(d)
print(e)
# discard
f = {1, 2, 3, 4, 5, 0}
f.discard(7)
f.discard(1)
print(f)
# remove
g = {1, 2, 3, 4, 5, 0}
# g.remove(7) =error
g.remove(1)
print(g)

# pop() choose random one
i = {'a', '2', '3', 'pop'}
print(i.pop())
# update()
j = {1, 2, 3, 4, 5, 6, 7, 8}
k = {4, 6, 8, 2, 3}
j.update(k)
print(j)
# difference()
k = {1, 2, 3, 4, 5, 6}
l = {1, 2, 'asd', 'dfg'}
print(k)
print(k.difference(l))  # =j-k
# difference_update
m = {1, 2, 3, 4, 5, 6}
n = {1, 2, 'asd', 'dfg'}
print(m)
print(m.difference_update(n))
# issuperset
o = {1, 2, 3, 4, 5}
p = {1, 3, 2, 4}
q = {1, 2, 3, 4, 5, 6}
print(o.issuperset(p))
print(o.issuperset(q))
# issubset oppiste issuperset
