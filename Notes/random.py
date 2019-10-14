import random 
import string
print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3,4]))
print(random.choices([1,2,3,4], k=2))
print(string.ascii_letters + string.digits)
numbers = [1,2,3,4]
numbers = random.shuffle(numbers)
