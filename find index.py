a=input("enter a string : ")
strfind=input("enter what u want to find : ")
l=len(a)
print("the length of our string is "+str(l))
'''
for i in range(l):
    if a[i]==strfind:
        print(a[i],": is at index :",i)
else:
    print("it is not present in string")
'''

for i in a:
    print(a.index(i))
