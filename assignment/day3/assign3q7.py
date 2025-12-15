def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
def power(x, n):
    if n == 0:          
        return 1
    else:
        return x * power(x, n - 1)
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result =", power(base, exp))
