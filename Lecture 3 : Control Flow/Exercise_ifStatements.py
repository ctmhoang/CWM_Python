#!/usr/bin/env python3
# https://pythonbasics.org/exercises/
# If statements

# Make a program that asks the number between 1 and 10.
# If the number is out of range the program should display “invalid number”.

num = int(input("Enter a number between 1 and 10: "))

if num.isnumeric() and num in range(1, 11):
    print("Valid input: ", num)
else:
    print("Invalid input received")

# Make a program that asks a password.

pass = input("Passwords: ")
