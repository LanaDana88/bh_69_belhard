# print ('Alena')
# print ('Hello Helena')
# a = 2
# b = 3
# c = a * b
# prrint(c)
#
# first_name = 'Helen'
# last_name = 'Kama'
# age = 28
# leave = 'Borisov'
# print(first_name, last_name, age, leave, sep='_', end=' И все!!!')

# first_name = input('Введите Ваше имя:')
# last_name = input ('Введите Вашу фамилию:')
# print(first_name, last_name, sep='  ', end=' Вы точно ввели Ваше Имя и Фамилию')

# first_name = input('Введите Ваше имя:')
# last_name = input ('Введите Вашу фамилию:')
# full_name = (first_name + last_name)
# print(full_name, sep='  ', end=' Вы точно ввели Ваше Имя и Фамилию')
# print(first_name * 3, sep='_')

# name = 'Alene'
# age = 17
# # 'Я %s. Мне d%d.' % (name, age)
#
# f"Меня зовут {name}. Мне {age} лет."

# name = 'Lena'
# age = 28
# text = f"Меня зовут {name}. Мне {age} лет."
# print(text)

age = 15
name ='Katya'
is_human = True
#text = f"Hello {name}, are you {age}?"
# text = 'Hello your name is human'
text1 = 'Hello ' + name + ' your age ' + str(age) + ' is_human ' + str(is_human)
text2 = 'Hello %s your age %d is human %d' % (name, age, is_human)
text3 = f"Hello { name * 3 } your age {age} is human {is_human}"
text4 = 'Hello {} your age {} is human {}'. format(name, age, is_human)
print(text1)
print(text2)
print(text3)
print(text4)

# print(f'{age:_>10}')

# print(f'{name=}')
# print(f'{17 * 18 = }')
# print(f'{name!r}')
# print(f'{name!a}')

# print(f'{3.1459:.7f}')

# print('могу вставить спец символы')

# text = 'Hello word Python'
# print(text.split())
#
# text = 'Hello___word___Python'
# print(text.split('___', 1))
# #
# text = 'Hello___word___Python'
# print(text.rsplit('___', 1))
# print(' | '.join(['hello', 'world']))

# text = 'Hello world python world'
# # print(text.find('world'))
# # print(text.find('world', 7))
# # print(text.rfind('world'))
# # print(text.index('world'))
# # print(text.rindex('world'))
# # print(text.count('world'))
# # print(text.partition('world'))
# # print(text.rpartition('world'))
#
# # print(text.replace(' ', '_'))
# print('Hello world'.startswith('Hell'))

# print('hello\tworld\tpython\tpuchara'.expandtabs(12))

# print('--=---=-=-=,=/hello/././world,/./-=-=-'.strip('-=,./'))
# print('--=---=-=-=,=/hello/././world,/./-=-=-'.lstrip('-=,./'))
# print('--=---=-=-=,=/hello/././world,/./-=-=-'.rstrip('-=,./'))

# print('hello'.center(13, '_'))
# print('hello'.ljust(13, '_'))
# print('hello'.rjust(13, '_'))

# print(bin(14).zfill(14))

# text = input('enter text:')
# first_space = text.find(' ')
# last_space = text.rfind(' ')
# first_world = text[:first_space]
# center = text[first_space: last_space + 1]
# last_world = text[last_space + 1:]
# text = last_world + center + first_world
# print(text)

# a = 400
# v = 400
# print(a is v)

# a = 'hel lo'
# v = 'hel lo'
# print(a is v)

# print(bin(13))
# print(bin(14))
# print(bin(13 & 14))
# print((13 | 14))
# print(bin(13 ^ 14))

# print(~-10)

# text = 'qwerty'

# text = input('enter world:')
# print(text == text[::-1])

# dad = int(input ('age:'))
# sun = int(input('age:'))
# print(dad - sun * 2)

# number = input('введите трехзнаяное число:')
# print(int(number[0]) + int(number[1]) + int(number[2]))

# x1 = int(input('x1:'))
# x2 = int(input('x2:'))
# y1 = int(input('y1:'))
# y1 = int(input('y1:'))
# wight = abs(x1) + abs(x2)
# height = abs(y1) + abs(y2)
# leght = (wight ** 2 + height ** 2) **0.5
# print(leght)

