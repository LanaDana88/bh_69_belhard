# rabota s failami

# для открытия файла функция open
# абсолютный путь (с диска)
# относительный путь, относительно исполняемого файла (в корне проекта)
# т.е. относительно корня проекта "input.txt" или './' из текущей папки

# file = open('input.txt') # относительный путь

from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent # возвращает экземпляр класса, parent отсекает по 1-му родителю
# print(BASE_DIR)

# file = open(BASE_DIR / 'input.txt') # в идеале заводить баз.дир и делить на относительный путь
#
# # mod - режим открытия файла, после работы нужно обязательно закрыть close()
#
# # file = open(BASE_DIR / 'input.txt', 'r') # chtenie
# # file = open(BASE_DIR / 'input.txt', 'buffering') # buferizaciua linenaya po umolch (не выгр. весь файл в оперативку), считывает построчно
# # file = open(BASE_DIR / 'input.txt', 'r', encoding = 'utf-8') # кодировка
# # print(file.closed)
# # print(file.readable()) #для чтения
# # print(file.writable()) # для записи
# # print(type(file))
#
# # pro chtenie
# # print(file.read()) #весь файл выгружаем для чтения
# # print(file.readline()) # итератор чтение по строкам
# # print(file.readlines()) #весь файл за раз, но в список строк
#
# for line in file:
#     print(line)
#
# lines = [line.strip() for line in file] #с пустыми строками
# print(lines)
# # #
# lines = [line.strip() for line in file if line.strip()] #без пустых строк
# print(lines)
#
# file.close()

# открываем так

BASE_DIR = Path(__file__).resolve().parent # возвращает экземпляр класса, parent отсекает по 1-му родителю
print(BASE_DIR)

# режимы r - чтение, r+ - чтение и запись
# w - запись, но если файла нет, то он создается и откр на запись,
# если есть то пересоздается   w+ - запись чтение
# a - если файл есть, то дозаписываем новую информацию. в конец
# x - на создание, не удобен нужен try   exept

# with (
#     open(BASE_DIR / 'input.txt', 'r', encoding='utf-8') as file,
#     open('output.txt', 'w', encoding='utf-8') as file2
# ):
#     print(file.read())
#
# print(file.closed)

# например напишем файл 10 строчек с разрывом в  hello \n
# \n - разрыв строки

# with open('output.txt', 'w', encoding='utf-8') as file:
#     from time import sleep
#     for _ in range(10):
#         file.write('hello\n')
#         file.flush()
#         sleep(3)

# TODO дан текстовый многострочный файл, в каждой строке написаны числа через пробел
# необходимо найти сумму чисел в каждой строки и результаты записать в новый файл
#

with (
    open(BASE_DIR / 'input.txt', 'r', encoding='utf-8') as input_file,
    open(BASE_DIR / 'output.txt', 'w', encoding='utf-8') as output_file
 ):
    output_file.writelines(
            f'{sum(int(number) for number in line.strip().split())}\n'
            for line in input_file if line.strip()
    )

# result = []
# for line in input_file:
#     line = line.strip().split()
#     line = [int(i) for i in line]
#     result.append(f'{sum(line)}\n')
# output_file.writelines(result)
#
#
# with open('output.txt', 'w', encoding='utf-8') as file:
#       line = '*' * 7 + '\n'
#       while True:
#          file.write(line)
#             break
#
# with open('output.txt', 'w', encoding='utf-8') as file:
      #File.wriete('') # почистить файл, удалить все, т.е перезаписали








