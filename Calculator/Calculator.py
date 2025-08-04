'''
Task 1 :Build a Calculator CLI App.
Objective: Create a command-line calculator supporting basic operations.
Tools: Python, VS Code.
Deliverables: A Python script (Calculator.py)

Hints/Mini Guide:
1.Use functions for each operation (+, -, *, /)
2.Take user input using input()
3.Loop until user chooses to exit

Outcome: A well-structured schema.
'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Welcome to the Calculator CLI App!")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()