# Accept two numbers from the user
a = input("Enter first number: ")
b = input("Enter second number: ")

print("Before swapping: a =", a, ", b =", b)

# Swap using temporary variable
temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)
