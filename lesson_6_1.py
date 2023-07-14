def func_to_binaty(n):
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

num = 12
binary = func_to_binaty(num)
print(binary)


def func_decimal(binary):
    decimal = 0
