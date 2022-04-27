def binToDec(b):
    res = 0

    p = 1
    for x in reversed(b):
        res = res + int(x) * p
        p = p * 2

    return res

############################################

def BinToDec(b):
    res = int(b, 2)

    return res


print(BinToDec('1100'))










