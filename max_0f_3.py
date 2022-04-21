"""
a = int(input("Enter First Number:\n"))
b = int(input("Enter Second Number:\n"))
c = int(input("Enter Third Number:\n"))

print(" Largest Number:",end=" ")

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c) 
else:
    if b >= c:
        print(b)
    else:
        print(c)
"""


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a==b==c:
    print("all value are equal")
    
if a==b and b<c:
    print ("a and b is equal and c is greater than a and b ")

if b==c and b<a:
    print ("c and b is equal and a is greater than c and b ")

if a==c and c<b:
    print ("a and c is equal and b is greater than a and c ")
    
elif a >= b and a >= c:
    print(a ,"is Larger than ",b ," and ",c) 

elif b >= a and b >= c:
    print("Largest number is:", b) 

elif c >= a and c >= b:
    print("Largest  number is:", c)


    
