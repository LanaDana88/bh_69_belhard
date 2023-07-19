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

# def geo_progress(a, b, c):
#     numbers = []
#     while a < b:
#         numbers.append(a)
#         a *= c
#     return numbers
#
# print(geo_progress(2, 100, 2))
#
# # TODO написать функцию average? принимающую неопределенное количество
# # чисел и возвращающее среднее с точностью до 2
#
# def average(*numbers):
#     return round(sum(numbers) / len(numbers), 2)


# анономная функция lambda
# multiply = lambda x, y: x * y
# print(multiply(4, 5))


numbers = [2, 3, 4, 5, '2', '4', '6', 8, 9]
# эта функция формирует список промежуточных значений,
# делет их строчными, т.е.
#приводит их к строке  ('2', '3', '4', '5', '2', '4', '6', '8', '9')
# затем этот промежуточный список сортирует
# numbers.sort(key=lambda x: str(x))
# print(numbers)

# data = [
#     {'name': 'Vasya', 'age': 45},
#     {'name': 'Petya', 'age': 23},
#     {'name': 'Masha', 'age': 18},
#     {'name': 'Maksim', 'age': 28}
# ]
# #по возрасту
# data.sort(key=lambda user: user.get('age'))
# print(data)
# max(data, key=lambda user: user.get('age'))
# min(data, key=lambda user: user.get('age'))
# print(max(data, key=lambda user: user.get('age')))
# print(min(data, key=lambda user: user.get('age')))


# numbers = input().split()
# numbers = [int(numbers) for numbers in numbers]
# print(numbers)
#
# #через map
# numbers = input().split()
# numbers = map(lambda x: int(x), numbers)
# print(numbers)
#
# numbers = input().split()
# numbers = map(lambda x: int(x) ** 2, numbers)
# print(numbers)
#
# numbers = input().split()
# numbers = list(map(lambda x: int(x) ** 2, numbers))
# print(numbers)


#
# numbers = ['1', '2', '3', '4', '5']
# numbers = [int(numbers) ** 2 for numbers in numbers]
# print(numbers)
#
# numbers = ['1', '2', '3', '4', '5']
# numbers = list(map(lambda x: int(x) ** 2, numbers)) # нельзя дописать условие
# print(numbers)
#
# # фильтр
#
# numbers = ['1', '2', '3', '4', '5']
# numbers = [int(numbers) ** 2 for numbers in numbers]
# numbers = [number for number in numbers if number % 2]
# numbers = filter(lambda x: x % 2, numbers)          #итератор
# numbers = list(filter(lambda x: x % 2, numbers))    #лист
# print(numbers)

#TODO s_vidio_urok_6

def is_palindrome(text):
    text = text.lower()
    print(text == text[::-1])
is_palindrome("lana")
is_palindrome('ШаЛаш')

#позиционный

def foo(a, b, c):
    print(a, b, c)

foo(2, 4, 18) #передача по позициям, за искл.явной передачи

def foo(a, b, c=7):
    print(a, b, c)
foo(a=3, b=88)

def foo(a, b=156, c=7): # чаще всего пердают явно, растет читабельность кода
    print(a, b, c)
print(foo.__defaults__)

foo(3)

# необязательные аргументы, по умолчание значение None
def foo(a, b=None, c=87):
    print(a, b, c)

def bar(*args): #args - кортеж
    print(args)
bar(4, 5, 8, 9, 'lena')


def baz(**kwargs): #kwargs - словарь
    print(kwargs)
baz(name = 'lena', city = "Dubai", age = 38)

# обязательные оппозиционные, всегда принимает первыми
# **kwargs всегда принимает последними
# все остальные в любом порядке, как необходимо
def bas(a, b, c=88, *args, d=None, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(d)
    print(kwargs)

bas(10, 8, 43, 75, 88, 9, 14, 69, 78, 12)

bas(10, 8, 43, 75, 88, 9, 14, 69, d=78, e=12)

def func(a, b=[]): # не индепотентна
    b.append(a)
    print(b)
func(4)
func(4)

# решение этой проблемы, чтобы функция была идемпотентной
def func(a, b=None): # не индепотентна
    if b is None:
        b = []
    b.append(a)
    print(b)
func(4)
func(4)

#если нуждно вернуть рез-т работы

def is_palindrome(text):
    text = text.lower()
    return (text == text[::-1])

res = is_palindrome("lana") #=False
print(res)

def is_palindrome(text):
    text = text.lower()
    return (text == text[::-1]), text # рез-т кортеж

res = is_palindrome("lana")
print(res)

a = 9.99
a1 = 9.99
a2 = 3.045
print((a + a1)*a2)

# TODO написать функцию при помощи 3-х челочисленных аргументов (а, b, c)
#  и возвращающая список чисел геометрической прогрессии о
#  т а до B с множетелем с, a=2, d=169, c=2 [2, 4, 8, 16, 64]

def geo_prog(a, b, c):
    numbers = []
    while a < b:
        numbers.append(a)
        a *= c
    return numbers

prog = geo_prog(2, 169, 2)
print(prog)

#TODO написать функцию average, принимающую неопределенное количество
#  чисел и возвращающая среднее значение с точностью 2

def average(*args):
    return round(sum(args) / len(args), 2)
res = average(2, 8, 9, 7, 5, 6, 3, 4, 28, 888)
print(res)

# анонимные функции lambda

myltiply = lambda x, y: x * y
print(myltiply(4, 8))

numbers = [4, 8, 9, '2', '99', 18, 45, '99']
numbers.sort(key=lambda x: str(x))
print(numbers)

data = [
    {"name": "Lena", 'age': 45},
    {"name": "Dima", 'age': 23},
    {"name": "Katya", 'age': 21},
    {"name": "Vam", 'age': 18},
]
# сортруем по возрастам

data.sort(key=lambda x: x.get('age'))
print(data)

starshii = max(data, key=lambda x: x.get('age'))
print(starshii)

# # класс map
# numbers = input().split()
# numbers = [int(number) for number in numbers]
# print(numbers)
#
# numbers = input().split()
# numbers = map(lambda x: int(x), numbers)
# print(numbers)
#
# numbers = input().split()
# numbers = map(lambda x: int(x) ** 2, numbers)
# print(numbers)
#
# numbers = input().split()
# numbers = list(map(lambda x: int(x) ** 2, numbers))
# print(numbers)

# filter

# numbers = ['1', '2', '3', '4', '5']
# numbers = [int(number) ** 2 for number in numbers]
# numbers = [number for number in numbers if number % 2]
# numbers = filter(lambda x: x % 2, numbers)
# numbers = list(filter(lambda x: x % 2, numbers))
# print(numbers)

#TODO написать функцию, принимающую спсок чисел и возв. список
# с аккумулятив суммой
# пример [1, 2, 3, 4, 5]
# ответ [1, 3, 6, 18, 15]

def acumilytive(numbers):
    x = 0
    res = []
    for number in numbers:
        x += number
        res.append(x)
    return res

itog = acumilytive([1, 2, 3, 4, 5, 6])
print(itog)

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
print(reduce(lambda x, y: x * y, numbers))

#TODO написать функцию, is_pangramm принимающую строку и взвр.
#  True - если строка явл. панграмм
#  False - если строка не панграмм

from string import ascii_lowercase

def is_pangram(text):
    text = text.lower()
    for letter in ascii_lowercase:
        if letter not in text:
            return False
    return True

pam= is_pangram('hello')
print(pam)

























































