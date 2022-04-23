
n = int(input("Enter the total items : "))
r = int(input("Enter the number of items to be arrange : "))
# calculate n factorial
fact_n = 1 
for i in range(1, n+1):  # (n,0,-1)  negetive index
    fact_n *= i

# calculate (n-r) factorial
x = n-r
fact_x = 1
for i in range(1, x+1):  # (n,0,-1)  negetive index
    fact_x *= i

p = fact_n//fact_x
print("P = ", p)