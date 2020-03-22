import math

print("Welcome to the Multiplication/Exponent Table App")
print()

userNumber = float(input("What is the number: "))

print()
print("Multiplication table for " + str(userNumber))
for i in range(1, 11):
    print(str(userNumber) + " x " + str(i) + " = " + str(i*userNumber))

print()
print("Exponent table for " + str(userNumber))
for i in range(1, 11):
    print(str(userNumber) + " ** " + str(i) + " = " + str(userNumber ** i))