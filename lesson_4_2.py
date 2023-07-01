# list = [2, 5, 8, 9, 10, 15, 48, 25, 18, 0]
# my_list = {}
# for items in list:
#     my_list[items] = my_list.get(items, 0) + 1
#
#         print(my_list.items())

text = input('введите тескст:')
count = len(text.split())
print(count)

text = input('enter text:')
counts = {}
for char in text:
    char = char.lower()
    counts[char] = counts.get(char, 0) + 1
for letter, count in counts.items():
    print(f"буква '{letter}' встречается {count} раз'")