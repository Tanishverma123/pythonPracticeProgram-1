n = int(input('enter the number of stairs : '))
num1=0;
num2=1;
if (n==0):
    print('0')
else:
    for i in range(n):
        num3=num1+num2
        num1=num2
        num2=num3
        i=i+1
    print(num3)