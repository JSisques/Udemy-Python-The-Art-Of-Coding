import math

print("Welcome to the Grade Sorter App")
print()

firstGrade = int(input("What is your first grade (0-100): "))
secondGrade = int(input("What is your second grade (0-100): "))
thirdGrade = int(input("What is your third grade (0-100): "))
fourthGrade = int(input("What is your fourth grade (0-100): "))
print()

grades = [firstGrade, secondGrade, thirdGrade, fourthGrade]

print("Your grades are: " + str(grades))
print()

grades.sort(reverse=True)
print("Your grades from the highest to lowest are: " + str(grades))

print("The lowest grades now will be dropped.")
removedValue = grades.pop()
print("Removed value: " + str(removedValue))
removedValue = grades.pop()
print("Removed value: " + str(removedValue))
print()

print("Your grades are " + str(grades))
print("Nice work!")
