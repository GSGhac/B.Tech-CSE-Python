import math

def area_of_triangle(a, b, c):
    # check if sides form a valid triangle
    if (a + b > c) and (a + c > b) and (b + c > a):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    else:
        return "The combination of sides is not possible"

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

print(area_of_triangle(a, b, c))
