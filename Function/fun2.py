def fun():
    print("fun() called")  # it will be printed when fun is called

print("before calling fun()")
fun()  # fun() is called
print("after calling fun()")

#################################################################

def fun():
    print("fun() called")  # it will be printed when fun is called

print("before calling fun()")
fun()  # fun() is called
fun()  # fun()  is called
print("after calling fun()")

#################################################################

def printDate(d, m, y):
    print(d, m, y, sep='-')

print("India became independence on:")
printDate("15", '08', '1947') # calling function

#################################################################

def getDate(d, m, y):
    return d + '-' + m + '-' + y

print("India became independence on:")
d = getDate('15', '08', '1947')     # calling fun to return data
print(d)

#################################################################

def greet_msg():
    print("Hi")
    print("welcome to GeeksforGeeks")

def exit_msg():
    print("please visit again")
    print("Bye")

greet_msg()         # calling fun()
print("Hope you are enjoying")
exit_msg()          # calling fun()