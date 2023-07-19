# def my_range(start, stop, step):
#     for i in range(start, stop, step):
#         yield i ** 2
#
# m = my_range(2, 188, 2)
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))
#
# # можно с циклом
# def my_range(start, stop, step):
#     for i in range(start, stop, step):
#         yield i ** 2
#
# m = my_range(2, 188, 2)
# for i in m:
#     print(i)
#
# # если писать не генератором, то будет так,
# # возвращается весь список значений
#
# def my_range(start, stop, step):
#     obj = []
#     for i in range(start, stop, step):
#         obj.append(i ** 2)
#     return obj

# написать генератор прогрессии от start до stop
# c множитеем multiplay

def mprogres(start, stop, multiplay):
    if start < stop and multiplay > 1:
        while start < stop:
            yield start
            start *= multiplay
    elif start > stop and multiplay < 1:
        while start > stop:
            yield start
            start *= multiplay
    else:
        raise ValueError


for i in mprogres(1, 20, 2.5):
    print(i)

def infinity_range(start, step): # бесконечная последовательность
    while True:
        yield start
        start += step

def foo1():
    print('foo1')


def foo2():
    print('foo2')


def foo3():
    print('foo3')

def error():
    print('error')

a = 'first'

data = {
    'first': foo1,
    'second': foo2,
    'third': foo3
}
data.get(a, error)()

a = 'first'

data = {
    'first': foo1,
    'second': foo2,
    'third': foo3
}
data.get(a, error)()
a = 'second'

data = {
    'first': foo1,
    'second': foo2,
    'third': foo3
}
data.get(a, error)()

a = 'third'

data = {
    'first': foo1,
    'second': foo2,
    'third': foo3
}
data.get(a, error)()

a = 'vndjsd'

data = {
    'first': foo1,
    'second': foo2,
    'third': foo3
}
data.get(a, error)()

# когда функция внутри себя может вызвать функции - callback функция

def bar():
    print('bar')

def baz(func):
    func()

baz(bar)

# zamikanie

def wrapper(a):

    def wrapped(b):
        print(a * b)

    return wrapped

a = wrapper(5)
a(6)

# декоратор

def is_digit_args(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError

        res = func(*args)
        return f'{res=}'

    return wrapper

def myltyply(*args):
    from functools import reduce
    return reduce(lambda x, y: x * y, args)

print(myltyply(1, 2, 3, 5, 8, 10, 11))
wrapped_myltiply = is_digit_args(myltyply)
print(wrapped_myltiply(3, 4, 5, 6, 7, 8))
print(wrapped_myltiply(3, '4', 5, 6, 8))

#если работает только с декоратором, то @

@is_digit_args
def myltyply(*args):
    from functools import reduce
    return reduce(lambda x, y: x * y, args)




























