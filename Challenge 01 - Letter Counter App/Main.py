print("Hello to the Letter Counter App")

userName = input("Write your name: ")
print("Hello " + str(userName) + "!")
print("I will count the number of times that a specific letter occurs in a message.")
print()

message = input("Please enter a message: ").upper()
letterToFind = input("Which letter would yo like to count: ").upper()

numberOfLetters = 0

for letter in message:
    if letter == letterToFind:
        numberOfLetters += 1

print()
print(str(userName) + ", your text has " + str(numberOfLetters) + " " + str(letterToFind) + "´s in it")