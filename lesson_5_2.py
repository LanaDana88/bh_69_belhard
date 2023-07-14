# num1 = int(input('enter number: '))
# znacenie = 'Ваше число отрицательне или равно 0' if num1 <= 0 else int(input('enter number: '))
#
#
# print(znacenie)

num1 = int(input('enter number: '))
znak = input('enter operator: ')
num2 = int(input('enter number: '))
if znak == '+':
    print(num1 + num2)
elif znak == '/':
    print(num1 - num2)
elif znak == '*':
    print(num1 * num2)
else: print(num1 - num2)


