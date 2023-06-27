list = [2, 5, 8, 9, 10, 15, 48, 25, 18, 0]
my_list = {}
for items in list:
    my_list[items] = my_list.get(items, 0) + 1

        print(my_list.items())