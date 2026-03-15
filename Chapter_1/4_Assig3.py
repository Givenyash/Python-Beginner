# Question - take diameter as input and calculate area of circle.

# import math 
diameter = float(input(" Enter diameter of a circle : "))
radius = (diameter/2)
area = 3.14 * (radius **2)       # area = math.pi *(radius **2)
print("The Area of Circle is :" , area)