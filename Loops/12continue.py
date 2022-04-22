from traceback import print_tb


i = 0
while True:
    if i + 1 < 5:
        i = i + 1
        continue
    print(i + 1, end=" ")
    if i == 33:
        break
    i = i + 1

####################333333333

l = [12, 14, 15, 17, 18, 23, 21]

for x in l:
    if x % 3 == 0:
        continue
    print(x)

#86000000000000000000000000000000000

l = [10, 16, 17, 18, 9, 15,21,13]

for x in l:
    if x % 5 == 0:
        continue
    
    if x%7==0:
        continue
        
    print(x)
print("Bye")

######################################

i = 0

while i <= 5:

    if i == 3:
        i = i + 1
        continue
    print(i, i * i)
    i = i + 1

######################################

l = [10,16,17,18,19,15]

for x in l:
    if x%5==0:      # if multiple of 5, continue
        continue
    print(x)
    

print()
for x in l:
    if x%5!=0:
        print(x)