def deco(func):
    def inner():
        print('running inner')
    return inner

@deco
def target():
    print('running target()')

target()

def f1(a):
    print(a)
    print(b)

try:
    f1(3)
except NameError:
    print('name b is not defined')
b = 6
f1(3)

def f2(a):
    print(a)
    print(b)
    b = 9

try:
    f2(3)
except NameError:
    print('name b is not defined')
    print('python判断b时局部变量，因为在方法体中赋值了。')
    print('在尝试获取局部变量的值时，发现并没有绑定值')

def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(4)
print(b)
from dis import dis
dis(f1)