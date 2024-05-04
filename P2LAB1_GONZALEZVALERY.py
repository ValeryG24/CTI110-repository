#Valery Gonzalez
#April 13, 2024
#P2Lab1
# Using math expressions
import math

#Get the radius user
radius =float (input("Enter the radius: "))

#Calculate circum, diameter, area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display results
print(f"The diameter of the circle is {diam: .1f} ")
print(f"The circumference of the circle is {cir: .2f}")
print(f"The area of the circle is {area: .3f} ")
