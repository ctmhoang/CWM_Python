# https://pythonbasics.org/exercises/
# Random numbers
import random

# just a method to convert & print X


def printx(x):
    x = str(x)
    print("X is " + x)

0,100
# Make a program that creates a random number and stores it into x.
x = random.random()
printx(x)

# Make a program that prints 3 random numbers.
iterator = 1

print("\nbegin loop")

while iterator < 4:
    x = random.randint(0, 10)
    printx(x)
    iterator += 1

print("end of loop\n")


# Create a program that generates 100 random numbers and find the frequency of each number.
