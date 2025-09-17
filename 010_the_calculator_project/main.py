# 100 Days of Code: Python
# Day 10 Project: The Calculator Project

def add(n1: float, n2: float):
    return n1 + n2


def subtract(n1: float, n2: float):
    return n1 - n2


def multiply(n1: float, n2: float):
    return n1 * n2


def divide(n1: float, n2: float):
    if n2 == 0:
        print("Cannot divide by zero.")
        return None
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Enter the first number:\n"))
    should_accumulate = True

    while should_accumulate:
        print(f"Available operations:", " ".join(operations.keys()))
        operation_symbol = input("Pick an operation:\n").strip()
        if operation_symbol not in operations:
            print("Invalid operation. Try again.")
            continue
        num2 = float(input("Enter the next number:\n"))
        result = operations[operation_symbol](num1, num2)
        if result is None:
            continue
        print(f"{num1} {operation_symbol} {num2} = {result:,.2f}")

        choice = input(f"Type 'y' to continue calculating with {result:,.2f},\n "
                       f"or type 'n' to start a new calculation,\n"
                       f"or type 'q' to quit the program:\n").strip().lower()

        if choice == 'y':
            num1 = result
        elif choice == 'n':
            should_accumulate = False
        elif choice == 'q':
            return False
    return True


print("Welcome to the calculator project")

while True:
    if not calculator():
        break
