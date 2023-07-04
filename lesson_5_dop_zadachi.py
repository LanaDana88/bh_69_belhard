# ЗАДАЧА 1
# Вводится число необходимо посчитать факториал


# num = int(input('enter number: '))
# factorial = 1
# while factorial >= 1:
#     factorial *= num
#     num -= 1
# print(factorial)

#
# num = int(input('enter number: '))
# pr = 1
# for i in range(1, num+1):
#     if num >= 1:
#         pr *= num
#         num -= 1
# print(pr)

# ЗАДАЧА 2
# Вводится число необходимо вывести N чисел Фибоначи

# num = int(input('enter number: '))
# fib_num = [0, 1]
#
# for i in range(2, num + 1):
#     if i <= num:
#         fib = fib_num[i-1] + fib_num[i-2]
#     fib_num.append(fib)
# print(fib_num)

# ЗАДАЧА 3
# Вводится число необходимо является ли оно простым

# num = int(input('enter number: '))
# category = 'Простое число' if num > 1  else ('число  простое' if num / num == 1 else "числоне простое")
# print(category)
# prostoe_chislo = True
# if num <= 1:
#     prostoe_chislo = False
# else:
#     for num in range(2, num +1):
#         if num % 2 == 0:
#             prostoe_chislo = False
#             break
# print('Ваше число', prostoe_chislo)


# if num <= 1:
#     num = False
# elif num % 2 == 0:
#     num = False
# else:
#     num = True
# print('Ваше число', num)

# ЗАДАЧА 5
# У пользователя спрашивают число (вводим с клавиатуры)
# но пользователь может ввестине число, вводит пока не введет число

# num = input('enter number:_')
#
# while num.isalpha():
#     num = False
#     num = input('enter new num: ')
# else:
#     num = True
# print('Вы ввели число', num)
#
#
# num = input('enter number:_')
# - проверяет только текст без символов

# num = input('enter number:_')
# while num in '+-*/()':
#     num = False
#     num = input('enter num new: ')
#     while num.isalpha():
#         num = input('enter new num: ')
# else:
#     num = True
# print('Вы ввели число', num)
# провряет на буквы или символы и символы

#ЗАДАЧА 6
#Дан список словарей, каждый словарь имеет ключи:
# category_id, title, price. Значение ключа category_id
# является целое положительное число,
# значением ключа name - str,
# а значение ключа price - float.
# Те словари, у которых ключ category_id = 1,
# необходимо удалить, а те у которых category_id = 2,
# необходимо уменьшить price на 5%.
# Остальные словари оставляем без изменений.

# list_slovarei = [
#     {'category_id': '1', 'name': 'coffe', 'price': '8.25'},
#     {'category_id': '2', 'name': 'tee', 'price': '5.25'},
#     {'category_id': '3', 'name': 'jus', 'price': '3.25'},
#     {'category_id': '4', 'name': 'water', 'price': '1.25'},
#     {'category_id': '5', 'name': 'coffe arabica', 'price': '18.77'},
#     {'category_id': '6', 'name': 'milk', 'price': '2.25'},
#     {'category_id': '7', 'name': 'fresh', 'price': '4.87'},
#     {'category_id': '2', 'name': 'soda', 'price': '1.77'},
#     {'category_id': '1', 'name': 'cola', 'price': '3.89'}
# ]
# first = list_slovarei[0]
# category_id = first['category_id']
# name = first['name']
# price = first['price']
# # second = list_slovarei[1]
# # thed = list_slovarei[2]
# # name = thed['name']
# print('ID категории товара: ', category_id, 'Название товара:', name, 'Цена товара: ', price)
#
# new_list_slovarei = []
# for item in list_slovarei:
#     if item['category_id'] != '1':
#      new_list_slovarei.append(item)
# print(new_list_slovarei)
#
# for item in list_slovarei:
#     if item['category_id'] == '2':
#         item['price'] = str(float(item['price']) * 1.05)
#         new_list_slovarei.append(item)
# print(new_list_slovarei)



#ЗАДАЧА 4
#Дан список содержащий словари,
# в каждом словаре может быть
# или не быть ключ price.
# Значение ключа, при его наличии,
# является число (int, float).
# Необходимо рассчитать среднее значение price
# среди словарей у которых есть данный ключ.


list_slovarei = [
    {'category_id': '1', 'name': 'coffe', 'price': '0'},
    {'category_id': '2', 'name': 'tee', 'price': '5.25'},
    {'category_id': '3', 'name': 'jus', 'price': '3.25'},
    {'category_id': '4', 'name': 'water', 'price': '0'},
    {'category_id': '5', 'name': 'coffe arabica', 'price': '18.77'},
    {'category_id': '6', 'name': 'milk', 'price': '2.25'},
    {'category_id': '7', 'name': 'fresh', 'price': '4.87'},
    {'category_id': '2', 'name': 'soda', 'price': '1.77'},
    {'category_id': '1', 'name': 'cola', 'price': '3.89'}
]

new_slovar = []
sr_prise = 0
count = 0
for item in list_slovarei:
    if item['price'] != '0':
        sr_prise += float(item['price'])
        count += 1
        new_slovar.append(item)
sr_prise /= count
print(sr_prise)



