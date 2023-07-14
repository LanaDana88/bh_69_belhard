def func(my_list, step):
    step = step % len(my_list)
    return(my_list)

n = int(input('enter number n: '))
my_list = [_ for _ in range (n)]
step = int(input('enter step: '))

print(func(my_list, step))


def func(my_list, i):
    new_my_list = my_list[i:] + my_list[:i]
    return(new_my_list)

i = int(input('enter number i: '))
my_list = list(range(i))
sdvig = int(input('enter number sdvig: '))

itog = func(my_list, sdvig)
print(itog)