# a=23
# b=3
# # c= sum({a,b})
# # c= sum((a,b))
# c= sum([a,b])
# print(c)

#**************************************************************

# def function1(a,b):
#     print("Hello you are in function 1")

# def function2(a,b):
#     average = (a+b)/2
#     print(average)
    
# # function1()
# # function1()
# # function1()
# function2(5,6)

#***************************************************************


# def function2(a,b):
# #   " " " This is function which will calculate average of the numbers " " "
#     average = (a+b)/2
#     # print(average)
#     return average

# # print(function2.__doc__)
# v=function2(5,6)
# print(v)

#*****************************************************************


# def function3(a,b):
#     print(a+ +b)

# print("black","bear")

#*****************************************************************

# x=20
# def FunctionName1(x):
#     return x+5
# print(x)

#****************************************************************

# def is_leap(year):
#     leap = False
#     if year%4==0 and year%100!=0 :
#         leap = True
#     elif year%400 ==0:
#         leap = True
#     # Write your logic here
    
#     return leap

# year = int(input())
# print(is_leap(year))

#****************************************************************

n = int(input())
i=range(1,n+1)
j=(i)
print(*range(1,n+1),sep="")
