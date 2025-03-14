# a basic calculator that takes two numbers and an operation as input and performs the operation on the two numbers

def basic_calculator(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Error: Division by zero is undefined.")
    else:
        print("Error: Invalid operation. Please input a valid operation: +, -, *, /")

# Get input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter the operation (addition (+), subtraction (-), multiplication (*), division (/)): ")

basic_calculator(num1, num2, operation)