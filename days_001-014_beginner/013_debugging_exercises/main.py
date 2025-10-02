# 100 Days of Code: Python
# Day 13 Project: Debugging Exercises

# Hints:
# The code below contains errors: identify them and add comments.
# Uncomment, correct and execute them.

number = int(input("Which number do you want to check?"))

if number % 2 = 0:   # Should be a comparison '==' not an assignment '='.
    print("This is an even number.")
else:
    print("This is an odd number.")

year = input("Which year do you want to check?")   # The input need to be converted to an int.

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:   # Should be an 'and' not an 'or'.
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])   # 'number' should not be in a list.
