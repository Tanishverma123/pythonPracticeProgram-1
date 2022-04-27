n = int(input("enter number in decimal : "))
res = ""
while n>0:
    res = res+str(n%2)
    n=n//2
ans = res[::-1]
print("In binary : ",ans)

######################################################

def decToBin(n):
    res = bin(n)

    return res[2:]


for i in range(1, 15):
    print(i, decToBin(i))
    
#######################################################

def decToBinary(n):
    if n == 0:
        return "0"

    res = ''
    while n > 0:
        res = res + str(n % 2)
        n = n // 2

    return res[::-1]
    
for i in range(1,16):
    print(i,decToBinary(i))