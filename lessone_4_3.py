n= 1
my_dict = {}
for items in my_dict:
    my_dict[items] = my_dict.get([i for i in range(1, n+1)])
    print(my_dict)