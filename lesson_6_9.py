#TODO дан словарь словарей, ключ внешнего словаря - id  пользователя,
# значение - словарь с данными о пользователе (имя, фамилия, телефон, почта),
# вывести имена тех, у ког не указана почта (нет ключа email
# или значение этого ключа - пустая строка)
#
#
# users_data = {
#     1: {
#         'first_name': 'Lana',
#         'last_name': 'Dana',
#         'phone': '77-888-77',
#         'email': ''
#     },
#     2: {
#         'first_name': 'Dana',
#         'last_name': 'Kama',
#         'phone': '88-777-88',
#         'email': 'jane.smith@example.com'
#     },
#     3: {
#         'first_name': 'Kama',
#         'last_name': 'Lana',
#         'phone': '77-777-77',
#         'email': None
#     }
# }
#
# for user_id, user_data in users_data.items():
#     email = user_data.get('email')
#     if email is None:
#         print(f'пользователь с именем {user_data["first_name"]} и id_{user_id} не заполнил почту')
#     if email == '':
#         print(f'пользователь с именем {user_data["first_name"]} и id_{user_id} не заполнил почту')

def pocta_none_ili_pusto():
    ne_zapolnili = []
    for user_id, user_data in users_data.items():
        email = user_data.get('email')
        if email == '' or email is None:
            ne_zapolnili.append(f'пользователь с именем {user_data["first_name"]} c id_{user_id} не заполнил почту')
    return ne_zapolnili

users_data = {
    1: {
        'first_name': 'Lana',
        'last_name': 'Dana',
        'phone': '77-888-77',
        'email': ''
    },
    2: {
        'first_name': 'Dana',
        'last_name': 'Kama',
        'phone': '88-777-88',
        'email': 'jane.smith@example.com'
    },
    3: {
        'first_name': 'Kama',
        'last_name': 'Lana',
        'phone': '77-777-77',
        'email': None
    }
}

print(pocta_none_ili_pusto())


