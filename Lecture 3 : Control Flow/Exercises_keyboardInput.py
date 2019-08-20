#!/usr/bin/env python3
# https://pythonbasics.org/exercises/
# Keyboard input


# Make a program that asks a phone number.
num = int(input("Please enter your number: "))

if num.isnumeric():
    print("Input accepted: " + str(num))
else:
    print("Invalid input received")

# Make a program that asks the users preferred programming language.
lang = input("\nWhat is your favourite language: ")

print("Your favourite is: " + lang)
