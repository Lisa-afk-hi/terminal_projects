def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operator!"

        print("Result:", result)
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    while True:
        calculator()
        cont = input("Do you want to calculate again? (y/n): ").lower()
        if cont != 'y':
            print("Goodbye!")
            break
