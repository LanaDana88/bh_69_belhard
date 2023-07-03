# age = int(input('enter your age: '))
# if age < 14:
#     print('Вы еще ребенок, потому что вам', age)
# elif age < 16 > 14:
#     print('Вы подросток, в возрате до', age)
# elif age < 18 > 16:
#     print('Вы, в возрасте до, когда что-то можно, а что-то нельзя,потому что вам', age)
# else:
#     print('Вы уже в том возрасте, что вам можно все!!!! Потому что вам', age)

# Тернарный оператор

# x = int(input('enter number: '))
# res = 'число больше 11' if x > 11 else 'число меньше или равно 11'
# print(res)

# x = int(input('enter number: '))
# res = 'Введенное число четное' if x % 2 == 0 else 'Введенное вами число нечетное'
# print(res)

# num1 = int(input('enter number 1: '))
# num2 = int(input('enter number 2: '))
# min_max = num1 if num1 > num2 else num2
# print("Миксимальное число из введенных Вами", min_max)

# age = int(input('enter yur age: '))
# category = "Ребенок" if age < 18 else "Взрослый"
# print(category)

# num = int(input('enter number: '))
# res = "Положительное" if num > 0 else ('Отрицательное' if num < 0 else "Нулевое")
# print(res)

# age = int(input('enter age:'))
# category = 'Дети' if age <=12 else ('Подростки' if age <= 19 else
#      ("Взрослые" if age <=59 else "Пожилые"))
# print(category)

# number = int(input('enter yur number: '))
# if number <= 10:
#     print("Введенное вами чило меньше 10 и равно ", number)
# elif number <= 20:
#     print("Введенное вами чило больше 10, но меньше 20 и равно ", number)
# elif number <= 30:
#     ("Введенное вами чило, больше 20, но  меньше 30 и равно ", number)
# else:
#     ("Введенное вами чило больше 30 и равно ", number)

# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not a)

# x = 5
# y = 10
# print(x == y)
# print(x > y)
# print(x <= y)
# print(x < y)
# print(x != y)

# num = int(input('enter number: '))
# if num % 2 == 0:
#     print("введенное число четное", num)
# else:
#     print('Введенное число не четное', num)

# x1 = int(input('enter number: '))
# x2 = int(input('enter number: '))
# if x1 != x2:
#     print('введенные значения не равны между собой')
# else:
#     print('введенные числа равны x1 = ', x1, 'x2 = ', x2)

# stydent_ball = float(input('enter ball studenta: '))
# if stydent_ball >= 60:
#     print('Студент успешно сдал предмет', stydent_ball, 'Вы молодец!!!!')
# else:
#     print('Студент не сдал предмет', stydent_ball, 'Вам на пересдачу. Будьте готовы!!!!')

# num1 = int(input('enter number1: '))
# num2 = int(input('enter number2: '))
# if num1 % 2 == 2 and num2 % 2 == 0:
#     print('числа четные')
# elif num1 != 0 or num2 != 0:
#     print('Числа  не нулевые')
# else:
#     print('числа отрицательные')

#ЦИКЛЫ

# fruktik = ('apple', 'banana', 'chery', 'orange')
# for frukt in fruktik:
#     print(frukt)
#
# world = input('enter world: ')
# glasnii_letter = 0
# for letter in world:
#     if letter.lower() in 'eyuoia':
#         glasnii_letter += 1
# print('kolichestvo glassnih bukv', glasnii_letter)

# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# print(sum)
#
# start = 20
# end = 30
# num = start
# while num <= 30:
#     if num % 7 == 0:
#         break
#     num += 1
# print(num)
#
# secret_number = 42
# guess = 0
# while guess != secret_number:
#     guess = int(input('enter secret number: '))
#     if guess == secret_number:
#         break
#
# print('Супер, молодец, ты угодал', secret_number)

# for i in range(1,10):
#     print(i)
#
# sum = 0
# num = 1
# for num in range(1,101):
#     sum += num
# print(sum)

# for i in range(2, 20, 2):
#     print(i)

