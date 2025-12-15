
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
if num2 != 0:
    division = num1 / num2
    print("Division =", division)
else:
    print("Division not possible (cannot divide by zero)")
