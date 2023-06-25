#Пользователь вводит три чиста. сказать
#сколько из них положительных и сколько отрицательных

number1 = int(input('enter number 1: '))
number2 = int(input('enter number 2: '))
number3 = int(input('enter number 3: '))
print((number1 > 0) + (number2 > 0) + (number3 > 0), end='положительные, остальные отрицательные')

