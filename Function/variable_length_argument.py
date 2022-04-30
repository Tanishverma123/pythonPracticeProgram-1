def sum(*elements):
    res = 0

    for x in elements:
        res = res + x
    return res


print(sum(10, 20))
print(sum(10, 20, 30))
print(sum(10))
print(sum())

#############################################################

def sum(init_sum, *elements):
    res = init_sum

    for x in elements:
        res = res + x
    return res

print(sum(0, 10, 20))   # 0 assigned to init_sum
print(sum(5, 10, 15))   # 5 assigned to init_sum

#############################################################

def printElements(*elements):
    print(*elements)  # print tuple


printElements(101, "abc", 100)
printElements(102, "NA", 200)

#############################################################

def printDetails(**details):
    for d, v in details.items():
        print(f"{d} {v}")


printDetails(id=101, name="abc", price=100)
print()
printDetails(id=102, name="xyz")

#############################################################

def printDetails(id,**details):
    print(f"Details of {id}")
    
    for d, v in details.items():
        print(f"{d} {v}")


printDetails(101, name="abc", price=100) 
print()
printDetails(102, name="xyz")