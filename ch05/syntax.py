def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)

print(factorial.__doc__)
print(type(factorial))
print(factorial(10))
print(help(factorial))
fact = factorial
print(map(fact, range(10)))
print(list(map(fact, range(10))))
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))

from functools import reduce
from operator import add
print(reduce(add, range(100)))
print(sum(range(100)))

class C: pass
obj = C()
def func(): pass
print(sorted(set(dir(func)) - set(dir(obj))))

def tag(name, *content, cls=None, **attrs):
    '''生成一个或者多个HTML标签'''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                            for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'hello world'))
print(tag('p', 'hello', 'hello world', cls='sidebar'))