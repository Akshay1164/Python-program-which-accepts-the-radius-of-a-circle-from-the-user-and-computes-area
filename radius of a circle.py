"""
python program which accepts the radius of a circle from the user and computes the area
pi = 3.14
"""
from math import pi
radius = float(input("Enter the radius of circle :"))
area = pi*(radius**2)

print("Area of circle is : %.10f"%area)

