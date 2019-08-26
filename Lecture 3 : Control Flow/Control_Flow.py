'''
File: Control_Flow.py
Project: artlist
File Created: Monday, 26th August 2019 5:10:40 am
Author: artlist
-----
Last Modified: Monday, 26th August 2019 5:40:46 am
Modified By: artlist
-----
'''

# Write a program that display even number from 1 to 10
# Then print message "We have 4 even numbers"
# Do not use step

counter = 0
for i in range(1, 10):
    if i % 2 == 0:
        counter += 1
        print(i)
print("We have {0} even numbers".format(counter))

# or can use f"We have {count} even numbers"
