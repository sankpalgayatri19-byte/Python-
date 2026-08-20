import math

a = int(input("Enter 1st positive int:-"))
b = int(input("Enter 2nd positive int:-"))

lcm = (a * b) // math.gcd(a, b)

print("LCM is:-", lcm)
