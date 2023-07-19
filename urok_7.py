def my_range(start, stop, step):
    for i in range(start, stop, step):
        yield i ** 2

m = my_range(2, 188, 2)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))

# можно с циклом
def my_range(start, stop, step):
    for i in range(start, stop, step):
        yield i ** 2

m = my_range(2, 188, 2)
for i in m:
    print(i)

# если писать не генератором, то будет так,
# возвращается весь список значений

def my_range(start, stop, step):
    obj = []
    for i in range(start, stop, step):
        obj.append(i ** 2)
    return obj














