# print("hllo world ")

# #**************************************************************************************

# #this is single line commnt
# ###
# # this is multiline comment
# ###

# #**************************************************************************************

# # print("this is first line",end=" this is aage ka matter")
# print("this is first line","this is aage ka matter","hllo",)
# print("this is first line""this is aage ka matter","hllo",)


print("rahul is a \'good boy")
print("rul is a \\good boy")
print("raul is a \ngood boy")
print("ahul is \ra good boy")
print("rahul is a \tgood boy")
print("rahul is a \bgood boy")
print("rahl is a \fgood boy")
print("rahul is a \ooo good boy")
# print("rahul is a \xhhgood boy")




# def task(r, unit, arr):
#      n = len(arr);
#  #We calculate the total amount of food that the rats can consume
#  sum = r * unit:
#  sum_arr = 0:
#  #We calculate the total amount in the households
#  for i in arr:
#  sum_arr = sum_arr + i
#  if len(arr) == 0:
#  return -1
#  elif sum > sum_arr:
#  return 0
#  #Where 1 represents that the household has surplus food for the rats 
#  elif sum < sum_arr:
#  return 1



print(""" rHUL
EWOIO
IWJFOJOIW""")








# def FreqCheck(arr):
#     elements_count = {}
#     a=[]
#     for element in arr:
#         if element in elements_count:
#             elements_count[element] += 1
#         else:
#             elements_count[element] = 1
#     for key, value in elements_count.items():
#         if(value>=4):
#             return key
 
            
# def get_rows(grid):
#     return [[c for c in r] for r in grid]
# def get_cols(grid):
#     return zip(*grid)
# def get_backward_diagonals(grid):
#     b = [None] * (len(grid) - 1)
#     grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
#     return [[c for c in r if c is not None] for r in get_cols(grid)]


# n=int (input())
# grid=[]
# for i in range(n):
#     grid.append(list(map(int,input().split(" "))))
# FinalList=[]    
# for i in range(n):
#     FinalList.append(FreqCheck(grid[i]))
# columns = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
# for i in range(len(columns)):
#     FinalList.append(FreqCheck(columns[i]))
# diagonals=get_backward_diagonals(grid)
# for i in range(len(diagonals)):
#     FinalList.append(FreqCheck(diagonals[i]))
    
# FinalList=[i for i in FinalList if i]
# if len(FinalList)==0:
#     print('-1')
# else:
#     print(min(FinalList))



a=23
b=34
print(a+b)



num1 = int(input("enter the first number : "))
num2 = int(input("enter the second number : "))
sum = num1+num2
print(sum)