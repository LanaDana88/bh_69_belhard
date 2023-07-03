n = int(input('enter n:'))
for i in range(2, n+2, 1):
    if i % 2 == 0:
        print(i, end=' ')
        if i % 5 == 0:
            print()
