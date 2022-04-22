# list1 = ["rahul","priya","raj","rohit"]
# for item in list1:
#     print(item)

# *******************************************************************

# list2 = [ ["rahul",1],["harry",2],["larry",3],["carry",6] ]
# for item in list2:
#     print(item)

# *******************************************************************

# list2 = [ ["rahul",1],["harry",2],["larry",3],["carry",6] ]
# dict1 = dict(list2)
# for item in dict1:
#     print(item)

# *******************************************************************

list2 = [["rahul", 1], ["harry", 2], ["larry", 3], ["carry", 6]]
dict1 = dict(list2)
for ite, lollypop in dict1.items():
    print(ite, "and lolly is ", lollypop)

# *******************************************************************

l = [2,3,4,5,6,7,8,9,10,12]
for i in l:
    if i%2 == 0:
        print(i)