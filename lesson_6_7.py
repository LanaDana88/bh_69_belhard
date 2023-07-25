#TODO дан список чисел, необходимо для каждго элемента посчитать его сумму
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка


def summ_sosedei(numbers):
    summa = []

    for number in range(0, len(numbers) - 1):
        summ_sosedei = numbers[number - 1] + numbers[number + 1]
        summa.append(summ_sosedei)
    return summa

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

res = summ_sosedei(numbers)

print(res)

