class DemoException(Exception):
    pass

def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('***DemoException Handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')

demo = demo_finally()
print(demo.send(None))
print(demo.send(12))
print(demo.send(12))
print(demo.send(12))
print(demo.send(12))
print(demo.send(12))
print(demo.throw(DemoException))