# Write a program that calculates the area of a circle from
# the radius. The radius will be an integer read in from the
# keyboard. You will need to use the constant math.pi
# (import math)

import math
from msilib.schema import Error

radius = 0

while True:
    try:
        radius = int(input("Enter the radius value: "))
        if radius <= 0:
            raise Error
        break
    except:
        print('wrong input, enter positive integer value')


print(f'The area is {str(float(math.pi * radius**2))}')