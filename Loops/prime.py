n = int(input('enter the number which you want to check prime or not : '))
if (n==0):
    print('No')
else:
    for i in range(2,(n//2)+2):
        if(n%i==0):
            print("No")
            break
    else:
        print("Yes")