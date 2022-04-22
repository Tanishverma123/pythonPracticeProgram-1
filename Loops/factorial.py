n = int(input("Enter any number : "))
fact = 1
m = n
while n != 1:
    fact = fact * n
    n = n - 1

print("The factorial of",m, "number is", fact)



###################################


n = int(input("Enter n:\n"))

res = 1

for i in range(2,n+1):
    res = res*i
    
print("factorial is :",res)


####################################

import math
n = int(input("Enter first number : "))
favt = math.factorial(n)

print(fact)
