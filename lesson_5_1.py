# n = int(input('enter number: '))
# m = int(input('enter number: '))
# k = int(input('enter number: '))
#
# while n < k:
#     n += 1
#     if n % m == 0:
#         print(n)


n = int(input('enter number: '))
m = int(input('enter number: '))
k = int(input('enter number: '))

while n % m == 0 and n > k:
    n -= 1
print(n)

