def find_first(n):
    while(n>=10):
        if(n>10):
            n=n//10
    return n;
        
n = int(input("enter any number"))
print(find_first(n))


############################################3

from math import log10

def getFirstDigit(x):
    d = int(log10(x))
    res = x // (10 ** d)
    return res

x = int(input("Enter x:\n"))
print(getFirstDigit(x))