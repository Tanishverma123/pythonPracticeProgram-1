def getevenodd(l):
    even=[]
    odd=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:odd.append(i)
    return even,odd

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
even,odd = getevenodd(l)
print(even)
print(odd)


#######################################################

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
even=[x for x in (l) if x%2==0]
print(even)
odd=[x for x in (l) if x%2!=0]
print(odd)