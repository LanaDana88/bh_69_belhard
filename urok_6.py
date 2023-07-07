# def simple_function(name):
#     print(f'Привет {name}! простая функция!')
#
#
# print(simple_function(name ='Katya'))
# simple_function('Lena')
#
# def simple_func(name):
#     return f'Привет {name}! Вот я такая простая функция!!!!'
# res = simple_func('VVVVV')
# print(res)
#
# def simple_func(n):
#     def vlozh_func():
#         print('Вот и Я!!! Вложенная функция!!!')
#     for i in range(n):
#         vlozh_func()
# simple_func(7)
#
# def multiply(x):
#     def power(y):
#         return x * y
#     return power
# x_3 = multiply(3)
# print(x_3(6))
#
# def multiply(x):
#     def power(y):
#         return x * y
#     return power
# x_3 = multiply(4)
# print(x_3(4))
#
# simple_funct = lambda x, n: x**n
# print(simple_funct(2, 3))
#
# text = ['a', '20', 's', '6', '8']
# text = list(filter(lambda x: x.isalpha(), text))
# print(text)
#
# a = [1, 2, 3, 4]
# b = 'xyz'
# c = (None, True)
# res = list(zip(a, b, c))
# print(res)
#
# def proizvolnoe_kolichestvo(*args):
#     print(list(args))
# proizvolnoe_kolichestvo(1, 2, 3, 5, 8, 9, 14, 37, 5, 77, 89, 98, 89)
#
# def pr_kol_vo(**kwargs):
#     print(kwargs)
# pr_kol_vo(a = 1, b = 8, c = 88, z = 77, s = 78)

# na_uroke_6
# data = {
#     'name': 'Lena',
# }
# data['age'] = '18'
# print(data)
# data['tel'] = '375-44-58-58-58'
# print(data)
# data['name'] = 'Kat'
#
# numbers = [5, 4, 8, 9, 6, 7, 8, 10]
# print(numbers[0])
#
# data = {'a': 5, 'z': 88}
# print(data['z'])
#
# user = {'name': 'Lena', 'email': 'lan@gmail.com', 'tel': '78-78-78-8'}
# user['city'] = 'Dubai'
# user['age'] = 27
# print(user)
#
# data = [
#     {'id': 5, 'name': 'Coffe', 'price': 5.28},
#     {'id': 2, 'name': 'Latte'}
# ]
# for inner_dict in data:
#     # if 'price' in inner_dict:
#     #     print(inner_dict['price'])
#     if inner_dict.get('price'):          # метод get
#         print(inner_dict['price'])

# ФУНКЦИИ

# def is_palindrome(text): #в скобках может быть, а может и не быть значения
#     text = text.lower()
#     print(text == text[::-1])
#
# is_palindrome('lena')
# is_palindrome('sos')

# def is_palindrome(text): #в скобках может быть, а может и не быть значения
#     text = text.lower()
#     print(text == text[::-1])
#
# is_palindrome('lena')
# is_palindrome('sos')

# def foo(a, b, c):
#     print(a, b, c)
#
# foo(2, 4, 1)

# можно передать явно
# def foo(a, b, c):
#     print(a, b, c)
#
# foo(a=2, c=4, b=1)


# def foo(a, b, c=34):
#     print(a, b, c)
#
# foo(5,6)

# def foo(a, b=None, c=34):
#     print(a, b, c)

# foo(5,6)
# def dar(*args): # тип данных передает - кортеж
#     print(args)
#
# dar(4, 8, 9, 7, 5,6, 3, 2, 'lena')
#
# def baz(**kwargs): #словарь
#     print(kwargs)
#
# baz(name='Lena', city='Dubai')

# def baz(a, b, c=45, *args, d=None, **kwargs):
#     print(a)
#     print(b)
#     print(d)
#     print(c)
#     print(args)
#     print(kwargs)
#
# baz(1, 2, 3, 4, 5, 6, 7, 8, 9)

# def baz(a, b, c=45, *args, d=None, **kwargs):
#     print(a)
#     print(b)
#     print(d)
#     print(c)
#     print(args)
#     print(kwargs)

# baz(1, 2, 3, 4, 5, 6, 7, 9, d=9, e=0)

# def func(a, b=[]): # добавляет значение в список, это не совсем верно
#     b.append(a)
#     print(b)
#
# func(4)
# func(4)
#
# # правильно так
# def func(a, b=None):
#     if b is None:
#         b = []
#     b.append(a)
#     print(b)
#
# func(4)
# func(4)

# def is_palindrome(text):
#      text = text.lower()
#      return text == text[::-1]
#
# result = is_palindrome('hello')
# print(result)


# def is_palindrome(text):
#     text = text.lower()
#     return text == text[::-1], text
#
#
# result = is_palindrome('hello')
# print(result) # результат кортеж

# TODO написать функцию, принимающую 3 целочисленных аргумента
# и возвращающую список чисел геомеитрической прогресии
# от а до b с множетелем
# 2, 4, 8, 16,  32, 64

def geo_progress(a, b, c):
    numbers = []
    while a < b:
        numbers.append(a)
        a *= c
    return numbers

print(geo_progress(2, 100, 2))

# TODO написать функцию average? принимающую неопределенное количество
# чисел и возвращающее среднее с точностью до 2

def average(*numbers):
    return round(sum(numbers) / len(numbers), 2)




