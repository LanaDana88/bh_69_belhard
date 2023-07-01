# numbers = [1, 2, 3, 4, 5, 8, 10]
# print(numbers)

# colors = list(('красный', 'green', 'blue'))
# print(colors)
#
# words = ['apple', 'box', 'milke', 'like']
# uppercase_words = [word.upper() for word in words]
# print(uppercase_words)

# some_list = [2, 5, 7, 8, 10, 5]
# del some_list[1:3:1]
# print(some_list)

# elem = some_list.remove(10)
# elem = some_list.pop(2)
# print(some_list)
# print(elem)

# search1 = 8 in some_list
# search2 = 3 in some_list
# print(search1)
# print(search2)

# some_list.append(15)
# print(some_list)

# some_list.insert(1, 20)
# print(some_list)

# words = 'Ekaterina, Alena'
# some_list.extend(words)
# print(some_list)

# some_list.index(7)
# print(some_list.index(10))

# some_list.count(5)
# some_list.count(11)
# print(some_list.count(5))
# print(some_list.count(11)) # если элемента нет, то выодит 0

# some_list = [2, 5, 7, 8, 10, 5]
# sorted(some_list)
# sorted(some_list, reverse = True)
# some_list.sort()
# some_list.sort(reverse = True)
# print(some_list)

# some_list.reverse()
# print(some_list)

# some_list1 = [2, 5, 7, 8, 10, 5]
# some_list1.clear()
# print(some_list1)

# some_list1.copy()
# print(some_list1)

# tuple_1 = ()
# # print(tuple_1)
# tuole_2 = tuple()
# print(tuple)

# set{1, 5, 7, 8, 10}

# number = [ ]
# n = 2
# list_number = [2 ** number for number in range(1, n+1)]
#
# # print(list_number)
# from collections import Counter
#
# letter_counter = Counter(input().split())
# text = input({})
# dict = {i: text.count(i) for i in text}
# print(dict)

# list = [2, 5, 8, 9, 10, 15, 48, 25, 18, 0]
# my_list = {}
# for items in list:
#     my_list[items] = my_list.get(items, 0) + 1
#
# #         print(my_list.items())
# n= 1
# my_dict = {}
# for items in my_dict:
#     my_dict[items] = my_dict.get([i for i in range(1, n+1)])
#     print(my_dict)

# numbers = [1, 2, 5, 4, 7, 8, 11, 15, 18]
# words = ['hello', 'python', 'world']
# # print(words[1][2])
#
# l = list('hello')
# # print(l)
#
# letters = list('hello')
# numbers2 = [i ** 2 for i in range(1, 100)]    #хочу квадраты чисел от 1 до 100
# print(numbers2)
#
# words[1] = 'jcsdgvsd'
# print(words)
#
# # del numbers[0:2]
# # print(numbers)
#
# # number = numbers.pop(2)
# # print(number)
#
# #удаление по значению
#
# numbers.remove(8)
# #numbers.remove(8) #при вызове второй раз, если нет такого значения, то будет ошибка
# print(numbers)

# obj = [2, 3, 5, 8, 9, 5]
# obj.append(10)
# obj.append([12, 15, 18]) #всегда добавляет в конец, одно значение, один аргумент
# print(obj)

#insert добавление по индексу

obj = [2, 3, 5, 8, 9, 5]
# obj.insert(2, 9)
# obj.insert(2, 'lena')
# obj.insert(2, 3) #список раздвигатся, указываем индекс и что добавить
# print(obj)

# obj.extend('привет лена') #сторого расширение в конец, текст разбивает по буквам
# obj.extend('787879')
# print(obj)

#a = [2, 5, 8, 9]
# z = [7, 8, 10, 1]
# n = a + z
# print(n * 5) #делаем дубли списка

# a = [2, 5, 8, 2, 10, 2, 9]
# print(a.count(2)) # считает по всему спску

# numbers = [1, 10, 14, 48, 5, 6, 98, 1, 3, 6, 8, 7]
# # numbers.sort(reverse=True)
# # print(numbers)
# print(sorted(numbers, reverse=True))   #получим отсортирванную копию

# a = [1, 2, 3, 4] #поверхностное копирование
# # z = a
# # a.append(2)
# # b = a.copy()
# # b = a[:] #через срез
# b = list(a)
# print(b)
# #z = [a, 5, 6, 7]

