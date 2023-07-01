# n= 1
# my_dict = {}
# for items in my_dict:
#     my_dict[items] = my_dict.get([i for i in range(1, n+1)])
#     print(my_dict)



n = int(input('введите число n: '))
slovar = {i: i for i in range(n+1)}
inner_slovar = {
    'name': input('enter name: '),
    'email': input('enter email: ')
}
slovar['inner_slovar'] = inner_slovar
print(slovar)