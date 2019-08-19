#!/usr/bin/env python3
# exercises https://pythonbasics.org/exercises/

string = "Hello World World World"
replacedstring = string.replace("World", "Universe", 1)
print(replacedstring)

# Can a string be replaced twice?
replacedstring = string.replace("World", "Universe", 2)
print(replacedstring)

# Does replace only work with words or also phrases?
replacedstring = string.replace("Hello World", "Hi Universe", 1)
print(replacedstring)
