#TODO дан список чисел, необходимо его развернуть без использования
# метода reverse и фукции reversed, а также дополнительно списка и среза


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in range(len(numbers) // 2):
    numbers[number], numbers[~number] = numbers[~number], numbers[number]

print(numbers)