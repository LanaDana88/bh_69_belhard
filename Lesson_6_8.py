#TODO дан словарь, ключ - Название страны, значение - список городов, на вход поступает город,
# необходимо сказать из какой страны он


# search_city = input('enter city:  ')
#
# cities_dict = {
#     'Russia': ['Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg'],
#     'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
#     'China': ['Beijing', 'Shanghai', 'Guangzhou', 'Chongqing'],
#     'Germany': ['Berlin', 'Hamburg', 'Munich', 'Cologne']
# }
# found = False
# for country, cities in cities_dict.items():
#     if search_city in cities:
#         print(f'{search_city} in {country}')
#         found = True
#         break
# else:
#     print(f'None {search_city} in dict')

def poisk():
    for country, cities in cities_dict.items():
        if search_city in cities:
            return f'{search_city} in {country}'

    return f'None {search_city} in dict'

search_city = input('enter city:  ')
cities_dict = {
    'Russia': ['Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'China': ['Beijing', 'Shanghai', 'Guangzhou', 'Chongqing'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Cologne']
}
itog = poisk()
print(itog)