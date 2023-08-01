#TODO дан список рандомных чисел, необходимо отсортировать его в виде,
# сначала четные потом не четные


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cetnii = []
necetnii = []
for number in numbers:
    if number % 2:
        necetnii.append(number)
    else:
        cetnii.append(number)

itog = cetnii + necetnii
print(itog)

def cet_necet_func(nubers):
    cetnii = []
    necetnii = []
    for number in numbers:
        if number % 2:
            necetnii.append(number)
        else:
            cetnii.append(number)


    return (cetnii + necetnii)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
itog = cet_necet_func(numbers)
print(itog)
