def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received:', x)

my_coro = simple_coroutine()
print(my_coro)
print(next(my_coro))
print(my_coro.send(42))