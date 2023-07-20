# Klassi

# class ProductDetail

# class Person:
#    pass
#
# person1 = Person()
#
# print(type(person1))

# class Person:
#     role = 'user'
#
# person1 = Person()
# person1.role = 'admin' #изменить атрибут объекта, только через обращение через класс
# # Person.role = 'admin'  #изменить атрибут класса
# # person1.__class__role = 'admin' #возвращает ссылку на данный класс
# print(Person.role)
# print(person1.role)
#
# # объявление атрибутов объекта
# # необходимо объявить конструктор
# class Person:
#     role = 'user' # атрибут класса (чертежа)
#
#     def __init__(self, name, age): #конструктор дандрет метод инит
#         self.name = name
#         self.age = age
#
# person1 = Person(name='Lana', age='18') # атрибут объекта
# person2 = Person(name='Katya', age=25)
# print(person1.name)
# print(person2.name)

#Metodi - 3 vida
# 1 metod obekta
class Person:
    role = 'user' # атрибут класса (чертежа)

    def __init__(self, name, age): #конструктор дандрет метод инит
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

person1 = Person(name="Lane", age=22)
person2 = Person(name='Ketya', age=25)
person1.birthday()
# person1.birthday()
# person1.birthday()
# person1.birthday() #сколько раз вызываем, столько и прибавляет + 4 итог 22
print(person1.age)

# 2 metod klassa
class Person:
    role = 'user' # атрибут класса (чертежа)

    def __init__(self, name, age): #конструктор дандрет метод инит
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    @classmethod
    def from_list(cls, objs: list):
        return [cls(**obj) for obj in objs]

print(Person.from_list([{'name': 'Lana', 'age': 25 },
                        {'name': 'Roma', 'age': 28 } ]))

# 3 metod staticeski
class Person:
    role = 'user' # атрибут класса (чертежа)

    def __init__(self, name, age): #конструктор дандрет метод инит
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    @staticmethod
    def foo():
        print('foo')
def foo():
    print('foo')


#TODO написать класс Category
# # #  1. Объявить атрибут класса categories со значением пустой список
# # #  2. Написать метод класса add принимающий на вход название новой категории
# # #  если такая категория есть в атрибуте класса categories, то вызвать исключение
# # #  ValueError, в противном случае добавить новую категорию в атрибут класса categories
# # #  и вернуть индекс вхождения новой категории в список categories

class Category:
    categories = []

    @classmethod
    def add(cls, new_category):
         if new_category.title() in cls.categories:
             raise ValueError('new category is not unique')
         else:
             cls.categories.append(new_category.title())
             return len(cls.categories) - 1

# # # TODO написать метод класса get принимающий номер категории и возвращающий соответствующую
# # #  категорию из списка categories, если категории нет, вызывать исключение IndexError

@classmethod
def get(cls, pk):
    return cls.categories[pk]

# # # TODO написать метод класса remove принимающий номер категории и удаляющий соответствующую
# # #  категорию из списка categories, если категории нет, ничего не должно происходить

# TODO написать метод класса get принимающий номер категории и возвращающий соответствующую
# # #  категорию из списка categories, если категории нет, вызывать исключение IndexError
# @classmethod
# def remove(cls, pk):
#     try:
#         del cls.categories[pk]
#     except IndexError:
#         pass


# Magicheskie metodi
class User:
     def __init__(self, name):
        self.name = name

vasya = User(name='Vasya')
print(f'User: name={vasya.name}')

# 1 variant napisat metod info

class User:
    def __init__(self, name):
        self.name = name

    # def __str__(self):  # приведение к строке
    #     return f'User: name={self.name}'

    def __repr__(self):
        return f'User: name={self.name}'
# хочу найти длину
    def __len__(self):
        return len(self.name)
# getitem позволяет реализовать обращение к объекту по индексу или ключу
#     def __getitem__(self, item):
#         return self.name[item]
#
# # getitem изменять по  индексу или ключу
#     def __setitem__(self, key, value):
#         return self.name[item]

# возможность итерации по объекту с for реализуетсЯ 2 метода iter и next
    def __iter__(self): # описывает что будет возвращаться, когда передаем в iter
        return self
    # def __next__(self):# описывает что будет возвращаться когда буду обращаться к итератору с помощью функции next- внутри не д.б. никаких циклов
    #     self.i += 1
    #     try:
    #         return self.name
    #     except IndexError
    #         self.i = 1
    #         raise StopIteration



# vasya = User(name='Vasya')
# for i in vasya:
#     print(i)
# print(vasya)
# print(len(vasya)) # dlina
# print(vasya[2]) #обращение по индексу

# если есть Len_ то объект будет приводиться к bool На основании рез-та длинны
# длинна пустой строки

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.i = -1
        self.is_active = True
    def __repr__(self):
        return f'User: name={self.name}'
    def __len__(self):
        return len(self.name)

    def disable(self):
        self.is_active = False

    def __getitem__(self, item):
        return self.name[item]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disable()
# реализовать сложение, нужно 2-а метода add и radd
    def __add__(self, other): # левое сложение.ю реализуется один метод, а во втором происходит перевызов первого
        if isinstance(other, int):
            return self.age + other
        elif isinstance(other, User):
            return self.age + other.age
        else:
            raise ValueError

    def __radd__(self, other): #правое сложение
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.age += other
            return self


user1 = User(name='User1', age=12)
user2 = User(name='User2', age=52)
print(user1 + user2)
print(user1 + 23)
user1 += 12
print(user1.age)


#OOP
#Abstrakciya
#Nasledovanie -
#Polimarfizm

class User:

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.is_active = True

    def __repr__(self):
        return f'User name={self.name} email={self.email}'

    def __bool__(self):
        return self.is_active

# хочу описать класс манеджер? код весь не повторять, нарушаем dry
#наследуемся
class Manager(User):

    def foo(self):
        print('foo')

vasya = Manager("Vasysa", "vas@gmail.com")
print(vasya)
vasya.foo()

# множественное наследование от 2-х и более классов

class A:
    name = 'a'

class B:
    name = 'B'


class C(A, B):
   pass

print(C.name)

#Polimarfizm переопределение род. метода внутри дочерноего с целью расширения

class Manager(User):
    def __init__(self, name: str, email: str, salary: int):
        super().__init__(name, email)
        self.salary = salary


vasya = Manager("Vasysa", "vas@gmail.com")
print(vasya)
vasya.foo()







