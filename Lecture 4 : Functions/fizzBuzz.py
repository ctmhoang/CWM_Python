def fizz_buzz(input):
    if input % 15 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    else:
        return "Buzz" if input % 5 == 0 else input


print(fizz_buzz(1))