# sum = 0
# for i in range(1, 51, 2):
#     sum += i
# print(sum)
#
# for i in range(1,11):
#     print(7, 'x', i, '=', 7 * i)

# for i in range(1,10):
#     print(i, end= ' ')

# for i in range(0, 20, 2):
#     print(i, end=" ")

# text = "Hello"
# for letter in text:
#     print(letter, end= "__")

# text = 'python'
# gl_let = 0
# for letter in text:
#     if letter in 'eyuoai':
#         gl_let += 1
# print(gl_let)

# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i, end=' ')
# n = int(input('enter number: '))
# for i in range(0, n+1):
#     if i % 3 == 0:
#         print(i, end=" ")

# sum = 0
# for i in range(1, 101, 2):
#      sum += i
# print(sum)

# sum = 0
# for i in range(1, 101, 2):
#     sum += i
# print(sum)

# for i in range(100, 0, -1):
#     print(i)

# num = int(input('enter number: '))
# prostoe_chislo = True
# if num <= 1:
#     prostoe_chislo = False
# else:
#     for i in range(2, num + 1):
#         if num % i == 0:
#             prostoe_chislo = False
#             break
# print(prostoe_chislo)



# num = int(input('Введите число: '))
# reversed_num = 0
#
# while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num = num // 10
#
# print(reversed_num)

#Zapis_zanyatiua

# a = 5
#
# if a > 0:
#     print('a is positive')

# a = -2
#
# if a > 0:
#     print('a is positive')
# elif a < 0:
#     print('a is negative')
# else:
#     print('a is null')


# a = 45
# if a % 2:
#     is_even = "No"
# else:
#     is_even = "Yes"
# print(is_even)
#
# a = 42
# is_even = 'No' if a % 2 else 'Yes'
# print(is_even)

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# x = input('enter num:' )
# x2 = 5
# print(isinstance(x, int))
# print(isinstance(x, (int, float)))
# print(isinstance(x2, int))

# без условный цикл FOR

# for i  in range(1, 10, 2): # 1 3 5 7 9
#     i **= 2
#     print(i, end=" ")

# text = 'hello' # для строки, список, кортеж, сета и фрозенсета
# for i in text:
#     print(i, end="  ")

# text = 'hello'
# for i in range(len(text)):
#     print((text[i]), end=" ")

# text = 'hello'
# for i in enumerate(text):
#     print(i)

# l = [
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9),
#     (10, 11, 12)
# ]
# for i in l:
#     print(i)
#
# l = [
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9),
#     (10, 11, 12)
# ]
# for i, j, k in l:
#     print(i, j, k)
#
# l = [
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9),
#     (10, 11, 12)
# ]
# for i, j, k in l:
#     print(f'{i=}', f'{j=}', f'{k=}')

# data = [
#     ('Cappuccino', 'Good', 5.50),
#     ('Latte', 'Bad', 6.20),
#     ('Mokko', 'Not so bad', 4.50),
# ]
# for name, descr, prise in data:
#     print(name, descr, prise)
#
# s = set('hello')
# for i in s:
#     print(i)

# data = {
#     'key1': 'value1',
#     'key2': "value2",
#     'key3': 'value3',
#     'key4': 'value4',
# }
# for key in data.keys():
#     print(key)
#
# data = {
#     'key1': 'value1',
#     'key2': "value2",
#     'key3': 'value3',
#     'key4': 'value4',
# }
# for key in data.values():
#     print(key)
# data = {
#     'key1': 'value1',
#     'key2': "value2",
#     'key3': 'value3',
#     'key4': 'value4',
# }
# for key in data.items():
#     print(key)
#
# data = {
#     'key1': 'value1',
#     'key2': "value2",
#     'key3': 'value3',
#     'key4': 'value4',
# }
# for key, val in data.items():
#     print(key, val)

# for i in range(10):
#     if i % 2:
#         continue
#     print(i)

# for i in range(10):
#     if i == 7:
#         break
#     print(i)

# for i in range(10):
#     if i == 7:
#         break
#     print(i)
# else:
#     print('FINISH!')
#
# for i in range(10):
#     if i == 10:
#         break
#     print(i)
# else:
#     print('FINISH!')








