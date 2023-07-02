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

sum = 0
for i in range(1, 51, 2):
    sum += i
print(sum)

for i in range(1,11):
    print(7, 'x', i, '=', 7 * i)


