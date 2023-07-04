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

#ЗАДАЧА 4
#Дан список содержащий словари,
# в каждом словаре может быть
# или не быть ключ price.
# Значение ключа, при его наличии,
# является число (int, float).
# Необходимо рассчитать среднее значение price
# среди словарей у которых есть данный ключ.






