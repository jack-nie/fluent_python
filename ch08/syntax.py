a = 1
b = a
print(a is b)
print(a == b)
print(id(a))
print(id(b))
a = 2
print(b)
print(a)
print(a is b)
print(a == b)
c = {'jack': 'nie'}
d = c
print(c is d)
print(c == d)
print(id(c))
print(id(d))
d['jack'] = "name"
print(c)
print(d)
print(c is d)
print(c == d)
t1 = (1,2,[30,40])
t2 = (1,2,[30,40])
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)
l1 = [3,[55,44],[7,8,9]]
l2 = list(l1)
print(l2 == l1)
print(l2 is l1)
l1.append(100)
l1[1].remove(55)
print(l2)
print(l1)
l1 += [33,22]
l2 += [10, 11]
print(l1)
print(l2)
def f(a, b):
    a += b
    return a
x = 1
y = 2
print(f(x, y))
print(x, y)
a = [1,2]
b = [3, 4]
f(a, b)
print(a)
c = (1, 2)
d = (3,4)
f(c, d)
print(c)
