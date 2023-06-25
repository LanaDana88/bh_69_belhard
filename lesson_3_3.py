# пользователь вводит
# имя
#возраст
#город
#приветственное сообщение тремя способами

name = 'Ekaterina'
age = 13
city = 'Dubai'
text1 = 'Hello %s my litlle %s  your %d is the best time in %s' % (name, name, age, city)
text2 = f"Hello {name} my litlle {name} your {age} is the best time in {city}"
text3 = 'Hello {} my litlle {} your {} is the best time in {}'. format(name, name, age, city)
print(text1)
print(text2)
print(text3)