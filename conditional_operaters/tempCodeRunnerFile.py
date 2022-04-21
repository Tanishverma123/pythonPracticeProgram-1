



# welcome to Rahul's calculator

# function to add
def addition(a, b):
    return a+b

# function for subtraction
def subtraction(a, b):
    return a-b

# function for multiplication
def multiplication(a, b):
    return a*b

# function for division
def division(a, b):
    if(b == 0):
        print("you can't take divisior 0 : ")
        exit()
    return a/b

# function for modulo
def modulo(a, b):
    if(b == 0):
        print("you can't take divisior 0 : ")
        exit()
    return a % b

# fumction for power
def power(a,b):
    return a**b

# function for square
def square(num):
    return num*num

# function for cube
def cube(a):
    return a*a*a

# function for square root
def square_root(a):
    return a**0.5

# function for cube root
def cube_root(a):
    return a**(1/3)



# function for taking input
def calculator():
    def variable():
        print("In which type do you want to take number ")
        print("""1. Int      2. Float""")
        type = (input("Enter your choice 1 or 2 : "))
        if type == "1":
            num1 = int(input("Enter the first number : "))
            num2 = int(input("Enter the second number : "))
        elif type == "2":
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))
        else:
            print("Invalid input please type 1 or 2 ")
            variable()

        return num1, num2



    print("which operation d2o you want to perform : ")
    print("""chose operator :
                1. Addition
                2. Subtraction
                3. Division
                4. Multiplication
                5. Modulo""")
    print("""Enter   + for Addition
            - for Subtraction
            / for division
            * for multiplication
            % for modulo
            ^ for power
            sqr for square 
            cube for cube 
            sqrroot for square root
            cuberoot for cube root """)

    optr = (input())
    if optr == "+":
        num1, num2 = variable()
        result = addition(num1, num2)
        print("Result : a+b = ", result)

    if optr == "-":
        num1, num2 = variable()
        result = subtraction(num1, num2)
        print("Result : a-b = ", result)

    if optr == "/":
        num1, num2 = variable()
        result = division(num1, num2)
        print("Result : a/b = ", result)

    if optr == "*":
        num1, num2 = variable()
        result = multiplication(num1, num2)
        print("Result : a*b = ", result)

    if optr == "%":
        num1, num2 = variable()
        result = modulo(num1, num2)
        print("Result : a%b = ", result)

    if optr == "^":
        base = int(input("Enter the base value : "))
        power = int(input("Enter the power : "))
        result = power(base,power)
        print("Result : ",a ,"to the power ",b," = ", result)

    if optr == "sqr":
        num = int(input("Enter number for finding square : "))
        result = square(num)
        print("Result : a^2  = ",result)

    if optr == "cube":
        num = int(input("Enter number for finding cube : "))
        result = cube(num)
        print("Result a^3 = ",result)

    if optr == "sqrroot":
        num = int(input("Enter number for finding square root : "))
        result = square_root(num)
        print("The root of ",num ," is ",result)

    if optr == "cuberoot":
        num = int(input("Enter number for finding square root : "))
        result = cube_root(num)
        print("The cube root of ",num ," is ",result)
        
    print("Do you want to continue calculate : ")
    print("""  1 for continue     2 for quit """)
    con_quit = int(input("Enter your choice : "))
    if con_quit == 1:
        calculator()
    elif con_quit == 2:
        exit()
    
calculator()