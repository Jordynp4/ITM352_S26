#!/usr/bin/env python3
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")


def choose_operation():
    print("Choose operation:")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    while True:
        choice = input("Enter choice (1/2/3/4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return choice
        print("Invalid selection, please choose 1-4.")


def main():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    choice = choose_operation()
    try:
        if choice == "1":
            result = add(a, b)
            op = "+"
        elif choice == "2":
            result = subtract(a, b)
            op = "-"
        elif choice == "3":
            result = multiply(a, b)
            op = "*"
        else:  # choice == "4"
            result = divide(a, b)
            op = "/"
        print(f"{a} {op} {b} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    main()
