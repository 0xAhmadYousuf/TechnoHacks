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
        return "Cannot divide by zero."

# Take input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display menu for operations
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take input for operation choice
choice = input("Enter choice (1/2/3/4): ")

# Perform the selected operation
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    result = "Invalid input"

# Display the result
print("Result:", result)
