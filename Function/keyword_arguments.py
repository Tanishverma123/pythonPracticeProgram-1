def printItem(id, name="NA", price="NA"):
    print(f"Id is {id}")
    print(f"Name is {name}")
    print(f"Price is {price}")


printItem(101, "abc", 100)  # passing param by positional-arg
print()
printItem(id=102, name="xyz", price=200)  # passing param by keyword-arg

printItem(name="abc", price=200, id=102)  # passing param by keyword-arg, not in order
