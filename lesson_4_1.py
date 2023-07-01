number = [ ]
n = 2
list_number = [2 ** number for number in range(1, n+1)]

print(list_number)

# не совсем верно сделано выше

nambers = [ ]
n = int(input('введите число n:'))
list_numbers = [numbers ** 2 for numbers in range(1, n ^ 2)]
print(list_numbers) # новое решение
