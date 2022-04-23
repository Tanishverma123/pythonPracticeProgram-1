n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
    
#######################################
    
    
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

########################################

n=int(input())
for i in range(n):
    for j in range(0,n-i):
        print("*",end=" ")
    print()

########################################

n=int(input())
for i in range(n):
    for j in range(n-i):
        print(' ',end="")
    for k in range(i*2+1):
        print("*",end="")
    print()