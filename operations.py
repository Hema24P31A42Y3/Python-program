def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y

print("Options: +, -, *, /")
choice = input("Enter operation: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "+": print("Result:", add(a, b))
elif choice == "-": print("Result:", subtract(a, b))
elif choice == "*": print("Result:", multiply(a, b))
elif choice == "/": print("Result:", divide(a, b))
else: print("Invalid choice")
