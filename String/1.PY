print(ord("a"))     # chr to ord
print(ord("A"))
print(chr(97))      # ord to chr
print(chr(65))

##################################################

s = "geek"

print(s)
print(s[0])
print(s[-1])
print(s[1])
print(s[-2])

##################################################

s = "geek"
s[0] = "e"  # error: item assignment not supported
print(s)

##################################################

s = """ Hi,
This is python course.
Hope you are enjoying it. """
print(s)










rahul = 23+3
print(type(rahul))
b=int(rahul)
print(b)
print(type(b))




rahul = 23+3j
print(rahul)
print(type(rahul))