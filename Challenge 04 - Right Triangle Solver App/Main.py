import math

print("Welcome to the Right Triangle Solver App")
print()

firstLeg = float(input("What is the first leg of the triangle: "))
secondLeg = float(input("What is the second leg of the triangle: "))

hypotenuse = round( math.sqrt((firstLeg ** 2) + (secondLeg ** 2)), 2)
area = (firstLeg * secondLeg) / 2

print("For a triangle with legs of  " + str(firstLeg) + " and " + str() + " the hypotenuse is " + str(hypotenuse))
print("For a triangle with legs of  " + str(firstLeg) + " and " + str() + " the area is " + str(area))