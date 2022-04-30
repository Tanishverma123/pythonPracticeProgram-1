def add_multiply(x, y):
    sum = x + y
    mul = x * y

    return sum, mul  # return as tuple


s, m = add_multiply(10, 20)
print("sum:", s)
print("mul:", m)

####################################################


def add_multiply(x, y):
    sum = x + y
    mul = x * y
    sub = y - x

    return [sum, mul , sub]  # return as list


s, m, sub = add_multiply(10, 20)
print("sum:", s)
print("mul:", m)
print("sub:", sub)
