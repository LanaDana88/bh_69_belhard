# TODO Написать класс ConfigParser, конструктор класса принимает строку в формате:
text = '''
[Section1]
key1=value1
key2=value2
[Section2]
key3=value3
key4=value4
'''
# TODO написать метод класса parse, который будет вызываться в конструкторе, данный метод
#  принимает данную строку и преобразовывает в словарь словарей
#  результат метода после вызова в конструкторе, помещается в атрибут объекта data
data = {
    'Section1': {
        'key1': 'value1',
        'key2': 'value2',
    },
    'Section2': {
        'key3': 'value3',
        'key4': 'value4'
    }
}

# TODO
#  1. объявить метод has_section принимающий название секции и возвращающий
#  True - если такая секция есть, в противном случае False
#  2. объявить метод has_param принимающий название секции и название параметра
#  True - если есть указанный параметр в указанной секции иначе False
#  3. объявить метод add_section принимающий название новой секции и объявляющий ее
#  в случае отсутствия, если такая секция уже есть, вызвать исключение ValueError
#  4. объявить метод add_param принимающий название секции, название параметра и значение
#  если нет указанной секции - ValueError
#  если в секции нет указанного параметра - объявить параметр с указанным значением
#  если в секции есть указанный параметр - заменить его значение на новое
#  5. объявить метод del_section - принимающий название секции и удаляющий ее, если секции
#  нет, ничего происходить не должно
#  6. объявить метод del_param - принимающий название секции и название параметра
#  если данной секции нет - ValueError
#  если параметра в секции нет - ничего не происходит
#  если параметр в секции есть - удалить его
#  7. объявить метод dumps превращающий словарь в строку согласно формату
#  и возвращающий данную строку

class ConfigParser:

    def __init__(self, text: str) -> None:
        self.data = self.loads(text)

    @classmethod
    def loads(cls, text: str) -> dict[str, dict[str, str]]:
        lines = [line for line in text.split('\n') if line]
        data = {}
        current_section = ''
        for line in lines:
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                data[current_section] = {}
            else:
                key, value = line.split('=')
                data[current_section][key] = value
        return data

    def has_section(self, section: str) -> bool:
        return section in self.data

    def has_param(self, section: str, param: str) -> bool:
        try:
            return param in self.data[section]
        except KeyError:
            raise ValueError

    def add_section(self, section: str) -> None:
        if self.has_section(section):
            raise ValueError
        self.data[section] = {}

    def del_section(self, section: str):
        if section in self.data:
            del self.data[section]

    def del_paramm(self, section: str, param: str):
        if param in self.data:
            del self.data[{"param"}]
        else:
            raise ValueError

    def dumps(self):
        for key, value in dict.items():
            stroka += f"{key}:{value}"
        return stroka









































































































