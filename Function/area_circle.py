def area(r):
    return 3.14*r*r

def circumference(r):
    return 2*3.14*r

radius = int(input("enter the radius of circle : "))
aor=area(radius)
aoc=circumference(radius)
print("area of circle : ",aor)
print("area of circumference : ",format(aoc,".3f"))
print("area of circumference : ",round(aoc,3))