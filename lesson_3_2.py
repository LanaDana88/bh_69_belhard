# Полльзователь вводит 3 числа, найти среднее
# рифметическое с точностью 3

number = input('введите трехзначное число:')
average = int(number[0]) + int(number[1]) + int(number[2]) / len(number)
print(round(average, 3))
