mystr="rahul is a good boy"
print(mystr[4])
print(mystr[0:7])  #0-r,1-a,2-h,3-u,4-l,5-space,6-i
                   # yaha pr last index 7 h to bo print ni hoga
print(len(mystr))
print(mystr[0:len(mystr)])
#print(mystr[78])error
print(mystr[0:78])
print("1",mystr[0:8:2])
print("2",mystr[0:8:1])
print("3",mystr[0:8:3])
print("4",mystr[0:])
print("5",mystr[:8])
print("6",mystr[::])
print("7",mystr[0:len(mystr):1])
print("8",mystr[::-1]) #reverse string
print("9",mystr[:])
print("10",mystr[-5:-1])#reverse start hua -5ko choda -4 mtlb d se -1 mtlb o tk
print("10",mystr[-11:-1:2])


a="rahul"
print(a[2])

#********************************************

# print("enter your string : ")
# #input(str)
# print("your sting is:",input(str))


b="23 3 34 45"
print(b[0:7:2])