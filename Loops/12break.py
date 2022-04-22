# i=0
# while(True):
#     print(i+1,end=" ")
#     if(i==33):
#         break
#     i=i+1
    
    
########################
i=1

while i<=5:
    
    if i==3:
        break
    print(i)
    
    i=i+1

print(i)


#######################33

n = int(input("Enter n:\n"))

for x in range(2, n + 1):
    if n % x == 0:
        print(x)
        break

print("\n while loop")

x=2

while x<=n:
    if n%x ==0:
        print(x)
        break
    x = x+1
    
    
    
