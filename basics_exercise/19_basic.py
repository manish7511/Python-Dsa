def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The maximum number is:", find_maximum(num1, num2))