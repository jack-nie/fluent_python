from collections import namedtuple

Result = namedtuple('Result', 'count average')

def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

demo = average()
print(next(demo))
print(demo.send(12))
print(demo.send(10))
print(demo.send(17))

try:
    print(demo.send(None))
except StopIteration as e:
    result = e.value

print(result)