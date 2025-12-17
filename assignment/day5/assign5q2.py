def add (a,b):
    return a + b
def subtract (a,b):
    return a - b
def multiply (a,b):
    return a * b
def divide (a,b):
    if b == 0:
        return "Error! Division by zero"
    return a/b

print("Simple Calculator using Functions")

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

print("Addition:", add(a, b))
print("subtract:", subtract(a,b))
print("multiply:", multiply(a,b))
print("divide:", divide(a,b))