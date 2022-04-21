num1 = int(input("please enter a number :"))
count=1
while (True):
    print("guess the number ")
    num2=int(input())
    if(num2==num1):
        print("you choose correct in ",count ," chances ")
        break;
    elif(num2<num1):
        count=count+1;
        print("please enter greater one\n")
    elif(num2>num1):
        count=count+1;
        print("please enter smaller one\n")