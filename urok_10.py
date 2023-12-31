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

# работа с типами файлов
#табличные файлы  - csv

from csv import reader, DictReader, writer, DictWriter

with open('input.csv', 'r', encoding='utf-8') as csv_file:
   r = reader(csv_file)
   for line in r:
       print(line)

with open('input.csv', 'r', encoding='utf-8') as csv_file:
   r = DictReader(csv_file) # если имена полей не указать, то в кач-ве имен полей значение строки 1
   for line in r:
       print(line) # получаем словарь - ключ значение

# with open('input.csv', 'r', encoding='utf-8') as csv_file:
#    r = DictReader(csv_file, filednames=('name', 'email', 'age'), delimiter=';')
#    for line in r:
#        print(line) # для сит. когда, нет первой строки и разделитель ';'

##ДЛЯ ЗАПИСИ

#создаем список строк

line = [
    ['vasya', 'vasya@gmail.com', 23],
    ['petua', 'petua@gmail.com', 35]
]
# writerows() принимает список списков, строк и записывает
# каждый список джойнит по разделителю, строчку по \n  и все отправляет в файл
with open('output.csv', 'w', encoding='utf-8') as csv_file:
    w = writer(csv_file)
    w.writerows(line) #принимает список строк и записывает

# есть DictWriter - нужен список словарей

line = [
    {'name': 'vasya', 'email': 'vasya@gmail.com', 'age': 23},
    {'name': 'petua', 'email': 'petua@gmail.com', 'age': 35}
]

with open('output1.csv', 'w', encoding='utf-8') as csv_file:
    w = DictWriter(csv_file, fieldnames=('name', 'email', 'age')) #filednames - обязателен
    w.writeheader()     # 3 метода - writerow принимает словарь
    w.writerows(line)           # writerows принимает список словарей
                                # writheader записывает ключи в первую строчку,
                                # как заголовки, если только создаем, то сначала
# writheader, а потом 2-а других метода

# 2-ой ТИП ФАЙЛОВ ЭТО JSON - спец. тип файлов на js написан
# фигурные скобки { }, ковычки только " ",
# ключи - только строки, значения - строки и числа, булеан с маленькой буквы  - boll - true ili false,
# null, вложенный словарь, список,
# после последней пары ключ - значение не ставят запятую - нарушене ситнтаксиса

from json import load, loads, dump, dumps

# у json 4-ре основных функции: load, loads, dump, dumps
# load - при работе с json в виде файла
# loads - при работе с json в виде строки
# dump - при работе с json в виде файла
# dumps - при работе с json в виде строки

with open('input.json', 'r', encoding='utf-8') as file:
    # data = load(file)
    # print(data) # получаем полноценный словарь

    data = loads(file.read()) # читаем строку
    print(data)

    print(file.read()) # просто прочитается файл json

# ПРО ЗАПИСЬ : 2  способа
# dump - записываем в файл
# dumps - записываем в строку

# Серелизация - превращение объекта в поток байт (улсловно записываем в файл)
#
# Десерилизация - процесс считывая из json файла в словарь (представление потока байт в объект)
#

data = {
    'name': 'Lena',
    'city': 'Dubai',
    'regim': 'сон'
}

data1 = {
    'name': 'Lena',
    'city': 'Dubai',
    'regim': 'сон'
}
with open('output.json', 'w', encoding='utf-8') as file:
    dump(data, file) # запишет в одну строку, для форматирвание исп. атрибут  indent
    dump(data, file, indent=2)
    dump(data, file, indent=2, ensure_ascii=False)

with open('output1.json', 'w', encoding='utf-8') as file:
    text = dumps(data1, indent=2, ensure_ascii=False)
print(text) # это и будет json file в виде строки

# json не поддерживает объекты даты,
# они передаются в виде строки согласно какому-то  формату - iso
# или
# они передаются виде timestemp (кол-во секунд с 01.01.1970)- число либо целое либо дробное

# русские буквы - юникод добавляем enshure_aschi=False
# dumps - файл не принимается, возвращается, т.е. его можно куда-то записать

from configparser import ConfigParser


with open('config.ini', 'r', encoding='utf-8') as file:
    parser = ConfigParser()
    parser.read_file(file)
    print(parser)

# работа с библиотекой pydantic - по валидации, сериализации, десиарилизации

# cтруктура данных описывается с пом. моделей, а модель это класс
# при этом класс похож на dataclass - класс сугубо для хранения данных

from pydantic import BaseModel
#from pydantic.v1 import BaseModel

# каждая модель наследуется от базовой модели или от другого
# дочернего класса или от другой базовой модели
# модель пользователя

class User(BaseModel): # объявляем атрибуты класса с аннотацией типов, обязательно с аннотацией типов
    name: str
    email: str
    age: int # или age: int | float
# данные передаваемые будут проверяться на указанный тип данных

vasya = User(
    name = "Vasya",
    email = "vas@gmail.com",
    age = "25"
)
print(vasya)

from pydantic import EmailStr, field_validator, model_validator

from typing import Optional, Literal, List



class User(BaseModel):
    name: str
    email: EmailStr  # проверка на то, что почта - это почта
    age: int

Lana = User(
    name = "Lana",
    email = "Lana@gmail.com",
    age = "15"
)
print(Lana)

# указание необязательного атрибута

from typing import Optional
# class SomeModel(BaseModel):
#     key: str | None # 1 вариант
#     key2: str = None # 2 вариант
#     key3: Optional[str] # 3 вариант исп. модуль from typing import Optional
#     key4: str = Field(defoult=None)
#     key5: str = Field(...)

# class Product(BaseModel):
#     name: str
#     price: Decimal = field(max_dagits=8, decimal_places=2)
#
# class Category(BaseModel):
#     name: str
#     products: List[Product]
#     parent: Optional["Category"]


class Shema(BaseModel):
    key1: str
    key2: str
    key3: Literal['value1', 'value2']

    @field_validator('key1')
    def key1_validator(cls, value: str):
        return value

    @model_validator(mode='after')
    def valdator(cls, values: dict):
        return values

from pydantic import validate_call

# нужна для (декоратор) для валидации аргументов функции

# def is_palindrome(text: str) -> bool:
#     return text.lower() == text.lower()[::-1]

# можно повесить декоратор и ему не нужно ничего передавать
@validate_call()
def is_palindrome(text: str) -> bool:
    return text.lower() == text.lower()[::-1]

print(is_palindrome('jasfgvsdjvb'))
print(is_palindrome("152477"))



db = ('vasya@gmail.com', 'petya@gmail.com')

class Person(BaseModel): #проверка  на уникальность емайла в базе данных
    email: EmailStr

    @field_validator('email')
    def email_validator(cls, email: str):
        if email in db:
            raise ValueError('email is not unique')
        return email


user = Person(email='qwer@gmail.com')
try:
    user2 = Person(email='vasya@gmail.com')
except ValueError as e:
    print(e.errors())
    print(e.json())


