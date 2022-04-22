n = int(input('enter the number which you want to check prime or not : '))
if (n==0):
    print('0')
else:
    for i in range(1,n+1):
        if(n%i==0):
            print(i,end=" ")
            
#####################################

n = int(input("Enter n:\n"))
x = 1
while x*x<n:

    if n%x ==0:
        print(x)
        print(n//x)

    x=x+1

    if x*x == n:
        print(x)