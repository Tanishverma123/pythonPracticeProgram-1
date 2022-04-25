l=[1,2,3,4,5,6,7,8,8]
ans=0
for i in l:
    ans=i+ans

avg=ans/len(l)
print(avg)


##################################

def average(l):
    return sum(l)/len(l)

print(average(l))