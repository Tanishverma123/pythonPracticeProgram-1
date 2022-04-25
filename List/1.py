from re import L


l=[10,20,30,40,50]
print(sum(l))
print(l[2])
print(l[-2])
print(l[-1])
l.append(30)
print(l)
l.insert(1,15)  # 1 index pr 15 insert hoga
l.insert(1000)  # TypeError: insert expected 2 arguments, got 1
print(l)
print(15 in l)   # true or false
print(l.count(30))
print(l.index(30))
print(l.index(30,4,7))
l.remove(20)
print(l)
print(l.pop())
print(l.pop(2))        # 2nd index bala pop ho jaygea 
del l[1]
print(l)
del l[0:2]
print(l)
print(max(l))
print(min(l))
print(sum(l))
l.reverse()
l.sort()
print(l)