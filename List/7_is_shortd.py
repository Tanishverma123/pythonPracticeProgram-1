l=[2,3,4,5,6,1,7,8,9]
for i in range(0,len(l)-1):
    if l[i]>=l[i+1]:
        print("NO")
        break
else:print("YES")
    