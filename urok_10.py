# rabota s failami

# для открытия файла функция open
# абсолютный путь (с диска)
# относительный путь, относительно исполняемого файла (в корне проекта)
# т.е. относительно корня проекта "input.txt" или './' из текущей папки

# file = open('input.txt') # относительный путь

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent # возвращает экземпляр класса, parent отсекает по 1-му родителю
print(BASE_DIR)

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
# # print(file.read()) #весь файл выгружаем
# # print(file.readline()) # итератор чтение по строкам
# # print(file.readlines()) #весь файл за раз, но в список строк
#
# for line in file:
#     print(file)
#
# lines = [line.strip() for line in file if line.strip]
# print(lines)
#
# file.close()

# открываем так
# режимы r - чтение, r+ - чтение и запись
# w - запись, но если файла нет, то он создается и откр на запись,
# если есть то пересоздается   w+ - запись чтение
# a - если файл есть, то дозаписываем новую информацию. в конец
# x - на создание, не удобен нужен try   exept

with (
    open(BASE_DIR / 'input.txt', 'r', encoding='utf-8') as file,
    open('output.txt', 'w', encoding='utf-8' ) as file2
):
    print(file.read())
print(file.closed)







