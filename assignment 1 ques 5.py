#Program to determine sine and cosine in increments
#Importing math modules for trignometric functions
import math
#Defining loop for 15 degree increments
for i in range(0,346,15):
     sine=math.sin(math.radians(i))
     cosine=math.cos(math.radians(i))
     print(f"sin({i})={sine:.4f} and cos({i})={cosine:.4f}")
