# Пользователь вводит предложене, заменить все пробелы на "_"
# 2-мя способами

text = input('Введите Ваше предложение:')
words = text.split()
print(*words, sep='_')

text = input('enter the sentence:')
words = text.split()
print('_', join([words]))