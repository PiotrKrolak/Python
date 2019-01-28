import math

####################
# deklaracja funkcji
####################
def funcion():
    pass #skipnie te funkcje

def sphere(r):
    """Returns the volume of a sphere with radius r."""
    v=(4/3)*math.pi*r**3
    return v

def rad_to_deg(rad):
    deg = rad*(180/math.pi)
    return deg

def triangle(a, h):
    """Returns the area of a triangle with mase a and height h."""
    return 0.5 * a * h

def cm(feet = 0, inches = 0):
    """Convert a length from feet and inches to centimeters"""
    inhes_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inhes_to_cm + feet_to_cm

###################
# wywolanie funkcji
###################
#print(help(sfera)) # wypisze podpowiedz z funkcjijako help'a

print(sphere(2))
print(rad_to_deg(1))
print(triangle(3,6))
print(cm(23,1))
