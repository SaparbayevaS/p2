#1
import math
n = int(input("Input degree: "))
m = n * ( math.pi / 180)
print("Output radian: ", m)
print()
#2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
area = (a + b)/2 * h
print("Expected Output: ", area)
print()
#3
import math
s = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area = (s * (l**2)) / (4 * math.tan(math.pi / s))
print("The area of the polygon is: ", area)
print()
#4
l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
area = l * h
print("Expected Output: ", area)