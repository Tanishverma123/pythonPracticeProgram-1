l=[2,5,6,1,7,8,9,2,4,3]
for i in range(len(l)//2-1):
    l[i], l[len(l)-i-1] = l[len(l)-i-1], l[i]
print (l)