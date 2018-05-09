
from functools import wraps

def coroutine(func):
    @wraps
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

co = average()
print(next(co))

print(co.send(12))
print(co.send(15))
print(co.send(16))
