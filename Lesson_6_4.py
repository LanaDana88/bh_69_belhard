obj = [2, 2, 5, 8, '2', '9', 4, 889, 'lena', 'gena']
for i in range(len(obj) -1, -1, -1):
    if not isinstance(obj[i], str):
        del obj[i]

print(obj)

# с фильтром
obj = list(filter(lambda x: isinstance(x, str), obj))
obj = list(ob for ob in obj if isinstance(ob, str))
print(obj)

def obj(data):
    for i in range(len(data) - 1, -1, -1):
        if not isinstance(data[i], str):
            del data[i]
    return data

data = [2, 2, 5, 8, '2', '9', 4, 889, 'lena', 'gena']
itog = obj(data)
print(itog)