# a = [1, 2, 3, 4]
# b = [a, 6, 5, 7]
# c = b.copy()
# a.append(5)
# print(b)
# print(c)

#сравление списков

# a = [1, 2, 3, 4, 5]
# b = [1, 2, 3, 4, 5]
# print(a is b)
# print(a == b)
# print(a[0] is b[0])
# c = 1
# print(a[0] is b[0] is c)

# Кортеж не изменяемый список
# status = (200, )
# status1 = 200, 300
# print(status)
# print(status1)

# a = (1, 2, 3, 4, [7, 8, 9]) #то что в квадратных скобках поменять можно
# a[4].append(11)
# print(a)

# available_methods = ('get', 'post')

#множества

# s = {1, 2, 3, 5, 8, 9, 11, 's', 'war'}
# print(s)

# a = set('hello') #обратитося по индексу не получиться,
# # т.к. каждый раз меняет по своему
# print(a)
# numbers = [1, 2, 5, 8, 9, 658, 78, -11, 12]
# numbers = set(numbers)
# # print(numbers)
# print(numbers.isdisjoint({3, 18, 25, 100})) #принимает объект, явл set
#
# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 2, 1, 8, 10, 78} # проверка на то, что множество б входит в множество а
# # print(a.issubset(b))
# #
# # c = a.union(b, {77, 88, 99, 'lena'})
# # print(c)
# # print(a | b | {77, 888, 99, 55})
#
# print(a.difference(b))
#
# #DICT - словари
#
# data = {}
# print(type(data))

# data = {
#     'name': 'Lena',
#     'age': 25,
#     'number': 375_29_6105_229
# }
# #
# print(data['name'])
# data['name'] = 'Alena'
# data['city'] = 'Dubai'
# print(data)

# data = dict([('name', 'katy'), ('age', 15), ('city', 'dubai')])
# print(data)
#
# data = {
#     'name': 'Lena',
#     'age': 25,
#     'number': 375_29_6105_229
# }

# print(data.get('city'))
# print(data.setdefault('page', 'нет значения'))
# print(data)
#
# print(data.pop('page'))
# print(data)

# print(list(data))

# print(data.keys())
# print(data.values())
# print(data.items())
#
# data = {
#     'name': 'Lena',
#     'age': 25,
#     'number': 375_29_6105_229
# }
# new_data = {
#     'name': 'Lesha',
#     'city': 'Praga'
# }
# # data.update(new_data)
# # print(data)
#
#  # обновить словарь, но сделав копию,
# # сам словарь останется без изменений
#
# # res ={**data, **new_data}
# # print(data)
# # print(new_data)
# # print(res)
#
# res = data | new_data
# print(data)
# print(new_data)
# print(res)

# print(sum([1, 2, 5, 3], 2))
# print(max())
# print(min())

# numbers = [(i + 2) ** 3 for i in range(10)]
# print(numbers)
#
# numbers = [int(input('enter number:')) for i in range(3)]
# print(numbers)

# data = {f'{i}': i ** 2 for i in range(1, 100, 2)}
# print(data)
#
# data = (i for i in range(10))
# print(data)
#
# data = [i for i in range(10)]
# print(data)

from collections import *


def nametuplle(param):
    pass

# user = namedtuple('user', ('name', 'age', 'email'))
# vasya = user(name='vasy', age=28, email='vas@gmai.com')
# print(vasya)
# print(vasya.age)

# numbers = ('hello', 'python', 'python', 'world')
# c = Counter(numbers)
# print(c)

# c1 = Counter('hello python')
# c2 = Counter('hello world')
# # print(c1.most_common())
# # print(c1.most_common(n=4))
# # print(c2)
# # print(list(c2.elements()))
# # print(c1.total())
# print(c1)
# print(c2)
# c1.subtract(c2)
# print(c1)
# print(c1 - c2)

# data = defaultdict(list)
# print(data['name'])
# print(data)
# data['languges'].append('ru')
#
# data = defaultdict(int)
# data['languges'] += 1
# print(data)

# data = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4
# }
# data2 = {
#     'b': 5,
#     'e': 6
# }
# chain = ChainMap(data, data2)
# print(chain['b'])
# print(chain['e'])
# chain['e'] = 8
# print(chain)
# chain.parents['g'] = 9
# print(chain)









